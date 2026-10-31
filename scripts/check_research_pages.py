#!/usr/bin/env python3
"""Validate the static research reading surfaces against manuscript evidence.

Run from any directory. No network, browser or third-party Python packages needed.
The accepted source, when available as ../source, adds independent label/heading
coverage checks. HTML parsing never executes JavaScript.
"""
from collections import Counter
from datetime import date
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TOPIC_PAGES = (
    "vision-language-action-models.html", "learning-from-demonstration.html",
    "robot-world-models.html", "robot-memory.html", "robot-self-improvement.html",
    "robot-navigation.html",
)
PAGE_NAMES = ("index.html", "paper.html", "taxonomy.html", "evaluation.html", "read.html", "topics.html", *TOPIC_PAGES)
SITE = "https://jethrojames.github.io/awesome-robots-icl/"
TITLE = "In-Context Learning for Robots: Methods and Applications"
ARXIV = "2609.36012"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def plain(value):
    value = unicodedata.normalize("NFKC", unescape(value))
    return " ".join(value.replace("\u00ad", "").split())


def comparable(value):
    return re.sub(r"[^a-z0-9]+", " ", plain(value).lower()).strip()


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.raw = path.read_text(encoding="utf-8")
        self.stack = []
        self.ids = Counter()
        self.ordered_ids = []
        self.links = []
        self.meta = {}
        self.canonicals = []
        self.title_parts = []
        self.visible_parts = []
        self.abstract_parts = []
        self.headings = []
        self.current_heading = None
        self.scripts = []
        self.current_script = None
        self.images = []
        self.tags = Counter()
        self.feed(self.raw)
        self.close()
        self.visible = plain(" ".join(self.visible_parts))
        self.abstract = plain("".join(self.abstract_parts))
        self.title = plain("".join(self.title_parts))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags[tag] += 1
        ids = {x for x in (a.get("id"), a.get("name") if tag == "a" else None) if x}
        self.ids.update(ids)
        for value in (a.get("id"), a.get("name") if tag == "a" else None):
            if value and value not in self.ordered_ids:
                self.ordered_ids.append(value)
        for key in ("href", "src", "data" if tag == "object" else ""):
            if key and a.get(key):
                self.links.append((tag, key, a[key]))
        if tag == "meta":
            self.meta.setdefault(a.get("name", a.get("property", "")), []).append(a.get("content", ""))
        if tag == "link" and "canonical" in a.get("rel", "").split():
            self.canonicals.append(a.get("href", ""))
        if tag == "img":
            self.images.append(a)
        if tag == "script":
            self.current_script = {"type": a.get("type"), "text": "", "src": a.get("src")}
        if re.fullmatch(r"h[1-6]", tag):
            self.current_heading = {"tag": tag, "text": ""}
        if tag not in VOID:
            self.stack.append((tag, a))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == "script" and self.current_script is not None:
            self.scripts.append(self.current_script)
            self.current_script = None
        if self.current_heading and self.current_heading["tag"] == tag:
            self.headings.append(plain(self.current_heading["text"]))
            self.current_heading = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self.current_script is not None:
            self.current_script["text"] += data
        if self.current_heading is not None:
            self.current_heading["text"] += data
        tags = {t for t, _ in self.stack}
        if "title" in tags:
            self.title_parts.append(data)
        if "body" in tags and not tags.intersection({"script", "style", "template"}):
            self.visible_parts.append(data)
            if any(set(a.get("class", "").split()) & {"abstract-text", "record-abstract-text"}
                   for _, a in self.stack):
                self.abstract_parts.append(data)


def manuscript_sources(source):
    """Follow actual input/include commands, not unused table files."""
    found = {}

    def visit(path):
        path = path.resolve()
        if path in found:
            return
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"(?<!\\)%[^\n]*", "", text)
        found[path] = text
        for name in re.findall(r"\\(?:input|include)\s*\{([^}]+)\}", text):
            target = source / name
            if target.suffix != ".tex":
                target = target.with_suffix(".tex")
            if target.is_file():
                visit(target)

    visit(source / "robot-icl-survey.tex")
    return found


