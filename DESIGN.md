# Design

## Source of truth
- Status: Active. Last refreshed: 2026-10-29.
- Surfaces: project homepage and paper record; taxonomy, evaluation and full-text reading pages; research directory and six related-topic guides.
- Evidence: docs/index.html, docs/paper.html, docs/assets/discovery.css, the accepted 2026-10-22 manuscript in ../source, and docs/assets/manuscript-release.json.

## Brand
- Scholarly, calm, precise. Identity: Robot ICL Survey; full title: In-Context Learning for Robots: Methods and Applications; arXiv:2609.36012.
- Trust comes from explicit sources, visible version information and accurate attribution. Avoid promotional claims or inflated citation instructions.

## Product goals
- Help researchers read the full survey and use its taxonomy and evaluation framework with evidence links.
- Preserve the accepted PDF and source, 548 manuscript references, 351 methods/comparisons, 39 authors, and the separate 582-entry catalogue scope.
- No arXiv submission, no v4 candidate figures, no change to academic claims. Successful delivery has readable static HTML, working references and verified mobile/desktop layouts.

## Personas and jobs
- Robotics researchers comparing mechanisms, planning evaluation and drafting related work; readers and search tools locating the supporting section.

## Information architecture
- Home; Read the survey (read.html); Taxonomy (taxonomy.html); Evaluation (evaluation.html); Paper & citation (paper.html); Supplement S1.
- Topics (topics.html) connects VLA models, learning from demonstration, robot world models, embodied-agent memory, robot self-improvement and vision-language navigation to specific survey evidence.
- Topic pages: question, concise answer, substantive comparison, assumptions/limits, supporting manuscript locations, citation.
- The full paper remains one HTML document with stable section/figure/table/reference anchors.

## Design principles
- User correction, 2026-10-28: enhance the existing website incrementally. Preserve its recognizable appearance, original structure, black-and-white palette, existing imagery, heading alignment, navigation and content order.
- References to Apple or a premium appearance mean restrained polish within this existing design. They do not authorize a new centered hero, blue pill buttons, new illustration cards, relocated author lists or a replacement navigation system.
- Restore the pre-redesign first-batch implementation; keep the abstract, Supplement, identity/version, topic pages and full HTML improvements. Current visual refinements are limited to small type, line-height and spacing adjustments.
- Keep key content visible as semantic HTML; use progressive enhancement only for optional convenience.
- Separate the survey's synthesis from results attributed to original studies.
- Keep the homepage concise and route deeper reading to dedicated pages.
- Topic guides answer distinct research questions using substantive comparisons and identifiable studies. Link to the survey's synthesis and original sources; do not create keyword variants or imply new experiments.

## Visual language
- Preserve warm white #f8f8f6, ink #161616, muted gray #656565, light rules #d5d5d2.
- Use existing system sans stack, readable 17–19px prose, restrained headings, generous line height and ~75-character text measures.
- Editorial rows and tables rather than a dashboard; no decorative illustration or new fonts.

## Components
- Reuse existing links, citation controls and record styles. New reader.css owns reading-layout, table-overflow, evidence and full-text styles.
- Keep topic navigation consistent. Paper identity and version details are collected on the paper record, linked from every reading page.

## Accessibility
- Aim for WCAG AA: semantic headings, labelled tables, descriptive links, visible keyboard focus, skip links, adequate contrast.
- No essential content gated by JavaScript, hover or animation. Figures have useful alt text and captions; equations retain readable semantics or text equivalents.

## Responsive behavior
- Single-column small-screen layout at 800px; sidebar TOC becomes in-flow navigation.
- Wide tables scroll inside labelled regions, never force whole-page horizontal scrolling.

## Interaction states
- Static content has no loading dependency. Copy-citation success/failure uses the existing status text.
- Native links and readable fallback content work without JavaScript; optional controls must not obscure content.

## Content voice
- English public content; explicit definitions, limits and provenance. Avoid calling every supporting work a core ICL method.
- User refinement, 2026-10-28: remove decorative eyebrow labels, repeated counts and version strips, generic reading reassurance and redundant citation advice. Keep research qualifications and source links that carry meaning.
- The paper record distinguishes Author revision 22 October 2026 from arXiv v1. Citation metadata retains the paper dates; website updates do not create a new paper version.
- Topic guides use WebPage metadata and point to the same survey identity. The directory is a CollectionPage; guides are not separate scholarly publications.

## Implementation constraints
- Buildless static website; no new runtime dependency or external font. Keep generated full text reproducible from the accepted source.
- Use existing Python/TeX/browser tooling. Validate reference coverage, anchors, citation abstracts, unchanged PDF hashes and responsive layouts.

## Open questions
- None. The user approved publication to the existing GitHub Pages site on 2026-10-28; arXiv submission remains on hold.
