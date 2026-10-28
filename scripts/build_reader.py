#!/usr/bin/env python3
"""Build the complete static HTML survey from the accepted LaTeX source.

Requires make4ht (TeX Live), lxml and pypdfium2; the latter two are included in
the Codex desktop Python runtime. No browser-side JavaScript or MathJax is used.
Example: python3 scripts/build_reader.py --source ../source --work-dir /tmp/robot-icl-reader
The original source and accepted PDF are never modified.
"""
import argparse
import hashlib
import html as escaped
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from lxml import etree, html
import pypdfium2 as pdfium

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ASSETS = DOCS / "assets/manuscript"
SITE = "https://jethrojames.github.io/awesome-robots-icl/"
TITLE = "In-Context Learning for Robots: Methods and Applications"
SHORTCUTS = {
    "sec:intro": "sec-introduction", "sec:foundations": "sec-foundations",
    "sec:methods": "sec-methods", "sec:data": "sec-data",
    "sec:recovery": "sec-landscape", "sec:applications": "sec-applications",
    "sec:evaluation": "sec-evaluation", "sec:discussion": "sec-discussion",
    "sec:conclusion": "sec-conclusion", "app:study-index": "sec-reference-index",
    "app:comparisons": "sec-comparisons", "app:related-surveys": "sec-related-surveys",
}
PREAMBLE = r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[table]{xcolor}
\usepackage{graphicx,array,tabularx,longtable,booktabs,multirow}
\usepackage{amsmath,amssymb,bm,textcomp,needspace}
\usepackage[numbers,sort&compress]{natbib}
\usepackage{hyperref}
\definecolor{panel}{HTML}{ECECEC}
\definecolor{takehead}{HTML}{E7E7E7}
\definecolor{ink}{HTML}{171717}
\newcommand{\FloatBarrier}{}
\newcommand{\surveytable}{\small}
\newcommand{\surveyanchor}[1]{\par\phantomsection\label{#1}}
\newcommand{\tablegroup}[2]{\multicolumn{#1}{l}{\textbf{#2}}\\}
\newcommand{\surveybiburl}[1]{\url{#1}}
\newcommand{\takepoint}{\par\noindent\textbullet\ }
\newenvironment{takeaway}{\begin{quote}\textbf{Takeaways}\par}{\end{quote}}
\newcommand{\promptvideo}{demonstration video}
\newcommand{\yes}{\checkmark}\newcommand{\no}{\times}\newcommand{\unk}{?}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\newcolumntype{Z}{>{\centering\arraybackslash}X}
\begin{document}
"""


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def plain(element):
    return " ".join(element.text_content().split())


def prepare(source, work):
    for directory in ("sections", "tables", "generated"):
        (work / directory).mkdir(parents=True, exist_ok=True)
        for path in (source / directory).glob("*.tex"):
            shutil.copy2(path, work / directory / path.name)
    main = (source / "robot-icl-survey.tex").read_text()
    abstract = re.search(r"\\abstract\{\n(.*?)\n\}", main, re.S)[1]
    cover = re.search(r"\\caption\{(.*?)\}\\label\{fig:cover\}", main, re.S)[1]
    body = main[main.index(r"\input{sections/01-introduction}"):]
    body = re.sub(r"\\bibliography\{[^}]+\}", lambda _: r"\input{reader.bbl}", body)
    cover_tex = (r"\begin{figure}\includegraphics[width=\linewidth]{figures/cover-hero.pdf}"
                 + r"\caption{" + cover + r"}\label{fig:cover}\end{figure}" + "\n")
    (work / "reader.tex").write_text(PREAMBLE + r"\begin{abstract}" + abstract
                                    + r"\end{abstract}" + "\n" + cover_tex + body)
    shutil.copy2(source / "robot-icl-survey.bbl", work / "reader.bbl")
    (work / "figures").mkdir(exist_ok=True)
    # The original overlay contains only invisible PDF link rectangles; all
    # visible text is already in this figure. Retain the original diagram.
    (work / "figures/roadmap-citation-overlay.tex").write_text(
        r"\includegraphics[width=\linewidth]{figures/robot-icl-roadmap.pdf}" + "\n")
    texfiles = [work / "reader.tex", *work.glob("sections/*.tex"),
                *work.glob("tables/*.tex"), work / "figures/roadmap-citation-overlay.tex"]
    figure_paths = set()
    for path in texfiles:
        text = path.read_text()
        figure_paths.update(re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+\.pdf)\}", text))
        text = re.sub(r"(\\includegraphics(?:\[[^\]]*\])?\{[^}]+)\.pdf\}", r"\1.png}", text)
        path.write_text(text)
    for name in sorted(figure_paths):
        pdf = pdfium.PdfDocument(str(source / name))
        page = pdf[0]
        bitmap = page.render(scale=2)
        image = bitmap.to_pil()
        target = (work / name).with_suffix(".png")
        image.save(target)
        image.close(); bitmap.close(); page.close(); pdf.close()
    (work / "reader.cfg").write_text("\\Preamble{xhtml,mathml}\n\\begin{document}\n\\EndPreamble\n")
    result = subprocess.run(["make4ht", "-c", "reader.cfg", "-B", "build", "reader.tex", "mathml"],
                            cwd=work, capture_output=True, text=True)
    (work / "conversion.log").write_text(result.stdout + result.stderr)
    if result.returncode:
        raise SystemExit(f"make4ht failed; see {work / 'conversion.log'}")
    log = (work / "build/reader.log").read_text()
    if re.search(r"^!|Citation .* undefined|Reference .* undefined", log, re.M):
        raise SystemExit(f"Unresolved LaTeX errors or citations; see {work / 'build/reader.log'}")


def add_alias(element, name):
    # An HTML span inside MathML ends the browser's foreign-content parsing.
    # Keep aliases outside the entire formula, including its equation table.
    math = next((node for node in element.iterancestors() if node.tag == "math"), None)
    if math is not None:
        element = next((node for node in math.iterancestors()
                        if node.tag == "table" and node.get("class") == "equation"), math)
    alias = etree.Element("span", id=name, attrib={"class": "source-anchor", "aria-hidden": "true"})
    if element.getparent() is not None:
        element.addprevious(alias)


def validate_mathml(body):
    """Reject foreign markup that would break native browser MathML parsing."""
    namespace = "http://www.w3.org/1998/Math/MathML"
    allowed = {"math", "mrow", "mi", "mn", "mo", "mtext", "mspace", "ms",
               "mfrac", "msqrt", "mroot", "mstyle", "merror", "mpadded",
               "mphantom", "mfenced", "menclose", "msub", "msup", "msubsup",
               "munder", "mover", "munderover", "mmultiscripts", "mprescripts",
               "none", "mtable", "mtr", "mlabeledtr", "mtd", "maction",
               "semantics", "annotation"}
    for formula in body.xpath(".//math"):
        # Parsing each serialized formula also catches accidental namespace
        # resets; the tag allowlist catches HTML elements such as span even if
        # an XML parser would incorrectly inherit the MathML namespace for them.
        parsed = etree.fromstring(etree.tostring(formula, with_tail=False))
        for node in parsed.iter():
            if not isinstance(node.tag, str):
                continue
            name = etree.QName(node)
            if name.namespace != namespace or name.localname not in allowed:
                raise ValueError(f"Non-MathML element inside a formula: {node.tag}")


def assemble(source, work):
    tree = html.fromstring((work / "build/reader.html").read_text())
    body = tree.find("body")
    aux = (work / "build/reader.aux").read_text()
    label_map = dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{\\rEfLiNK\{([^}]+)\}", aux))
    by_id = {node.get("id"): node for node in body.xpath(".//*[@id]")}
    missed = []
    for label, target in label_map.items():
        if target in by_id:
            add_alias(by_id[target], label)
            if label in SHORTCUTS:
                add_alias(by_id[target], SHORTCUTS[label])
        elif label.startswith(("sec:", "app:", "fig:", "tab:", "eq:")):
            missed.append((label, target))
    if missed:
        raise SystemExit(f"Unmapped manuscript labels: {missed}")
    for node in body.xpath(".//*[@id and starts-with(@id,'X')]"):
        key = node.get("id")[1:]
        add_alias(node, "ref-" + key)
    for link in body.xpath(".//a[@href]"):
        href = link.get("href").replace("reader.html#", "#")
        if href.startswith("#X"):
            href = "#ref-" + href[2:]
        link.set("href", href)
    for title in body.xpath(".//h3|.//h4|.//h5"):
        cls = title.get("class", "")
        if cls in ("sectionHead", "likesectionHead", "abstracttitle"):
            title.tag = "h2"
        elif cls == "subsectionHead":
            title.tag = "h3"
        if cls == "likesectionHead" and plain(title) == "References":
            add_alias(title, "sec-references")
    for para in body.xpath(".//span[contains(@class,'paragraphHead')]"):
        para.tag = "strong"
    ASSETS.mkdir(parents=True, exist_ok=True)
    for image in body.xpath(".//img"):
        local = work / image.get("src")
        if not local.is_file():
            raise SystemExit(f"Missing figure: {local}")
        target = ASSETS / local.name
        shutil.copy2(local, target)
        image.set("src", "assets/manuscript/" + target.name)
        image.set("loading", "lazy"); image.set("decoding", "async")
        figure = next((x for x in image.iterancestors() if x.tag == "figure"), None)
        caption = figure.find("figcaption") if figure is not None else None
        image.set("alt", plain(caption) if caption is not None else local.stem.replace("-", " "))
        image.attrib.pop("width", None); image.attrib.pop("height", None)
    for table in body.xpath(".//table"):
        is_equation = table.get("class") == "equation"
        wrapper = etree.Element("div", attrib={"class": "math-scroll" if is_equation else "table-scroll",
                                                "role": "region", "tabindex": "0"})
        caption = table.find("caption")
        if caption is None:
            figure = next((x for x in table.iterancestors() if x.tag == "figure"), None)
            caption = figure.find("figcaption") if figure is not None else None
        label = plain(caption) if caption is not None else ("Mathematical equation" if is_equation else "Survey comparison table")
        wrapper.set("aria-label", label)
        table.addprevious(wrapper)
        wrapper.append(table)
        if not is_equation:
            for row in table.xpath("./tr|./thead/tr|./tbody/tr"):
                cells = row.xpath("./td")
                if cells and all(cell.xpath(".//span[starts-with(@class,'ecbx')]") for cell in cells):
                    for cell in cells:
                        cell.tag = "th"; cell.set("scope", "col")
    for node in body.iter():
        if not isinstance(node.tag, str):
            continue
        if node.get("style"):
            # TeX's fixed-width/nowrap layout is replaced by responsive CSS.
            node.set("style", re.sub(r"(?:white-space|width|height):[^;]+;?", "", node.get("style")))
    for comment in body.xpath(".//comment()"):
        comment.getparent().remove(comment)

    authors_src = (source / "frontmatter-authors.tex").read_text()
    authors = re.findall(r"\\mbox\{([^{}]+)\\textsuperscript\{([^}]+)\}\}", authors_src)
    if len(authors) != 39:
        raise SystemExit(f"Expected 39 authors, found {len(authors)}")
    affiliation_matches = re.findall(r"\\mbox\{\\textsuperscript\{(\d+)\}([^{}]+)\}", authors_src)
    author_html = ", ".join(escaped.escape(name) + "<sup>" + aff + "</sup>" for name, aff in authors)
    affiliation_html = " · ".join("<sup>" + n + "</sup>" + escaped.escape(name) for n, name in affiliation_matches)
    toc = []
    for heading in body.xpath(".//h2[@class='sectionHead' or @class='likesectionHead']"):
        toc.append(f'<a href="#{heading.get("id")}">{escaped.escape(plain(heading))}</a>')
    content = "".join(html.tostring(child, encoding="unicode", method="html") for child in body)
    # Retain all generated math and character semantics; style only the reading view.
    metadata = json.loads((DOCS / "assets/manuscript-release.json").read_text())
    canonical = SITE + "read.html"
    author_meta = "\n".join(f'<meta name="citation_author" content="{escaped.escape(name, quote=True)}">' for name, _ in authors)
    abstract = " ".join(re.search(r"\\abstract\{\n(.*?)\n\}", (source / "robot-icl-survey.tex").read_text(), re.S)[1].split())
    graph = {"@context": "https://schema.org", "@type": "ScholarlyArticle", "@id": "https://arxiv.org/abs/2609.36012#article",
             "headline": TITLE, "url": canonical, "abstract": abstract,
             "author": [{"@type": "Person", "name": name} for name, _ in authors],
             "datePublished": "2026-09-28", "dateModified": "2026-10-22", "version": "Author revision 2026-10-22",
             "identifier": "arXiv:2609.36012", "isAccessibleForFree": True, "inLanguage": "en"}
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLE} — Full text</title>
<meta name="description" content="Read the complete Robot ICL Survey: four method families, training, transfer, evaluation, 26 figures, 25 tables and 548 references.">
<meta name="robots" content="index, follow, max-image-preview:large"><link rel="canonical" href="{canonical}">
<meta name="citation_title" content="{TITLE}">{author_meta}
<meta name="citation_publication_date" content="2026/09/28"><meta name="citation_arxiv_id" content="2609.36012">
<meta name="citation_pdf_url" content="{SITE}assets/robot-icl-survey.pdf"><meta name="citation_language" content="en">
<meta name="citation_abstract" content="{escaped.escape(abstract, quote=True)}">
<link rel="alternate" type="application/pdf" href="assets/robot-icl-survey.pdf?v=20261022" title="Accepted PDF">
<link rel="alternate" type="application/x-bibtex" href="citation.bib" title="BibTeX">
<link rel="stylesheet" href="assets/reader.css"><link rel="stylesheet" href="assets/full-paper.css">
<script type="application/ld+json">{json.dumps(graph, ensure_ascii=False)}</script>
</head><body class="reader-page full-paper">
<a class="skip-link" href="#main-content">Skip to full text</a>
<header class="reader-header"><div class="reader-shell"><a class="reader-brand" href="index.html">Robot ICL Survey</a><nav class="reader-nav" aria-label="Main navigation"><a href="read.html" aria-current="page">Read the survey</a><a href="topics.html">Topics</a><a href="taxonomy.html">Taxonomy</a><a href="evaluation.html">Evaluation</a><a href="paper.html">Paper &amp; citation</a></nav></div></header>
<main class="reader-shell" id="main-content">
<header class="reader-hero"><h1>{TITLE}</h1>
<div class="reader-actions"><a class="reader-button" href="assets/robot-icl-survey.pdf?v=20261022">Download PDF</a><a class="reader-button" href="assets/supplement-s1.zip">Supplement S1</a><a class="reader-button" href="paper.html#record-citation-title">Cite this survey</a></div>
<details class="manuscript-credits"><summary>Authors and affiliations</summary><p class="manuscript-authors">{author_html}</p><p class="manuscript-affiliations">{affiliation_html}</p><p><sup>*</sup> Corresponding authors.</p></details>
</header>
<div class="reader-layout"><aside class="reader-toc" aria-label="Table of contents"><h2>Contents</h2>{''.join(toc)}<a href="assets/supplement-s1.zip">Supplement S1 ↗</a></aside>
<article class="reader-content manuscript-body" aria-label="Full survey">{content}</article></div>
</main><footer class="reader-footer"><div class="reader-shell"><p>Robot ICL Survey</p><a href="paper.html">Paper &amp; citation</a></div></footer>
</body></html>'''
    page = "\n".join(line.rstrip(" \t") for line in page.split("\n"))
    final = html.fromstring(page)
    validate_mathml(final)
    ids = final.xpath("//*[@id]/@id")
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate anchors in final reader")
    broken = [link for link in final.xpath("//a/@href") if link.startswith("#") and link[1:] not in ids]
    if broken:
        raise SystemExit(f"Broken internal links: {broken[:12]}")
    references = json.loads((source / "Supplement-S1/references.json").read_text())
    expected = {"ref-" + x["key"] for x in references}
    actual = {key for key in ids if key.startswith("ref-")}
    if actual != expected:
        raise SystemExit("Reference coverage differs from accepted inventory")
    (DOCS / "read.html").write_text(page)
    source_paths = [source / "robot-icl-survey.tex", source / "frontmatter-authors.tex", source / "robot-icl-survey.bbl",
                    *source.glob("sections/*.tex"), *source.glob("tables/*.tex"), *source.glob("generated/*.tex")]
    source_paths += [source / "figures" / Path(x).with_suffix(".pdf").name for x in final.xpath("//article//img/@src")]
    report = {"author_revision_date": "2026-10-22", "source_pdf_sha256": metadata["files"]["robot-icl-survey.pdf"]["sha256"],
              "html_bytes": (DOCS / "read.html").stat().st_size, "authors": len(authors), "references": len(actual),
              "figures": len(final.xpath("//article//img")), "data_tables": len(final.xpath("//article//table[@class='tabular' or @class='longtable']")),
              "numbered_equations": len(final.xpath("//article//table[@class='equation']")),
              "mathml_expressions": len(final.xpath("//math")), "manuscript_labels": len(label_map),
              "text_words": len(plain(final).split()), "broken_internal_links": broken,
              "conversion": "TeX4ht / make4ht; native MathML; figures rendered from original PDFs at 144 dpi",
              "layout_transformations": ["Print-only preamble replaced with HTML-compatible packages and equivalent survey macros.",
                                         "Invisible roadmap PDF hyperlink rectangles omitted; visible roadmap retained.",
                                         "Original numeric citation order, labels and table/figure/equation numbering retained."],
              "source_files": {str(p.relative_to(source)): digest(p) for p in sorted(set(source_paths))}}
    (ASSETS / "coverage.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in {"source_files", "layout_transformations"}}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT.parent / "source")
    parser.add_argument("--work-dir", type=Path)
    parser.add_argument("--reuse-tex4ht", action="store_true", help="Reuse an existing complete conversion in --work-dir (development only)")
    args = parser.parse_args()
    source = args.source.resolve()
    if args.work_dir:
        work = args.work_dir.resolve(); work.mkdir(parents=True, exist_ok=True)
        if not args.reuse_tex4ht:
            prepare(source, work)
        assemble(source, work)
    else:
        with tempfile.TemporaryDirectory(prefix="robot-icl-reader-") as directory:
            work = Path(directory)
            prepare(source, work)
            assemble(source, work)


if __name__ == "__main__":
    main()
