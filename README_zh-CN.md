# Robot In-Context Learning

**In-Context Learning for Robotics** — 机器人上下文学习的论文、数据与评测。

[English](README.md) · [论文](#papers) · [数据](#data) · [评测](#benchmarks) · [数据说明](notes/reproducibility.md)

<a id="papers"></a>

## 论文

年份按首次预印本标注。

### 从人类视频学习

| 工作 | 核心做法 | 资源 |
| --- | --- | --- |
| **[Zero-WAM](https://arxiv.org/abs/2608.26103)** · 2026<br>[![arXiv 2608.26103](https://img.shields.io/badge/arXiv-2608.26103-b31b1b)](https://arxiv.org/abs/2608.26103) | 人类 `prompt_video` → 机器人未来帧与动作。 | [项目](https://robbyant-research.github.io/Zero-WAM/) · [发布计划](https://github.com/robbyant-research/Zero-WAM) |
| **[HOST](https://arxiv.org/abs/2607.20033)** · 2026<br>[![arXiv 2607.20033](https://img.shields.io/badge/arXiv-2607.20033-b31b1b)](https://arxiv.org/abs/2607.20033) | 对齐任务进度，预测机器人未来，再解码动作。 | [代码](https://github.com/CGuangyan-BIT/HOST) · [权重](https://huggingface.co/Guangyan/HOST) |
| **[ViVLA](https://arxiv.org/abs/2512.07582)** · 2025<br>[![arXiv 2512.07582](https://img.shields.io/badge/arXiv-2512.07582-b31b1b)](https://arxiv.org/abs/2512.07582) | 用 expert–agent 配对数据训练视频条件动作预测。 | — |
| **[MimicDroid](https://arxiv.org/abs/2509.09769)** · 2025<br>[![arXiv 2509.09769](https://img.shields.io/badge/arXiv-2509.09769-b31b1b)](https://arxiv.org/abs/2509.09769) | 从 human play 挖掘配对，重定向手腕运动作为监督。 | [基准](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) · [数据](https://huggingface.co/datasets/Rutav/MimicDroidDataset) |
| **[RHyME](https://arxiv.org/abs/2409.06615)** · 2024<br>[![arXiv 2409.06615](https://img.shields.io/badge/arXiv-2409.06615-b31b1b)](https://arxiv.org/abs/2409.06615) | 为机器人轨迹检索、拼接示范片段。 | [代码](https://github.com/portal-cornell/rhyme) · [仿真数据](https://huggingface.co/datasets/prithwishdan/RHyME) |
| **[Vid2Robot](https://www.roboticsproceedings.org/rss20/p052.html)** · 2024<br>[![arXiv 2403.12943](https://img.shields.io/badge/arXiv-2403.12943-b31b1b)](https://arxiv.org/abs/2403.12943) | Cross-attention 将 `prompt_video` 与当前观测映射为动作。 | [项目](https://vid2robot.github.io/) |

### 从带运动信息的示范学习

| 工作 | 示范输入 | 核心做法 / 资源 |
| --- | --- | --- |
| **[BPP](https://arxiv.org/abs/2606.30457)** · 2026<br>[![arXiv 2606.30457](https://img.shields.io/badge/arXiv-2606.30457-b31b1b)](https://arxiv.org/abs/2606.30457) | iPhUMI 感知动作示范 | 用示范条件化操作策略。[代码](https://github.com/real-stanford/behavior_prompting) |
| **[RICL](https://proceedings.mlr.press/v305/sridhar25a.html)** · 2025<br>[![arXiv 2508.02062](https://img.shields.io/badge/arXiv-2508.02062-b31b1b)](https://arxiv.org/abs/2508.02062) | 检索到的机器人示范 | 为预训练 VLA 加入上下文条件；使用 10–20 条目标任务示范。[代码](https://github.com/ricl-vla/ricl_openpi) |
| **[Instant Policy](https://arxiv.org/abs/2411.12633)** · 2024<br>[![arXiv 2411.12633](https://img.shields.io/badge/arXiv-2411.12633-b31b1b)](https://arxiv.org/abs/2411.12633) | 点云 + 夹爪位姿 / 状态 | 用伪示范训练图扩散策略。[代码](https://github.com/vv19/instant_policy) |
| **[ICRT](https://arxiv.org/abs/2408.15980)** · 2024<br>[![arXiv 2408.15980](https://img.shields.io/badge/arXiv-2408.15980-b31b1b)](https://arxiv.org/abs/2408.15980) | 机器人观测 + 状态 + 动作 | 在示范与执行序列上做 next-token prediction。[代码](https://github.com/Max-Fu/icrt) · [数据](https://huggingface.co/datasets/Ravenh97/ICRT-MT) |

### 从交互中学习，以及与 TTT 的区别

| 工作 | 测试时改变什么？ | 核心做法 / 资源 |
| --- | --- | --- |
| **[Zeva](https://arxiv.org/abs/2608.30880)** · 2026<br>[![arXiv 2608.30880](https://img.shields.io/badge/arXiv-2608.30880-b31b1b)](https://arxiv.org/abs/2608.30880) | 外部记忆；策略冻结 | 检索动作引起的状态变化，复用跨尝试经验。[代码](https://github.com/air-embodied-brain/Zeva) |
| **[LocoFormer](https://proceedings.mlr.press/v305/liu25a.html)** · 2025<br>[![arXiv 2509.23745](https://img.shields.io/badge/arXiv-2509.23745-b31b1b)](https://arxiv.org/abs/2509.23745) | 交互上下文 | 长上下文运动控制适应。[项目](https://generalist-locomotion.github.io/) |
| **[RoboTTT](https://arxiv.org/abs/2607.15275)** · 2026<br>[![arXiv 2607.15275](https://img.shields.io/badge/arXiv-2607.15275-b31b1b)](https://arxiv.org/abs/2607.15275) | 通过梯度更新 fast weights | 将长时视觉动作历史压入自适应记忆。[项目](https://research.nvidia.com/labs/gear/robottt/) |
| **[WAM-TTT](https://arxiv.org/abs/2607.06988)** · 2026<br>[![arXiv 2607.06988](https://img.shields.io/badge/arXiv-2607.06988-b31b1b)](https://arxiv.org/abs/2607.06988) | 通过梯度更新轻量记忆 | 预测人类视频动态，使冻结 WAM 适应任务。 |

<details>
<summary>早期工作与其他路线 — 35 篇</summary>

### 基础工作

- **[One-Shot Imitation Learning](https://papers.nips.cc/paper/2017/hash/ba3866600c3540f67c1e9575e213be0a-Abstract.html)** · 2017 — 示范配对训练。 [![arXiv 1703.07326](https://img.shields.io/badge/arXiv-1703.07326-b31b1b)](https://arxiv.org/abs/1703.07326)
- **[MOSAIC](https://arxiv.org/abs/2110.13423)** · 2021 — 注意力与时序对比学习。[代码](https://github.com/rll-research/mosaic) [![arXiv 2110.13423](https://img.shields.io/badge/arXiv-2110.13423-b31b1b)](https://arxiv.org/abs/2110.13423)
- **[BC-Z](https://proceedings.mlr.press/v164/jang22a.html)** · 2022 — 语言或人类视频条件策略。[项目](https://sites.google.com/view/bc-z/home) [![arXiv 2202.02005](https://img.shields.io/badge/arXiv-2202.02005-b31b1b)](https://arxiv.org/abs/2202.02005)
- **[VIMA](https://proceedings.mlr.press/v202/jiang23b.html)** · 2022 — 多模态任务描述。[代码](https://github.com/vimalabs/VIMA) [![arXiv 2210.03094](https://img.shields.io/badge/arXiv-2210.03094-b31b1b)](https://arxiv.org/abs/2210.03094)

### 更多示范条件策略

- **[ICI-VLA](https://arxiv.org/abs/2609.07581)** · 2026 — 为固定的文本动作 VLA 检索阶段对齐的机器人短示范，训练时掩蔽动作前缀。[![arXiv 2609.07581](https://img.shields.io/badge/arXiv-2609.07581-b31b1b)](https://arxiv.org/abs/2609.07581)
- **[ContextFlow](https://arxiv.org/abs/2609.06852)** · 2026 — 压缩机器人 RGB、状态与动作示范，通过条件流匹配生成连续动作块。[项目](https://dingjiansw101.github.io/contextflow-page/) · [数据](https://huggingface.co/datasets/vo2yager/aloha_incontext) [![arXiv 2609.06852](https://img.shields.io/badge/arXiv-2609.06852-b31b1b)](https://arxiv.org/abs/2609.06852)
- **[ReCAP](https://arxiv.org/abs/2606.15631)** · 2026 — 用检索到的跨本体状态–动作片段条件化冻结 WAM，通过扩展示范库加入新任务。[项目](https://recap-robot.github.io/) [![arXiv 2606.15631](https://img.shields.io/badge/arXiv-2606.15631-b31b1b)](https://arxiv.org/abs/2606.15631)
- **[SynthICL](https://arxiv.org/abs/2606.08154)** · 2026 — 用合成示范训练 RGB 流匹配策略。 [![arXiv 2606.08154](https://img.shields.io/badge/arXiv-2606.08154-b31b1b)](https://arxiv.org/abs/2606.08154)
- **[Instant-Fold](https://arxiv.org/abs/2606.04269)** · 2026 — RGB-D 示范条件下的衣物折叠。[项目](https://instant-fold.github.io/) [![arXiv 2606.04269](https://img.shields.io/badge/arXiv-2606.04269-b31b1b)](https://arxiv.org/abs/2606.04269)
- **[HiST-AT](https://arxiv.org/abs/2604.15215)** · 2026 — 分层动作 token 化。 [![arXiv 2604.15215](https://img.shields.io/badge/arXiv-2604.15215-b31b1b)](https://arxiv.org/abs/2604.15215)
- **[ICLR](https://arxiv.org/abs/2603.07530)** · 2026 — 视觉推理轨迹与动作预测。 [![arXiv 2603.07530](https://img.shields.io/badge/arXiv-2603.07530-b31b1b)](https://arxiv.org/abs/2603.07530)
- **[Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt](https://arxiv.org/abs/2505.20795)** · 2025 — 交叉预测预训练与共享动作表征。 [![arXiv 2505.20795](https://img.shields.io/badge/arXiv-2505.20795-b31b1b)](https://arxiv.org/abs/2505.20795)
- **[Human2Robot](https://arxiv.org/abs/2502.16587)** · 2025 — 人机视频配对与解耦动作解码。[数据](https://huggingface.co/datasets/dannyXSC/HumanAndRobot) [![arXiv 2502.16587](https://img.shields.io/badge/arXiv-2502.16587-b31b1b)](https://arxiv.org/abs/2502.16587)
- **[XSkill](https://arxiv.org/abs/2307.09955)** · 2023 — 跨本体技能发现与组合。[代码](https://github.com/real-stanford/xskill) [![arXiv 2307.09955](https://img.shields.io/badge/arXiv-2307.09955-b31b1b)](https://arxiv.org/abs/2307.09955)

### 结构化迁移与轨迹回放

- **[Show-Harness](https://arxiv.org/abs/2609.10522)** · 2026 — 将示范视频转为任务步骤，通过语义运动单元与本体专属解释器执行。[项目](https://showlab.github.io/Show-Harness/) [![arXiv 2609.10522](https://img.shields.io/badge/arXiv-2609.10522-b31b1b)](https://arxiv.org/abs/2609.10522)
- **[CFAM](https://arxiv.org/abs/2609.04552)** · 2026 — 对已存技能胶囊做几何适配，保留经验证的同技能族变化，骨干模型不更新。[![arXiv 2609.04552](https://img.shields.io/badge/arXiv-2609.04552-b31b1b)](https://arxiv.org/abs/2609.04552)
- **[StellaVLA](https://arxiv.org/abs/2608.11671)** · 2026 — 检索结构化计划与运动描述。 [![arXiv 2608.11671](https://img.shields.io/badge/arXiv-2608.11671-b31b1b)](https://arxiv.org/abs/2608.11671)
- **[ManiLong-Shot](https://ojs.aaai.org/index.php/AAAI/article/view/38881)** · 2025 — 交互原语与几何匹配。[项目](https://sites.google.com/view/manilong-shot) [![arXiv 2512.16302](https://img.shields.io/badge/arXiv-2512.16302-b31b1b)](https://arxiv.org/abs/2512.16302)
- **[Robust Instant Policy](https://arxiv.org/abs/2506.15157)** · 2025 — 对 LLM 生成的轨迹做稳健聚合。 [![arXiv 2506.15157](https://img.shields.io/badge/arXiv-2506.15157-b31b1b)](https://arxiv.org/abs/2506.15157)
- **[R+X](https://arxiv.org/abs/2407.12957)** · 2024 — 人类视频检索与关键点动作接口。[代码](https://github.com/gpapagiannis/r-plus-x-hand2actions) [![arXiv 2407.12957](https://img.shields.io/badge/arXiv-2407.12957-b31b1b)](https://arxiv.org/abs/2407.12957)
- **[ORION](https://link.springer.com/article/10.1007/s10514-026-10253-8)** · 2024 — 从人类示范提取物体图计划。[项目](https://ut-austin-rpl.github.io/ORION-release/) [![arXiv 2405.20321](https://img.shields.io/badge/arXiv-2405.20321-b31b1b)](https://arxiv.org/abs/2405.20321)
- **[RoboPrompt](https://arxiv.org/abs/2410.12782)** · 2024 — 将物体位姿和关键帧动作编码为文本示例，供冻结 LLM 预测动作。[代码](https://github.com/davidyyd/roboprompt) [![arXiv 2410.12782](https://img.shields.io/badge/arXiv-2410.12782-b31b1b)](https://arxiv.org/abs/2410.12782)
- **[Keypoint Action Tokens](https://arxiv.org/abs/2403.19578)** · 2024 — 将关键点与动作作为 LLM 上下文。[项目](https://www.robot-learning.uk/keypoint-action-tokens) [![arXiv 2403.19578](https://img.shields.io/badge/arXiv-2403.19578-b31b1b)](https://arxiv.org/abs/2403.19578)
- **[DOME](https://arxiv.org/abs/2204.02863)** · 2022 — 视觉伺服后回放运动。[项目](https://www.robot-learning.uk/dome) [![arXiv 2204.02863](https://img.shields.io/badge/arXiv-2204.02863-b31b1b)](https://arxiv.org/abs/2204.02863)
- **[Coarse-to-Fine Imitation](https://arxiv.org/abs/2105.06411)** · 2021 — 到达交互关键位姿后回放轨迹。[项目](https://www.robot-learning.uk/coarse-to-fine-imitation-learning) [![arXiv 2105.06411](https://img.shields.io/badge/arXiv-2105.06411-b31b1b)](https://arxiv.org/abs/2105.06411)

### 测试时适应及相关工作

- **[SimpleMemVLA](https://arxiv.org/abs/2609.05533)** · 2026 — 将带时间戳的视频历史作为原生上下文，生成的子任务表征条件化流匹配动作头。[代码](https://github.com/wadeKeith/SimpleMemVLA) [![arXiv 2609.05533](https://img.shields.io/badge/arXiv-2609.05533-b31b1b)](https://arxiv.org/abs/2609.05533)
- **[AGM](https://arxiv.org/abs/2608.29537)** · 2026 — 根据抓取、放置的验证结果推进或回退任务进度记忆，底层 VLA 保持冻结。[![arXiv 2608.29537](https://img.shields.io/badge/arXiv-2608.29537-b31b1b)](https://arxiv.org/abs/2608.29537)
- **[CorrectVLA](https://arxiv.org/abs/2608.29967)** · 2026 — 将任务级语言纠正转为局部时间窗内的动作偏置，VLA 权重保持冻结。 [![arXiv 2608.29967](https://img.shields.io/badge/arXiv-2608.29967-b31b1b)](https://arxiv.org/abs/2608.29967)
- **[ICWM](https://arxiv.org/abs/2606.26025)** · 2026 — 从任务无关的观测—动作转移推断控制配置，测试时不更新权重。 [![arXiv 2606.26025](https://img.shields.io/badge/arXiv-2606.26025-b31b1b)](https://arxiv.org/abs/2606.26025)
- **[WHIRL](https://arxiv.org/abs/2207.09450)** · 2022 — 人类视频初始化，再通过机器人交互在线优化。[项目](https://human2robot.github.io/) [![arXiv 2207.09450](https://img.shields.io/badge/arXiv-2207.09450-b31b1b)](https://arxiv.org/abs/2207.09450)
- **[DAML](https://www.roboticsproceedings.org/rss14/p02.html)** · 2018 — 从人类视频进行梯度适应。 [![arXiv 1802.01557](https://img.shields.io/badge/arXiv-1802.01557-b31b1b)](https://arxiv.org/abs/1802.01557)
- **[One-Shot Visual Imitation via Meta-Learning](https://proceedings.mlr.press/v78/finn17a.html)** · 2017 — 基于梯度的元模仿学习。 [![arXiv 1709.04905](https://img.shields.io/badge/arXiv-1709.04905-b31b1b)](https://arxiv.org/abs/1709.04905)
- **[VICX](https://arxiv.org/abs/2606.12028)** · 2026 — 用检索到的图像–状态对将生成式视觉计划落到动作。[项目](https://scaling-group.github.io/vicx/) [![arXiv 2606.12028](https://img.shields.io/badge/arXiv-2606.12028-b31b1b)](https://arxiv.org/abs/2606.12028)
- **[Video In-context Learning](https://arxiv.org/abs/2407.07356)** · 2024 — 视频模仿，本身不输出可执行动作。 [![arXiv 2407.07356](https://img.shields.io/badge/arXiv-2407.07356-b31b1b)](https://arxiv.org/abs/2407.07356)
- **[MimicPlay](https://arxiv.org/abs/2302.12422)** · 2023 — 人类 play 学意图，机器人示范学底层控制。[代码](https://github.com/j96w/MimicPlay) [![arXiv 2302.12422](https://img.shields.io/badge/arXiv-2302.12422-b31b1b)](https://arxiv.org/abs/2302.12422)

</details>

**工业进展：** [Skild S1](https://skild.ai/blogs/s1) — 视频条件化，无需微调。[GEN-1.5](https://generalistai.com/blog/gen-1.5) — 感知动作示例，同时报告 ICL 与梯度适应。架构细节尚未充分公开。

<a id="data"></a>

## 数据

人类视频 ICL 的训练样本：**人类 `prompt_video` + 机器人 RGB / 状态 + 对齐的机器人动作目标**。

| 资源 | 用途 | 说明 |
| --- | --- | --- |
| [H&R](https://huggingface.co/datasets/dannyXSC/HumanAndRobot) | 人机视频配对 | v1 `/action` 是人手位姿，不是实际执行的机器人动作。 |
| [RH20T](https://rh20t.github.io/) | 人类示范 + 机器人轨迹 | 任务对应，不是人机视频逐帧同步。 |
| [MIME](https://sites.google.com/view/mimedataset/home) | 人类示范 + Baxter 轨迹 | 较早的硬件平台与数据格式。 |
| [DROID](https://droid-dataset.github.io/) / [AgiBot World](https://huggingface.co/datasets/agibot-world/AgiBotWorld-Alpha) | 机器人 query 侧 RGB / 动作 | 需要另配人类 `prompt_video`。 |
| [ICRT-MT](https://huggingface.co/datasets/Ravenh97/ICRT-MT) | 机器人 demo/query 实验 | 机器人示范，不是人类视频。 |
| [UMI](https://umi-gripper.github.io/) / [iPhUMI](https://github.com/real-stanford/iPhUMI) | 带运动信息的人类示范 | 手持夹爪，不是徒手视频。 |

<details>
<summary>更多数据资源</summary>

- [ContextFlow ALOHA](https://huggingface.co/datasets/vo2yager/aloha_incontext) — 用于单臂、双臂上下文模仿的机器人遥操作示范。
- [MimicDroid](https://huggingface.co/datasets/Rutav/MimicDroidDataset) — 重定向动作监督。
- [RHyME](https://huggingface.co/datasets/prithwishdan/RHyME) — 仿真配对数据。
- [BC-Z](https://sites.google.com/view/bc-z/home) — 任务级人类视频条件。
- [Open X-Embodiment](https://robotics-transformer-x.github.io/) / [RoboMIND](https://x-humanoid-robomind.github.io/) — 多本体机器人数据。
- [HumanEgo](https://huggingface.co/datasets/Leo-TX/HumanEgo) — 仅人类视频。
- [HumanGen](https://github.com/robbyant-research/Zero-WAM) — 已公布计划，数据待发布。

</details>

<a id="benchmarks"></a>

## 评测

- [RoboReel](https://roboreel.github.io/) · 2026 — 真实人类视频与仿真机器人轨迹配对，含 10 个任务、四套评测；代码与数据待发布。[![arXiv 2609.08209](https://img.shields.io/badge/arXiv-2609.08209-b31b1b)](https://arxiv.org/abs/2609.08209)
- [MEMOBench](https://github.com/Collab-Gen/MEMOBench) · 2026 — 30 个依赖历史的任务，以 4,200 个检查点评估记忆存储、更新与压缩。[数据](https://huggingface.co/datasets/SunSeaLucky/MEMOBench) [![arXiv 2609.07047](https://img.shields.io/badge/arXiv-2609.07047-b31b1b)](https://arxiv.org/abs/2609.07047)
- [BPP：LIBERO / LIBERO-Gen / DrawAnything](https://github.com/real-stanford/behavior_prompting) — 示范条件化评测。
- [RoboTwin 2.0](https://robotwin-platform.github.io/) / [MimicDroid](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) / [VIMA-Bench](https://vimalabs.github.io/) — 任务与环境泛化。
- [Zeva Atomic5 & PIM](https://github.com/air-embodied-brain/Zeva) — 冻结策略评测，以及独立的跨尝试案例。

## 相关清单

[Embodied ICL](https://github.com/asimfish/awesome_ICL) · [ICL in Robot](https://github.com/BraveBoBo/awesome-in-context-learning--in-robot) · [Test-Time Robot Learning](https://github.com/Oliverbansk/Awesome-Test-Time-Robot-Learning) · [Learning from Human Videos](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos) · [WAM](https://github.com/OpenMOSS/Awesome-WAM) · [In-Context RL](https://github.com/dunnolab/awesome-in-context-rl)

[贡献](CONTRIBUTING.md) · [MIT](LICENSE) · 更新：2026-09-11。外链资源遵循各自许可。
