# 研究阅读页维护与交接

更新日期：2026-10-28。发布目标为既有 GitHub Pages（`main` 分支的 `docs/`）；arXiv 继续暂不提交。

## 版式范围更正（2026-10-28）

用户明确要求在原网站基础上增强，保持熟悉的外观。本轮已恢复改版前的首页与阅读页结构、黑白基调、原图、标题对齐方式、导航、作者和版本位置，撤回居中大标题、蓝色胶囊按钮、示意卡片与大范围折叠内容的尝试。

摘要一致性、Supplement 入口、论文身份和版本、分类与评测专题页、完整 HTML 等首批增强全部保留。当前仅微调正文与比较表字号、行距及段落间距。后续设计以 `DESIGN.md` 的“渐进增强、保持原貌”约束为准。

本次进一步删除装饰性小标签、重复计数、版本条、阅读说明和重复的引用提示。版本信息集中在 `paper.html`，各页保留入口与机器可读论文元数据；摘要、完整论文正文和有意义的研究限定保持完整。

论文身份为 **In-Context Learning for Robots: Methods and Applications**，arXiv:2609.36012。网站提供 2026-10-22 作者修订稿；arXiv 记录仍为 v1，首次公开日期为 2026-09-28。专题页的 2026-10-27 更新日期不代表论文的新版本。

## 本轮修改

| 位置 | 内容 |
| --- | --- |
| `docs/index.html` | 统一摘要，新增全文、分类、评测和 Supplement S1 入口，明确版本状态 |
| `docs/paper.html` | 摘要、论文身份、版本、引用格式及资源入口集中呈现 |
| `docs/taxonomy.html` | 四类执行接口、混合系统分类、共享机制与参数更新边界 |
| `docs/evaluation.html` | 归因控制、迁移、保留经验、报告要求，以及有原始来源的研究实例 |
| `docs/read.html` | 完整正文、附录、548 条参考文献、26 张原图、25 张数据表和 21 个编号公式 |
| `docs/assets/paper-metadata.json` | 摘要、标题、作者顺序及版本信息的维护入口 |
| `docs/assets/reader.css` / `full-paper.css` | 专题页与全文阅读版样式，手机表格局部横向滚动 |
| `docs/assets/manuscript/` | 从原稿 PDF 图片生成的阅读版图像及 `coverage.json` 构建记录 |
| `docs/citation.json` / `citation.ris` | 与原稿一致的摘要及作者修订说明 |
| `docs/sitemap.xml` | 包含五个公开页面的 sitemap |

专题页是论文内容的阅读导引。分类框架与综合判断归于综述；算法、数据集和实验结果归于原始研究。548 条论文参考文献、351 条方法及比较条目、582 条网站目录条目的范围分别说明。

## 重建与验证

在本 `website/` 目录执行。基础检查只需要 Python 3；全文重建另外需要现有 TeX Live 的 `make4ht`、Python 的 `lxml` 和 `pypdfium2`。本机使用 Codex 已有的 Python 运行时，没有安装新依赖。

```sh
python3 scripts/sync_citation_metadata.py
python3 scripts/build_reader.py --source ../source
python3 scripts/check_manuscript_release.py
python3 scripts/check_research_pages.py
python3 scripts/reader-tests.py
python3 ../verify_package.py
git diff --check
```

完整 HTML 由 `scripts/build_reader.py` 生成，后续改动应修改源稿或转换脚本再重建，不直接手改 `read.html`。脚本在临时目录转换 LaTeX，不覆盖原稿和已验收 PDF。原图按 144 dpi 生成 PNG；仅省略路线图 PDF 中不可见的链接热点层。公式用原生 MathML，阅读不依赖 MathJax 或浏览器脚本。

原 LaTeX 标签保留为锚点，例如 `read.html#tab:methodological-taxonomy`；文献锚点为 `read.html#ref-<BibTeX key>`。公式锚点置于 MathML 容器外，构建检查和四项回归测试防止上下标退化成普通文本。

将 TeX Live 的可执行目录加入 `PATH`，并使用包含 `lxml` 和 `pypdfium2` 的 Python 环境。`verify_package.py` 是独立交接包中的验收脚本，仅在完整交接目录中可用。

摘要变更时先以验收源稿为准更新 `paper-metadata.json`，运行同步与全文重建，再执行验证。专题页文案与论文信息页的可见版本仍需人工同步；验证器会检查日期、标题、作者、摘要和链接，不能代替学术内容复核。

## 本地预览

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
```

浏览器打开 `http://127.0.0.1:8765/`；专题页路径分别为 `/taxonomy.html`、`/evaluation.html`、`/read.html`。全站是静态文件，发布仍沿用现有 GitHub Pages 的 `docs/` 目录。

## 验收与后续状态

- 本轮已验证五页本地链接、原始标签、正文覆盖、参考文献顺序及题名、摘要一致性、原稿和补充材料哈希；已检查桌面和手机显示。
- 浏览器检查发现并修复了独立公式中插入 HTML 锚点导致的上下标丢失。
- 原始交接包的 `manifest.json` 保留不改；`verify_package.py` 仍可验证 168 个原交付文件。旧的整包接收快照若包含网站文件，会因本轮有意修改而发生差异。
- 原稿 PDF、LaTeX 内容和补充材料没有改动。四类方法手绘实图 v4 尚未纳入，仍需从原交接说明中的独立路径取用。
- 用户已批准网站发布。后续更新需先完成上述验证，将网站改动提交并推送至 `main`，等待 GitHub Pages 构建成功，再核验五个公开页面及附件；不执行 arXiv 提交。
- 尚未验证搜索引擎收录或 AI 调研工具的实际引用变化；这些只能在公开部署后观察。