def validate(source):
    errors, notes = [], []
    metrics = {}
    revision_date = date.fromisoformat(json.loads((DOCS / "assets/manuscript-release.json").read_text())["author_revision_date"])
    visible_dates = (revision_date.isoformat(), revision_date.strftime("%Y/%m/%d"),
                     f"{revision_date.day} {revision_date:%B %Y}", f"{revision_date:%B} {revision_date.day}, {revision_date.year}")

    def require(condition, message):
        if not condition:
            errors.append(message)

    pages = {}
    for name in PAGE_NAMES:
        if not (DOCS / name).is_file():
            errors.append(f"Missing page: {name}")
            continue
        pages[name] = Page(DOCS / name)
    if len(pages) != len(PAGE_NAMES):
        return errors, notes, metrics

    for name, page in pages.items():
        duplicates = [key for key, n in page.ids.items() if n > 1]
        require(not duplicates, f"{name}: duplicate anchors: {duplicates[:12]}")
        require(page.tags["h1"] == 1, f"{name}: expected one h1, got {page.tags['h1']}")
        require(bool(page.title), f"{name}: page title is missing")
        require(page.canonicals == [SITE + ("" if name == "index.html" else name)], f"{name}: canonical URL mismatch")
        require(len(page.meta.get("description", [])) == 1 and bool(page.meta["description"][0].strip()), f"{name}: page description is missing or repeated")
        require(not any("noindex" in v.lower() for v in page.meta.get("robots", [])), f"{name}: noindex is present")
        require("robot icl survey" in comparable(page.visible), f"{name}: visible Robot ICL Survey identity missing")
        # Version details live on the paper record; all reading pages link to it.
        if name == "paper.html":
            require(ARXIV in page.visible, "paper.html: visible arXiv identifier missing")
            require(any(comparable(value) in comparable(page.visible) for value in visible_dates), "paper.html: author revision date is not visible")
            require(bool(re.search(r"arxiv(?::\s*2609\.36012)?(?:\s+record)?\s*(?:[·:—–-]\s*)?(?:remains\s+)?v1", page.visible, re.I)), "paper.html: distinct arXiv v1 status missing")
        else:
            require(any(tag == "a" and urlsplit(url).path == "paper.html" for tag, _, url in page.links), f"{name}: paper and version record link missing")
        require(any("supplement-s1.zip" in url for _, _, url in page.links), f"{name}: Supplement S1 download missing")
        for image in page.images:
            require("alt" in image, f"{name}: image lacks alt: {image.get('src')}")
        for tag, attribute, url in page.links:
            parts = urlsplit(url)
            if parts.scheme in {"mailto", "tel", "data", "javascript"}:
                require(parts.scheme != "javascript", f"{name}: JavaScript-only navigation: {url}")
                continue
            if parts.netloc:
                if parts.netloc.lower() != "jethrojames.github.io" or not parts.path.startswith("/awesome-robots-icl/"):
                    continue
                relpath = unquote(parts.path[len("/awesome-robots-icl/"):])
                target = DOCS / (relpath or "index.html")
            elif parts.path.startswith("/"):
                relpath = unquote(parts.path)
                if relpath.startswith("/awesome-robots-icl/"):
                    relpath = relpath[len("/awesome-robots-icl/"):]
                target = DOCS / relpath.lstrip("/")
            else:
                target = page.path.parent / unquote(parts.path) if parts.path else page.path
            if target.is_dir():
                target = target / "index.html"
            target = target.resolve()
            require(target.is_relative_to(DOCS.resolve()), f"{name}: link escapes published docs: {url}")
            require(target.is_file(), f"{name}: missing {attribute} target: {url}")
            fragment = unquote(parts.fragment).split(":~:text=", 1)[0]
            if target.is_file() and target.suffix == ".html" and fragment:
                target_page = pages.get(target.name) if target.parent == DOCS else None
                target_page = target_page or Page(target)
                require(fragment in target_page.ids, f"{name}: unresolved fragment: {url}")

    metadata_path = DOCS / "assets/paper-metadata.json"
    require(metadata_path.is_file(), "Canonical paper-metadata.json is missing")
    metadata = json.loads(metadata_path.read_text()) if metadata_path.is_file() else {}
    canonical_abstract = plain(metadata.get("abstract", ""))
    require(bool(canonical_abstract), "Canonical abstract is empty")
    for name in ("index.html", "paper.html"):
        page = pages[name]
        require(page.abstract == canonical_abstract, f"{name}: visible abstract differs from canonical metadata")
        require([plain(x) for x in page.meta.get("citation_abstract", [])] == [canonical_abstract], f"{name}: citation_abstract differs")
        require(page.meta.get("citation_title") == [TITLE], f"{name}: citation_title differs")
        require(page.meta.get("citation_publication_date") == ["2026/09/28"], f"{name}: publication date must not become website update date")
        require(len(page.meta.get("citation_author", [])) == 39, f"{name}: citation authors count differs from 39")
        require(page.meta.get("citation_arxiv_id") == [ARXIV], f"{name}: arXiv metadata differs")
        graph_articles = []
        for script in page.scripts:
            if script["type"] == "application/ld+json":
                try:
                    data = json.loads(script["text"])
                    graph_articles.extend(x for x in data.get("@graph", [data]) if x.get("@type") == "ScholarlyArticle")
                except (ValueError, TypeError, AttributeError) as e:
                    errors.append(f"{name}: invalid JSON-LD: {e}")
        require(len(graph_articles) == 1, f"{name}: expected one ScholarlyArticle")
        for article in graph_articles:
            require(plain(article.get("abstract", "")) == canonical_abstract, f"{name}: JSON-LD abstract differs")
            require(article.get("datePublished") == "2026-09-28", f"{name}: JSON-LD publication date differs")
            require(article.get("dateModified") == metadata["author_revision_date"], f"{name}: JSON-LD author revision differs")
    require(pages["index.html"].meta.get("citation_author") == pages["paper.html"].meta.get("citation_author"), "Author order differs between landing pages")
    csl = json.loads((DOCS / "citation.json").read_text())
    require(len(csl) == 1 and plain(csl[0].get("abstract", "")) == canonical_abstract, "CSL JSON abstract differs")
    ris = (DOCS / "citation.ris").read_text()
    ris_abstracts = re.findall(r"^AB\s+-\s+(.*)$", ris, re.M)
    require([plain(x) for x in ris_abstracts] == [canonical_abstract], "RIS abstract differs")

    sitemap = ET.parse(DOCS / "sitemap.xml")
    sitemap_urls = [x.text for x in sitemap.findall(".//{*}loc")]
    locations = set(sitemap_urls)
    require(len(sitemap_urls) == len(locations), "sitemap.xml repeats URLs")
    for name in PAGE_NAMES:
        require(SITE + ("" if name == "index.html" else name) in locations, f"sitemap.xml lacks {name}")

    with zipfile.ZipFile(DOCS / "assets/supplement-s1.zip") as z:
        references = json.loads(z.read("Supplement-S1/references.json"))
    known_source_urls = {item["source_url"] for item in references if item.get("source_url")}
    reader = pages["read.html"]
    require(reader.path.stat().st_size < 5_000_000, "read.html exceeds the 5 MB single-document target")
    require(reader.tags["iframe"] == 0, "read.html must contain HTML, not an embedded PDF")
    require(len(reader.visible.split()) > 30000, "read.html has insufficient static text for the full survey")
    expected_refs = {"ref-" + item["key"] for item in references}
    actual_refs = {key for key in reader.ids if key.startswith("ref-")}
    require(actual_refs == expected_refs, f"Reference coverage mismatch: missing {sorted(expected_refs - actual_refs)[:12]}, extra {sorted(actual_refs - expected_refs)[:12]}")
    require(len(references) == metadata["references"], "Supplement reference count differs from release metadata")
    expected_order = ["ref-" + item["key"] for item in sorted(references, key=lambda item: item["number"])]
    actual_order = [key for key in reader.ordered_ids if key.startswith("ref-")]
    require(actual_order == expected_order, "read.html bibliography anchor order differs from accepted reference numbers")
    compact_text = comparable(reader.visible).replace(" ", "")
    plain_titles = [item for item in references if "\\" not in item["title"] and "$" not in item["title"] and len(item["title"].split()) >= 5]
    absent_titles = [item["key"] for item in plain_titles if comparable(item["title"]).replace(" ", "") not in compact_text]
    require(not absent_titles, f"read.html loses reference titles: {absent_titles[:15]}")
    for anchor in ("sec-introduction", "sec-foundations", "sec-methods", "sec-data", "sec-landscape", "sec-applications", "sec-evaluation", "sec-discussion", "sec-conclusion", "sec-references"):
        require(anchor in reader.ids, f"read.html missing stable section: {anchor}")
    require(reader.tags["math"] > 0, "read.html lacks static MathML; verify formula preservation")
    require(TITLE in reader.visible, "Full paper title not visible in read.html")
    if csl:
        missing_authors = []
        for author in csl[0].get("author", []):
            full_name = plain(author.get("given", "") + " " + author.get("family", ""))
            if comparable(full_name) not in comparable(reader.visible):
                missing_authors.append(full_name)
        require(not missing_authors, f"read.html loses named authors: {missing_authors}")
    for name in ("taxonomy.html", "evaluation.html"):
        require(len(pages[name].visible.split()) >= 400, f"{name}: substantive static content is missing")
        require(pages[name].tags["table"] > 0, f"{name}: expected native HTML comparison table")

    # Research routes must remain discoverable and point back to the one paper.
    graph = {name: set() for name in pages}
    for name, page in pages.items():
        for tag, attribute, url in page.links:
            if tag != "a" or attribute != "href":
                continue
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                if not url.startswith(SITE):
                    continue
                target = urlsplit(url[len(SITE):]).path or "index.html"
            else:
                target = parts.path or name
            if target in pages:
                graph[name].add(target)
    reachable, pending = set(), ["index.html"]
    while pending:
        name = pending.pop()
        if name not in reachable:
            reachable.add(name)
            pending.extend(graph[name] - reachable)
    require(reachable == set(pages), f"Pages unreachable from homepage links: {sorted(set(pages) - reachable)}")
    require(set(TOPIC_PAGES) <= graph["topics.html"], "topics.html must link to every research topic")
    topic_titles = [pages[name].title for name in TOPIC_PAGES]
    topic_descriptions = [pages[name].meta.get("description", [""])[0] for name in TOPIC_PAGES]
    require(len(set(topic_titles)) == len(TOPIC_PAGES), "Research topics repeat page titles")
    require(len(set(topic_descriptions)) == len(TOPIC_PAGES), "Research topics repeat descriptions")
    for name in ("topics.html", *TOPIC_PAGES):
        page = pages[name]
        structured_pages = []
        for script in page.scripts:
            if script["type"] != "application/ld+json":
                continue
            try:
                data = json.loads(script["text"])
                nodes = data.get("@graph", [data])
                structured_pages.extend(node for node in nodes if node.get("@type") in {"WebPage", "CollectionPage"})
                require(not any(node.get("@type") == "ScholarlyArticle" for node in nodes), f"{name}: topic must not be represented as a separate paper")
            except (ValueError, TypeError, AttributeError) as e:
                errors.append(f"{name}: invalid JSON-LD: {e}")
        require(len(structured_pages) == 1, f"{name}: expected one WebPage or CollectionPage")
        for node in structured_pages:
            require(node.get("url") == SITE + name, f"{name}: structured URL mismatch")
            about = node.get("about", [])
            about = about if isinstance(about, list) else [about]
            require(any(item.get("@id") == "https://arxiv.org/abs/2609.36012#article" for item in about), f"{name}: survey attribution missing in structured data")
        require(not page.meta.get("citation_title"), f"{name}: guide must not have its own paper citation metadata")
        if name == "topics.html":
            continue
        require("topics.html" in graph[name], f"{name}: research directory link missing")
        require(len(page.visible.split()) >= 450, f"{name}: substantive topic discussion is missing")
        require(page.tags["table"] > 0, f"{name}: comparison table missing")
        section_links, study_links = set(), set()
        for tag, _, url in page.links:
            if tag != "a":
                continue
            parts = urlsplit(url)
            if parts.path == "read.html" and parts.fragment.startswith(("sec", "tab:", "app:")):
                section_links.add(parts.fragment)
            if (parts.path == "read.html" and parts.fragment in expected_refs) or url in known_source_urls:
                study_links.add(url)
        require(len(section_links) >= 2, f"{name}: needs specific survey section or table links")
        require(len(study_links) >= 2, f"{name}: needs identifiable original studies")
    metrics.update(research_topics=len(TOPIC_PAGES), reachable_pages=len(reachable))

    if source and (source / "robot-icl-survey.tex").is_file():
        sources = manuscript_sources(source)
        combined = "\n".join(sources.values())
        labels = set(re.findall(r"\\label\{((?:sec|app|fig|tab):[^}]+)\}", combined))
        missing = labels - set(reader.ids)
        require(not missing, f"read.html loses manuscript labels: {sorted(missing)[:30]}")
        headings = re.findall(r"\\(?:sub)*section\*?\s*\{([^{}]+)\}", combined)
        readtext = comparable(reader.visible)
        missing_headings = [heading for heading in headings if comparable(heading) not in readtext]
        require(not missing_headings, f"read.html loses section headings: {missing_headings[:15]}")
        expected_tables = len(re.findall(r"\\begin\{(?:table\*?|longtable)\}", combined))
        require(reader.tags["table"] >= expected_tables, f"read.html has {reader.tags['table']} tables; source has at least {expected_tables}")
        # Long plain-language spans are independently extracted from the source;
        # metadata/reference counts alone cannot prove that paragraphs survived.
        sentinels = []
        for path, tex in sources.items():
            if path.parent.name != "sections":
                continue
            candidates = re.findall(r"(?<![A-Za-z\\])(?:[A-Za-z][A-Za-z,'’\-]*[ \n]+){11}[A-Za-z][A-Za-z,'’\-]*", tex)
            sentinels.extend((path.name, candidate) for candidate in candidates)
        absent = [(name, plain(sentence)) for name, sentence in sentinels if comparable(sentence) not in readtext]
        require(not absent, f"read.html loses source prose spans ({len(absent)}): {absent[:8]}")
        metrics.update(source_input_files=len(sources), source_labels=len(labels), source_headings=len(headings), prose_sentinels=len(sentinels))
    else:
        notes.append("Accepted LaTeX source unavailable; skipped independent source label/heading/prose checks.")
    metrics.update(pages=len(pages), html_bytes=reader.path.stat().st_size, static_words=len(reader.visible.split()), references=len(actual_refs), checked_reference_titles=len(plain_titles), native_tables=reader.tags["table"], mathml_nodes=reader.tags["math"], images=len(reader.images), checked_links=sum(len(p.links) for p in pages.values()))
    return errors, notes, metrics


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT.parent / "source")
    parser.add_argument("--json", type=Path, help="Optional validation report path")
    args = parser.parse_args()
    errors, notes, metrics = validate(args.source.resolve())
    report = {"passed": not errors, "errors": errors, "notes": notes, "metrics": metrics}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
