# Contributing

Corrections, carefully selected papers and useful data releases are welcome.

## Add or correct a paper

Edit the appropriate section in `README.md` or `README_zh-CN.md`, or open an issue with the source and proposed change. **No JSON, build step or generated catalog is required.** Maintainers can help with the other language.

Use the same short format as neighboring entries:

```markdown
- **[First preprint year · Venue] Exact paper title** — [Paper](canonical-url) · [Code](official-code-url)
  `context-tag` `method-tag` · One sentence explaining the contribution and a material caveat.
```

Use only links that exist. Omit unavailable resources; label a placeholder repository **Release plan**, not **Code**. Label a benchmark release **Benchmark** unless it actually includes the claimed policy implementation.

## Selection and evidence

- Focus on deployment-time demonstrations or interaction history for robot manipulation. Include broader control, historical and adjacent work only with a clear reason.
- Use the published title when available; keep a method acronym in the description if it is not part of that title.
- The first year is the earliest preprint year, or publication year if no preprint is available; a later conference year is recorded separately. Check proceedings, paper metadata or an author project page for the venue. Use `venue unverified` when unresolved.
- State what the context contains: human `prompt_video`, robot demonstration, instrumented sensorimotor demonstration, structured description or interaction history.
- Do not equate one-shot learning with zero-gradient ICL. Name test-time parameter, fast-weight or memory optimization when present.
- Keep input type, adaptation mechanism and output pathway separate. A world-action model can be used with either ICL or TTT; retrieval is not exclusive to one category.
- Separate author-reported results from independently reproduced evidence. Do not rank success rates from incompatible tasks, splits or retry budgets.
- Do not infer hidden company architectures, parameter counts or training recipes.
- Prefer the paper and official resources, not an awesome list as the sole evidence. Existing lists are discovery aids and are acknowledged in Related lists.

## Data and benchmarks

Name the exact release. Distinguish native task correspondence from frame synchronization, pseudo-pairs, retargeting and generated videos. A measured robot pose, a commanded action and an estimated human-hand pose are not interchangeable.

A dataset with robot RGB/actions is not automatically a human-video ICL dataset. Conversely, inspect a release before declaring that it has no human demonstrations. Check both the human side and the robot trajectory fields.

Link to datasets rather than copying them. Respect access restrictions, privacy and version-specific licenses.

## Optional maintainer check

```bash
python3 scripts/check_readme.py
```

This checks local links, duplicate paper entries and English/Chinese consistency. It does **not** verify external availability, factual correctness, licenses or reproducibility. CI runs it automatically; contributors do not need a local Python setup.

## 中文说明

直接编辑任一语言 README 或提交带一手来源的 issue 即可。另一语言可由维护者同步。添加论文时优先核对正式标题、会议、上下文模态、测试时是否更新参数和实际发布内容；不要仅凭 GitHub 链接就标记“完整开源可复现”。
