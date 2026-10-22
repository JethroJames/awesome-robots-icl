#!/usr/bin/env python3
"""Check the published manuscript bundle and its catalogue/website references."""
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
import hashlib, json, re, zipfile

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'docs/assets'
release = json.loads((ASSETS / 'manuscript-release.json').read_text())
for name, expected in release['files'].items():
    data = (ASSETS / name).read_bytes()
    assert len(data) == expected['bytes'], name
    assert hashlib.sha256(data).hexdigest() == expected['sha256'], name

with zipfile.ZipFile(ASSETS / 'supplement-s1.zip') as z:
    assert z.testzip() is None
    refs = json.loads(z.read('Supplement-S1/references.json'))
    summary = json.loads(z.read('Supplement-S1/summary.json'))
    methods = json.loads(z.read('Supplement-S1/corpus.json'))
    for line in z.read('Supplement-S1/checksums.sha256').decode().splitlines():
        digest, name = line.split('  ', 1)
        assert hashlib.sha256(z.read('Supplement-S1/' + name)).hexdigest() == digest, name
assert len(refs) == len({r['key'] for r in refs}) == release['references']
assert {r['number'] for r in refs} == set(range(1, len(refs) + 1))
assert len(methods) == summary['method_references'] == release['method_references']
assert Counter(r['method_family'] for r in methods) == release['family_counts']
assert Counter(r['year'] for r in refs) == {r['year']: r['works'] for r in summary['annual']}
assert round(sum(r['year'] >= 2024 for r in refs) / len(refs) * 100, 1) == release['recent_share_percent']
assert sum(r['year'] == 2026 for r in refs) == release['first_public_2026']
assert summary['as_of'] == release['literature_cutoff']
with zipfile.ZipFile(ASSETS / 'figure9-editable.zip') as z:
    assert z.testzip() is None
    chart = json.loads(z.read('data-audit.json'))
    assert chart['references'] == release['references']
    assert chart['method_references'] == release['method_references']
    assert chart['as_of'] == release['literature_cutoff']
    assert chart['annual'] == summary['display_annual']
    assert {r['family']: r['count'] for r in chart['sectors']} == release['family_counts']
    assert z.read('figure9.png') == (ASSETS / 'figure9.png').read_bytes()
    assert z.read('figure9.svg') == (ASSETS / 'figure9.svg').read_bytes()

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.authors = []; self.links = []
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if tag == 'meta' and a.get('name') == 'citation_author': self.authors.append(a['content'])
        if tag == 'a' and 'href' in a: self.links.append(a['href'])

pages = []
for filename in ['index.html', 'paper.html']:
    text = (ROOT / 'docs' / filename).read_text()
    p = Page(); p.feed(text); pages.append(p)
    assert len(p.authors) == release['authors']
    graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)[1])
    article = next(n for n in graph['@graph'] if n['@type'] == 'ScholarlyArticle')
    assert article['dateModified'] == release['author_revision_date']
    assert article['numberOfPages'] == release['pages']
    for link in p.links:
        if link.startswith('assets/robot-icl-survey.pdf'):
            assert '?v=' + release['author_revision_date'].replace('-', '') in link
        if link.startswith('assets/'):
            assert (ROOT / 'docs' / link.split('?')[0].split('#')[0]).is_file(), link
assert pages[0].authors == pages[1].authors
assert (ROOT / 'citation.bib').read_bytes() == (ROOT / 'docs/citation.bib').read_bytes()

pattern = r'<!-- paper:([^ ]+) -->'
category_ids = set()
category_rows = set()
for file in (ROOT / 'papers').glob('*.md'):
    if file.name.endswith('.zh-CN.md'): continue
    ids = set(re.findall(pattern, file.read_text()))
    translated = file.with_name(file.stem + '.zh-CN.md')
    assert ids == set(re.findall(pattern, translated.read_text())), file.name
    rows = {line for line in file.read_text().splitlines() if '<!-- paper:' in line}
    assert rows == {line for line in translated.read_text().splitlines() if '<!-- paper:' in line}, file.name
    category_rows.update(rows)
    category_ids.update(ids)
assert len(category_ids) == release['catalogue_works']
for name in ['README.md', 'README_zh-CN.md']:
    text = (ROOT / name).read_text()
    assert set(re.findall(pattern, text)) == category_ids, name
    assert {line for line in text.splitlines() if '<!-- paper:' in line} == category_rows, name
    assert str(release['catalogue_works']) in text
    assert release['author_revision_date'] in text
    assert str(release['references']) in text

# Legacy catalogue aliases are matched by original-source identity as well as key.
catalogue = '\n'.join(category_rows)
for ref in refs:
    arxiv_id = re.search(r'\d{4}\.\d{4,5}', ref['source_url'])
    assert (ref['key'] in category_ids
            or (arxiv_id and arxiv_id[0] in catalogue)
            or ref['source_url'].rstrip('/') in catalogue), ('Missing manuscript reference', ref['key'])
print(f"Verified {release['pages']} pages / {release['references']} references / {release['authors']} authors; {len(category_ids)} catalogue entries; PDF, figures, supplement, bilingual mirrors and web metadata agree.")
