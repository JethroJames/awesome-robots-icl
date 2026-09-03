#!/usr/bin/env python3
"""Offline Markdown hygiene only; not a factual or external-link validator."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]*\]\(([^\s)]+)\)")
PAPER = re.compile(r"^(?:\| |- )\*\*\[([^\]\n]+)\]\((https://[^\s)]+)\)\*\* · (\d{4})([^\n]*)$", re.M)
ARXIV_BADGE = re.compile(r"\[!\[arXiv ([^\]]+)\]\((https://[^)]+)\)\]\((https://[^)]+)\)")


def prose(text: str) -> str:
    """Ignore fenced examples when extracting links or paper entries."""
    return re.sub(r"^```[^\n]*\n.*?^```[^\n]*(?:\n|$)", "", text, flags=re.M | re.S)


def anchors(text: str) -> set[str]:
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    used: Counter[str] = Counter()
    for title in re.findall(r"^#{1,6} (.+)$", prose(text), re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        suffix = f"-{used[slug]}" if used[slug] else ""
        result.add(slug + suffix)
        used[slug] += 1
    return result


def check(root: Path) -> list[str]:
    errors: list[str] = []
    documents = {p: p.read_text(encoding="utf-8") for p in root.rglob("*.md") if ".git" not in p.parts}
    for path, text in documents.items():
        where = str(path.relative_to(root))
        for target in LINK.findall(prose(text)):
            parsed = urlsplit(target)
            if parsed.scheme:
                if parsed.scheme != "https" or not parsed.netloc:
                    errors.append(f"{where}: expected HTTPS URL: {target}")
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not dest.is_relative_to(root.resolve()):
                errors.append(f"{where}: link leaves repository: {target}")
            elif not dest.exists():
                errors.append(f"{where}: missing local target: {target}")
            elif parsed.fragment and dest.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(documents.get(dest, dest.read_text(encoding="utf-8"))):
                    errors.append(f"{where}: missing anchor: {target}")
        if "GENERATED:CATALOG" in text or "scripts/render_catalog.py" in text:
            errors.append(f"{where}: stale generated-catalog reference")

    catalogs = []
    for filename in ("README.md", "README_zh-CN.md"):
        text = documents.get(root / filename, "")
        entries = PAPER.findall(text)
        if not entries:
            errors.append(f"{filename}: no paper entries in README")
        titles = [title.casefold() for title, _, _, _ in entries]
        for title, count in Counter(titles).items():
            if count > 1:
                errors.append(f"{filename}: duplicate paper: {title}")
        urls = [url for _, url, _, _ in entries]
        for url, count in Counter(urls).items():
            if count > 1:
                errors.append(f"{filename}: duplicate paper URL: {url}")
        for title, url, _, resources in entries:
            badges = ARXIV_BADGE.findall(resources)
            if url.startswith("https://arxiv.org/abs/") and len(badges) != 1:
                errors.append(f"{filename}: expected one arXiv badge for {title}")
            for identifier, image, target in badges:
                if (not re.fullmatch(r"\d{4}\.\d{4,5}", identifier)
                        or image != f"https://img.shields.io/badge/arXiv-{identifier}-b31b1b"
                        or target != f"https://arxiv.org/abs/{identifier}"):
                    errors.append(f"{filename}: inconsistent arXiv badge for {title}")
                if url.startswith("https://arxiv.org/abs/") and target != url:
                    errors.append(f"{filename}: arXiv badge differs from paper link for {title}")
        catalogs.append([(title, url, year, LINK.findall(resources))
                         for title, url, year, resources in entries])
    if catalogs[0] != catalogs[1]:
        errors.append("READMEs disagree on paper order, name, year or resource links")
    return errors


def main() -> int:
    errors = check(ROOT)
    if errors:
        print("README checks failed:\n" + "\n".join(f"- {item}" for item in errors))
        return 1
    count = len(PAPER.findall((ROOT / "README.md").read_text(encoding="utf-8")))
    print(f"Checked {count} bilingual paper entries and local Markdown links.")
    print("External availability, factual claims and reproducibility are NOT validated by this check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
