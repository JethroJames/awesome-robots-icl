# Contributing

Open an issue with a primary source, or edit either README. Translation help is welcome.

- Keep entries short: method, year, one concrete contribution, official links.
- Put representative methods in the tables; use the folded list for other work.
- Check the context input and whether test-time gradients are used.
- Label resources accurately: code, benchmark, weights, data, or release plan.
- Use first-preprint years. Link method names to the paper; do not infer unpublished details.
- For datasets, distinguish robot actions from human-pose estimates and retargeted targets.

Checks run automatically. To run locally:

```bash
python3 scripts/check_readme.py
```

The check covers local links and bilingual consistency, not factual correctness.

中文：提交一手来源，说明要补充或更正什么即可。保持一篇一句；另一语言可由维护者同步。
