# Robots ICL

**In-Context Learning for Robotics** — 机器人上下文学习的论文、数据与评测。

[English](README.md) · [论文](#papers) · [数据](#data) · [评测](#benchmarks) · [复现笔记](notes/reproducibility.md)

<a id="papers"></a>

## 论文

点击方法名查看论文。年份为首次预印本年份；**TTT 涉及测试时优化**。

### 从人类视频学习

| 工作 | 核心做法 | 资源 |
| --- | --- | --- |
| **[Zero-WAM](https://arxiv.org/abs/2608.26103)** · 2026 | 人类 `prompt_video` → 机器人未来帧与动作。 | [项目](https://robbyant-research.github.io/Zero-WAM/) · [发布计划](https://github.com/robbyant-research/Zero-WAM) |
| **[HOST](https://arxiv.org/abs/2607.20033)** · 2026 | 对齐任务进度，预测机器人未来，再解码动作。 | [代码](https://github.com/CGuangyan-BIT/HOST) · [权重](https://huggingface.co/Guangyan/HOST) |
| **[ViVLA](https://arxiv.org/abs/2512.07582)** · 2025 | 用 expert–agent 配对数据训练视频条件动作预测。 | — |
| **[MimicDroid](https://arxiv.org/abs/2509.09769)** · 2025 | 从 human play 挖掘配对，重定向手腕运动作为监督。 | [基准](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) · [数据](https://huggingface.co/datasets/Rutav/MimicDroidDataset) |
| **[RHyME](https://arxiv.org/abs/2409.06615)** · 2024 | 为机器人轨迹检索、拼接示范片段。 | [代码](https://github.com/portal-cornell/rhyme) · [仿真数据](https://huggingface.co/datasets/prithwishdan/RHyME) |
| **[Vid2Robot](https://www.roboticsproceedings.org/rss20/p052.html)** · 2024 | Cross-attention 将 `prompt_video` 与当前观测映射为动作。 | [项目](https://vid2robot.github.io/) |

### 从带运动信息的示范学习

| 工作 | 示范输入 | 核心做法 / 资源 |
| --- | --- | --- |
| **[BPP](https://arxiv.org/abs/2606.30457)** · 2026 | iPhUMI 感知动作示范 | 用示范条件化操作策略。[代码](https://github.com/real-stanford/behavior_prompting) |
| **[RICL](https://proceedings.mlr.press/v305/sridhar25a.html)** · 2025 | 检索到的机器人示范 | 为预训练 VLA 加入上下文条件；使用 10–20 条目标任务示范。[代码](https://github.com/ricl-vla/ricl_openpi) |
| **[Instant Policy](https://arxiv.org/abs/2411.12633)** · 2024 | 点云 + 夹爪位姿 / 状态 | 用伪示范训练图扩散策略。[代码](https://github.com/vv19/instant_policy) |
| **[ICRT](https://arxiv.org/abs/2408.15980)** · 2024 | 机器人观测 + 状态 + 动作 | 在示范与执行序列上做 next-token prediction。[代码](https://github.com/Max-Fu/icrt) · [数据](https://huggingface.co/datasets/Ravenh97/ICRT-MT) |

### 从交互中学习，以及与 TTT 的区别

| 工作 | 测试时改变什么？ | 核心做法 / 资源 |
| --- | --- | --- |
| **[Zeva](https://arxiv.org/abs/2608.30880)** · 2026 | 外部记忆；策略冻结 | 检索动作引起的状态变化，复用跨尝试经验。[代码](https://github.com/air-embodied-brain/Zeva) |
| **[LocoFormer](https://proceedings.mlr.press/v305/liu25a.html)** · 2025 | 交互上下文 | 长上下文运动控制适应。[项目](https://generalist-locomotion.github.io/) |
| **[RoboTTT](https://arxiv.org/abs/2607.15275)** · 2026 | 通过梯度更新 fast weights | 将长时视觉动作历史压入自适应记忆。[项目](https://research.nvidia.com/labs/gear/robottt/) |
| **[WAM-TTT](https://arxiv.org/abs/2607.06988)** · 2026 | 通过梯度更新轻量记忆 | 预测人类视频动态，使冻结 WAM 适应任务。 |

<details>
<summary>早期工作与其他路线 — 25 篇</summary>

### 基础工作

- **[One-Shot Imitation Learning](https://papers.nips.cc/paper/2017/hash/ba3866600c3540f67c1e9575e213be0a-Abstract.html)** · 2017 — 示范配对训练。
- **[MOSAIC](https://arxiv.org/abs/2110.13423)** · 2021 — 注意力与时序对比学习。[代码](https://github.com/rll-research/mosaic)
- **[BC-Z](https://proceedings.mlr.press/v164/jang22a.html)** · 2022 — 语言或人类视频条件策略。[项目](https://sites.google.com/view/bc-z/home)
- **[VIMA](https://proceedings.mlr.press/v202/jiang23b.html)** · 2022 — 多模态任务描述。[代码](https://github.com/vimalabs/VIMA)

### 更多示范条件策略

- **[SynthICL](https://arxiv.org/abs/2606.08154)** · 2026 — 用合成示范训练 RGB 流匹配策略。
- **[Instant-Fold](https://arxiv.org/abs/2606.04269)** · 2026 — RGB-D 示范条件下的衣物折叠。[项目](https://instant-fold.github.io/)
- **[HiST-AT](https://arxiv.org/abs/2604.15215)** · 2026 — 分层动作 token 化。
- **[ICLR](https://arxiv.org/abs/2603.07530)** · 2026 — 视觉推理轨迹与动作预测。
- **[Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt](https://arxiv.org/abs/2505.20795)** · 2025 — 交叉预测预训练与共享动作表征。
- **[Human2Robot](https://arxiv.org/abs/2502.16587)** · 2025 — 人机视频配对与解耦动作解码。[数据](https://huggingface.co/datasets/dannyXSC/HumanAndRobot)
- **[XSkill](https://arxiv.org/abs/2307.09955)** · 2023 — 跨本体技能发现与组合。[代码](https://github.com/real-stanford/xskill)

### 结构化迁移与轨迹回放

- **[StellaVLA](https://arxiv.org/abs/2608.11671)** · 2026 — 检索结构化计划与运动描述。
- **[ManiLong-Shot](https://arxiv.org/abs/2512.16302)** · 2025 — 交互原语与几何匹配。[项目](https://sites.google.com/view/manilong-shot)
- **[Robust Instant Policy](https://arxiv.org/abs/2506.15157)** · 2025 — 对 LLM 生成的轨迹做稳健聚合。
- **[R+X](https://arxiv.org/abs/2407.12957)** · 2024 — 人类视频检索与关键点动作接口。[代码](https://github.com/gpapagiannis/r-plus-x-hand2actions)
- **[ORION](https://link.springer.com/article/10.1007/s10514-026-10253-8)** · 2024 — 从人类示范提取物体图计划。[项目](https://ut-austin-rpl.github.io/ORION-release/)
- **[Keypoint Action Tokens](https://arxiv.org/abs/2403.19578)** · 2024 — 将关键点与动作作为 LLM 上下文。[项目](https://www.robot-learning.uk/keypoint-action-tokens)
- **[DOME](https://arxiv.org/abs/2204.02863)** · 2022 — 视觉伺服后回放运动。[项目](https://www.robot-learning.uk/dome)
- **[Coarse-to-Fine Imitation](https://arxiv.org/abs/2105.06411)** · 2021 — 到达交互关键位姿后回放轨迹。[项目](https://www.robot-learning.uk/coarse-to-fine-imitation-learning)

### 测试时适应及相关工作

- **[WHIRL](https://arxiv.org/abs/2207.09450)** · 2022 — 人类视频初始化，再通过机器人交互在线优化。[项目](https://human2robot.github.io/)
- **[DAML](https://www.roboticsproceedings.org/rss14/p02.html)** · 2018 — 从人类视频进行梯度适应。
- **[One-Shot Visual Imitation via Meta-Learning](https://proceedings.mlr.press/v78/finn17a.html)** · 2017 — 基于梯度的元模仿学习。
- **[VICX](https://arxiv.org/abs/2606.12028)** · 2026 — 用检索到的图像–状态对将生成式视觉计划落到动作。[项目](https://scaling-group.github.io/vicx/)
- **[Video In-context Learning](https://arxiv.org/abs/2407.07356)** · 2024 — 视频模仿，本身不输出可执行动作。
- **[MimicPlay](https://arxiv.org/abs/2302.12422)** · 2023 — 人类 play 学意图，机器人示范学底层控制。[代码](https://github.com/j96w/MimicPlay)

</details>

**工业进展：** [Skild S1](https://skild.ai/blogs/s1) — 视频条件化，无需微调。[GEN-1.5](https://generalistai.com/blog/gen-1.5) — 感知动作示例，同时报告 ICL 与梯度适应。架构细节尚未充分公开。

<a id="data"></a>

## 数据

人类视频 ICL 的训练样本：**人类 `prompt_video` + 机器人 RGB / 状态 + 对齐的机器人动作目标**。

| 资源 | 用途 | 使用前核对 |
| --- | --- | --- |
| [H&R](https://huggingface.co/datasets/dannyXSC/HumanAndRobot) | 人机视频配对 | v1 `/action` 是人手位姿，不是实际执行的机器人动作。 |
| [RH20T](https://rh20t.github.io/) | 人类示范 + 机器人轨迹 | 任务对应，不是人机视频逐帧同步。 |
| [MIME](https://sites.google.com/view/mimedataset/home) | 人类示范 + Baxter 轨迹 | 较早的硬件平台与数据格式。 |
| [DROID](https://droid-dataset.github.io/) / [AgiBot World](https://huggingface.co/datasets/agibot-world/AgiBotWorld-Alpha) | 机器人 query 侧 RGB / 动作 | 需要另配人类 `prompt_video`。 |
| [ICRT-MT](https://huggingface.co/datasets/Ravenh97/ICRT-MT) | 机器人 demo/query 实验 | 机器人示范，不是人类视频。 |
| [UMI](https://umi-gripper.github.io/) / [iPhUMI](https://github.com/real-stanford/iPhUMI) | 带运动信息的人类示范 | 手持夹爪，不是徒手视频。 |

<details>
<summary>更多数据资源</summary>

- [MimicDroid](https://huggingface.co/datasets/Rutav/MimicDroidDataset) — 重定向动作监督。
- [RHyME](https://huggingface.co/datasets/prithwishdan/RHyME) — 仿真配对数据。
- [BC-Z](https://sites.google.com/view/bc-z/home) — 任务级人类视频条件。
- [Open X-Embodiment](https://robotics-transformer-x.github.io/) / [RoboMIND](https://x-humanoid-robomind.github.io/) — 多本体机器人数据。
- [HumanEgo](https://huggingface.co/datasets/Leo-TX/HumanEgo) — 仅人类视频。
- [HumanGen](https://github.com/robbyant-research/Zero-WAM) — 已公布计划，本次核查时仍待发布。

</details>

<a id="benchmarks"></a>

## 评测

- [BPP：LIBERO / LIBERO-Gen / DrawAnything](https://github.com/real-stanford/behavior_prompting) — 示范条件化评测。
- [RoboTwin 2.0](https://robotwin-platform.github.io/) / [MimicDroid](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) / [VIMA-Bench](https://vimalabs.github.io/) — 任务与环境泛化。
- [Zeva Atomic5 & PIM](https://github.com/air-embodied-brain/Zeva) — 冻结策略评测，以及独立的跨尝试案例。

重点看四项：**未见任务、独立 demo/query、替换示范消融、相同重试预算**。

## 相关清单

[Embodied ICL](https://github.com/asimfish/awesome_ICL) · [ICL in Robot](https://github.com/BraveBoBo/awesome-in-context-learning--in-robot) · [Test-Time Robot Learning](https://github.com/Oliverbansk/Awesome-Test-Time-Robot-Learning) · [Learning from Human Videos](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos) · [WAM](https://github.com/OpenMOSS/Awesome-WAM) · [In-Context RL](https://github.com/dunnolab/awesome-in-context-rl)

[贡献](CONTRIBUTING.md) · [MIT](LICENSE) · 核查日期：2026-09-03。外链资源遵循各自许可。
