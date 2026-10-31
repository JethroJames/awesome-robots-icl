#!/usr/bin/env python3
"""Keep citation exports and existing scholarly records aligned with paper-metadata.json."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def synchronize():
    metadata = json.loads((DOCS / "assets/paper-metadata.json").read_text())
    abstract = metadata["abstract"]
    for name in ["index.html", "paper.html"]:
        path = DOCS / name
        page = path.read_text()
        page, count = re.subn(
            r'<meta name="citation_abstract" content="[^"]*">',
            lambda _: '<meta name="citation_abstract" content="' + html.escape(abstract, quote=True) + '">',
            page,
        )
        assert count == 1, name
        match = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', page, re.S)
        graph = json.loads(match[2])
        article = next(item for item in graph["@graph"] if item["@type"] == "ScholarlyArticle")
        article["abstract"] = abstract
        article["name"] = metadata["title"]
        article["headline"] = metadata["title"]
        article["datePublished"] = metadata["publication_date"]
        article["dateModified"] = metadata["author_revision_date"]
        article["version"] = "Author revision " + metadata["author_revision_date"]
        page = page[:match.start(2)] + json.dumps(graph, ensure_ascii=False, indent=2) + page[match.end(2):]
        css_class = "abstract-text" if name == "index.html" else "record-abstract-text"
        page, count = re.subn(
            r'(<p class="' + css_class + r'">).*?(</p>)',
            lambda m: m[1] + html.escape(abstract) + m[2], page, flags=re.S,
        )
        assert count == 1, name
        path.write_text(page)
    path = DOCS / "citation.json"
    csl = json.loads(path.read_text())
    csl[0]["abstract"] = abstract
    csl[0]["title"] = metadata["title"]
    csl[0]["author"] = metadata["authors"]
    csl[0]["note"] = f"arXiv:2609.36012; author revision {metadata['author_revision_date']}; arXiv record v1"
    path.write_text(json.dumps(csl, ensure_ascii=False, indent=2) + "\n")
    path = DOCS / "citation.ris"
    ris, count = re.subn(r"^AB  - .*", lambda _: "AB  - " + abstract, path.read_text(), flags=re.M)
    assert count == 1
    ris = re.sub(r"^N1  - .*", f"N1  - arXiv:2609.36012; {metadata['pages']} pages; author revision {metadata['author_revision_date']}; arXiv record v1", ris, flags=re.M)
    path.write_text(ris)
    print("Synchronized the accepted abstract across HTML, JSON-LD, CSL JSON and RIS.")


if __name__ == "__main__":
    synchronize()
