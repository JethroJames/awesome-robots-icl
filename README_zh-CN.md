# Awesome Embodied In-Context Learning

以机器人操作为重点，精选部署时利用示范或交互经历适应任务的研究，以及必要的历史工作、数据和评测资源。区分零梯度 ICL、结构化迁移和测试时训练；本列表不是完整综述或成功率排行榜。

[English](README.md) · [复现证据与注意事项](notes/reproducibility.md) · 更新：2026-09-03

## 目录

- [示范条件化策略](#demo)
- [交互历史条件化策略](#memory)
- [结构化示范迁移](#structured)
- [历史基础工作](#history)
- [测试时训练与在线优化](#adapt)
- [相关视频与技能学习方法](#adjacent)
- [工业发布](#industrial)
- [数据与采集资源](#datasets)
- [评测基准](#benchmarks)
- [相关 awesome 仓库](#related)
- [贡献](#contributing)

条目格式为「首个预印本年份（没有则使用出版年份）· 会议／期刊」。会议信息依据正式论文集、论文元数据或作者项目页；未核实的 venue 会明确注明。视频示范统一称为 `prompt_video`；`human-sensorimotor` 还包含设备采集的运动信息，不是纯视频。资源链接仅说明已定位到对应发布，**不保证完整复现**；没有链接也不代表不存在。

<a id="demo"></a>

## 示范条件化策略

根据部署时提供的示范推断行为。是否预测视觉未来属于输出路线，不应与 ICL 适应机制并列成互斥类别。

### 2026

- **[2026 · preprint] Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization** — [Paper](https://arxiv.org/abs/2608.26103) · [Project](https://robbyant-research.github.io/Zero-WAM/) · [Release plan](https://github.com/robbyant-research/Zero-WAM)
  `human-video` `visual-future` · 以人类 prompt_video 为条件预测机器人未来观测和动作，提出 HumanGen 配对数据及未来块训练目标。所查仓库仍是发布计划，代码、权重和数据尚未发布。

- **[2026 · preprint] HOST: Robots Acquire Manipulation Skills in Seconds from a Single Human Video** — [Paper](https://arxiv.org/abs/2607.20033) · [Code](https://github.com/CGuangyan-BIT/HOST) · [Weights](https://huggingface.co/Guangyan/HOST)
  `human-video` `visual-future` · 对齐示范与执行进度，预测机器人自身的未来观测，再推导动作；部署时不做任务特定参数更新。

- **[2026 · preprint] Behavior Prompting Policy: Demonstrations as Prompts for Manipulation** — [Paper](https://arxiv.org/abs/2606.30457) · [Project](https://behavior-prompting.github.io/) · [Code](https://github.com/real-stanford/behavior_prompting)
  `human-sensorimotor` `action-policy` · 使用一条带运动信息的人类示范来条件化视觉动作策略；iPhUMI 示范不等于普通相机拍摄的人类视频。

- **[2026 · preprint] SynthICL: Scalable In-context Imitation Learning with Synthetic Data** — [Paper](https://arxiv.org/abs/2606.08154)
  `RGB-demo` `synthetic-data` · 使用合成示范训练基于 RGB 的 flow-matching 模仿策略，并加入下一子目标图像预测辅助目标。

- **[2026 · preprint] Instant-Fold: In-Context Imitation Learning for Deformable Object Manipulation** — [Paper](https://arxiv.org/abs/2606.04269) · [Project](https://instant-fold.github.io/)
  `human-demo` `RGB-D` · 用形变感知表征和示范条件化 flow 策略完成折叠；项目描述使用 RGB-D 布料 token，不能视为纯 RGB 路线。

- **[2026 · preprint] A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics** — [Paper](https://arxiv.org/abs/2604.15215)
  `robot-demo` `action-tokens` · HiST-AT 研究层级向量量化及时间戳重建，改进上下文模仿学习中的动作表示。

- **[2026 · IROS 2026] ICLR: In-Context Imitation Learning with Visual Reasoning** — [Paper](https://arxiv.org/abs/2603.07530)
  `robot-demo` `visual-future` · 联合生成视觉推理轨迹与底层动作；ICLR 是方法名，作者报告的录用会议是 IROS 2026。

### 2025

- **[2025 · preprint] See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations** — [Paper](https://arxiv.org/abs/2512.07582)
  `human-video` `action-policy` · ViVLA 通过 expert-agent 配对数据学习，同时预测示范动作序列与机器人后续动作。

- **[2025 · ICRA 2026] MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos** — [Paper](https://arxiv.org/abs/2509.09769) · [Project](https://ut-austin-rpl.github.io/MimicDroid/) · [Benchmark](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) · [Data](https://huggingface.co/datasets/Rutav/MimicDroidDataset)
  `human-video` `retargeting` · 从 human play 中挖掘相似行为对，并重定向腕部姿态作为动作监督；所链接代码是已发布的 benchmark。

- **[2025 · CoRL 2025] RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models** — [Paper](https://proceedings.mlr.press/v305/sridhar25a.html) · [Project](https://ricl-vla.github.io/) · [Code](https://github.com/ricl-vla/ricl_openpi)
  `robot-sensorimotor` `retrieval` · 先离线再训练赋予 VLA 上下文适应能力，再检索示范片段供部署使用；论文使用 10–20 条目标任务示范，不是 one-shot。

- **[2025 · ICRA 2026] Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt** — [Paper](https://arxiv.org/abs/2505.20795)
  `human-video` `shared-representation` · 将跨域视频预测预训练与共享动作表示结合，实现无需目标任务微调的人类 prompt_video 条件化控制。

- **[2025 · AAAI 2026] Human2Robot: Learning Robot Actions from Paired Human-Robot Videos** — [Paper](https://arxiv.org/abs/2502.16587) · [Data](https://huggingface.co/datasets/dannyXSC/HumanAndRobot)
  `human-video` `visual-future` · 用 H&R 同步人机视频学习人类条件化的机器人动态表示，再通过解耦动作解码器输出控制。

### 2024

- **[2024 · ICLR 2025] Instant Policy: In-Context Imitation Learning via Graph Diffusion** — [Paper](https://arxiv.org/abs/2411.12633) · [Project](https://www.robot-learning.uk/instant-policy) · [Code](https://github.com/vv19/instant_policy)
  `robot-sensorimotor` `point-cloud` · 通过仿真伪示范学习图扩散模仿；部署输入包含分割点云、夹爪位姿和状态，不是普通人类 RGB 视频。

- **[2024 · ICRA 2025] One-Shot Imitation under Mismatched Execution** — [Paper](https://arxiv.org/abs/2409.06615) · [Project](https://portal.cs.cornell.edu/rhyme/) · [Code](https://github.com/portal-cornell/rhyme) · [Data](https://huggingface.co/datasets/prithwishdan/RHyME)
  `human-video` `pseudo-pairing` · RHyME 利用最优传输，为机器人轨迹检索并组合示范者片段；所链接数据发布以仿真为主。

- **[2024 · ICRA 2025] In-Context Imitation Learning via Next-Token Prediction** — [Paper](https://arxiv.org/abs/2408.15980) · [Project](https://icrt.dev/) · [Code](https://github.com/Max-Fu/icrt) · [Data](https://huggingface.co/datasets/Ravenh97/ICRT-MT)
  `robot-sensorimotor` `action-policy` · ICRT 将机器人观测、本体状态与动作序列放入上下文，根据示范轨迹预测动作。

- **[2024 · RSS 2024] Vid2Robot: End-to-End Video-Conditioned Policy Learning with Cross-Attention Transformers** — [Paper](https://www.roboticsproceedings.org/rss20/p052.html) · [Project](https://vid2robot.github.io/)
  `human-video` `action-policy` · 使用交叉注意力，将 prompt_video 与机器人当前观测直接映射为动作。

### 2023

- **[2023 · CoRL 2023] XSkill: Cross Embodiment Skill Discovery** — [Paper](https://arxiv.org/abs/2307.09955) · [Project](https://xskill.cs.columbia.edu/) · [Code](https://github.com/real-stanford/xskill)
  `human-video` `skill-composition` · 从无标注人机视频中发现跨本体技能原型，并按人类 prompt_video 组合执行技能。


<a id="memory"></a>

## 交互历史条件化策略

通过累积执行经历进行适应的策略。更新外部记忆，不等于更新神经网络参数。

- **[2026 · preprint] Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation** — [Paper](https://arxiv.org/abs/2608.30880) · [Project](https://air-embodied-brain.github.io/Zeva/) · [Code](https://github.com/air-embodied-brain/Zeva)
  `interaction-history` `external-memory` · 冻结策略从尝试内及跨尝试记忆中检索动作引起的状态变化；主协议不是仅输入人类视频的模仿。

- **[2025 · CoRL 2025] LocoFormer: Generalist Locomotion via Long-context Adaptation** — [Paper](https://proceedings.mlr.press/v305/liu25a.html) · [Project](https://generalist-locomotion.github.io/)
  `interaction-history` `locomotion` · 长上下文运动策略利用跨 episode 历史适应不同本体；作为非操作任务的控制先例收录。


<a id="structured"></a>

## 结构化示范迁移

显式转换、检索或回放示范结构的方法。前面的学习式策略也可能使用检索；本节侧重结构化执行接口。

- **[2026 · preprint] StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models** — [Paper](https://arxiv.org/abs/2608.11671)
  `structured-demo` `action-policy` · 离线将轨迹转为计划、子目标和运动描述，再用检索到的结构化示范条件化动作专家，不是直接输入原始视频。

- **[2025 · AAAI 2026] ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation** — [Paper](https://arxiv.org/abs/2512.16302) · [Proceedings](https://ojs.aaai.org/index.php/AAAI/article/download/38881/42843) · [Project](https://sites.google.com/view/manilong-shot)
  `structured-demo` `geometry` · 将示范分解成交互原语，通过不变交互区域匹配计算末端目标，支持长时程执行。

- **[2025 · preprint] Robust Instant Policy: Leveraging Student's t-Regression Model for Robust In-context Imitation Learning of Robot Manipulation** — [Paper](https://arxiv.org/abs/2506.15157)
  `structured-demo` `LLM` · 用 Student’s t 回归聚合 LLM 候选轨迹，降低异常轨迹影响；与图扩散的 Instant Policy 是不同工作。

- **[2024 · ICRA 2025] R+X: Retrieval and Execution from Everyday Human Videos** — [Paper](https://arxiv.org/abs/2407.12957) · [Code](https://github.com/gpapagiannis/r-plus-x-hand2actions)
  `human-video` `retrieval` · 从日常人类视频检索相关片段，再通过 KAT 结构化动作接口迁移执行。

- **[2024 · Autonomous Robots 2026] Vision-based Manipulation from Single Human Video with Open-World Object Graphs** — [Paper](https://link.springer.com/article/10.1007/s10514-026-10253-8) · [Project](https://ut-austin-rpl.github.io/ORION-release/)
  `human-video` `object-graph` · ORION 从单条 RGB 或 RGB-D 人类示范提取物体中心的操作计划；作为结构化方法对照收录。

- **[2024 · RSS 2024] Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics** — [Paper](https://arxiv.org/abs/2403.19578) · [Project](https://www.robot-learning.uk/keypoint-action-tokens)
  `structured-demo` `LLM` · KAT 将视觉关键点和动作轨迹编码为文本预训练 Transformer 可读的 token，无需额外训练该模型。

- **[2022 · IROS 2022] Demonstrate Once, Imitate Immediately (DOME): Learning Visual Servoing for One-Shot Imitation Learning** — [Paper](https://arxiv.org/abs/2204.02863) · [Project](https://www.robot-learning.uk/dome)
  `robot-demo` `trajectory-replay` · 将学习式分割、视觉伺服与示范末端速度回放结合，实现单次示范后执行。

- **[2021 · ICRA 2021] Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration** — [Paper](https://arxiv.org/abs/2105.06411) · [Project](https://www.robot-learning.uk/coarse-to-fine-imitation-learning)
  `robot-demo` `trajectory-replay` · 先到达视觉估计的交互起始位姿，再回放示范中的精细运动速度。


<a id="history"></a>

## 历史基础工作

当代示范条件化策略的代表性先例；并非所有多模态任务接口都是人类视频 ICL。

- **[2022 · ICML 2023] VIMA: Robot Manipulation with Multimodal Prompts** — [Paper](https://proceedings.mlr.press/v202/jiang23b.html) · [Project](https://vimalabs.github.io/) · [Code](https://github.com/vimalabs/VIMA)
  `multimodal-context` `simulation` · 用交错文本和视觉 token 统一任务描述，是多模态条件化先例，并非专门的人类视频 ICL。

- **[2022 · CoRL 2021] BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning** — [Paper](https://proceedings.mlr.press/v164/jang22a.html) · [Project](https://sites.google.com/view/bc-z/home)
  `human-video` `task-embedding` · 用语言或人类视频嵌入条件化多任务机器人策略，是早期规模化任务条件化基线。

- **[2021 · ICRA 2022] Towards More Generalizable One-shot Visual Imitation Learning** — [Paper](https://arxiv.org/abs/2110.13423) · [Code](https://github.com/rll-research/mosaic)
  `robot-demo` `contrastive-learning` · MOSAIC 将注意力与时序对比学习用于多任务单次模仿，并分别评测不更新参数与微调的情形。

- **[2017 · NeurIPS 2017] One-Shot Imitation Learning** — [Paper](https://papers.nips.cc/paper/2017/hash/ba3866600c3540f67c1e9575e213be0a-Abstract.html)
  `robot-demo` `action-policy` · 训练时用一条轨迹描述任务，以另一条轨迹中的状态和动作监督策略，是示范配对范式的早期工作。


<a id="adapt"></a>

## 测试时训练与在线优化

作为对照收录，不与零梯度 ICL 混称。评测应报告更新哪些参数或快状态，以及适应计算和交互预算。

- **[2026 · preprint] RoboTTT: Context Scaling for Robot Policies** — [Paper](https://arxiv.org/abs/2607.15275) · [Project](https://research.nvidia.com/labs/gear/robottt/)
  `fast-weights` `gradient-update` · 把长视觉动作上下文压缩进快权重，训练和推理时均更新快权重；不属于零梯度 ICL。

- **[2026 · preprint] WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time** — [Paper](https://arxiv.org/abs/2607.06988)
  `human-video` `gradient-update` · 通过人类视频预测在测试时适应轻量记忆，基础 WAM 冻结；元训练使用人机配对数据。

- **[2022 · RSS 2022] Human-to-Robot Imitation in the Wild** — [Paper](https://arxiv.org/abs/2207.09450) · [Project](https://human2robot.github.io/)
  `human-video` `online-optimization` · WHIRL 用人类视频初始化行为，再通过机器人交互与采样优化改进；不是只看一次即冻结执行的策略。

- **[2018 · RSS 2018] One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning** — [Paper](https://www.roboticsproceedings.org/rss14/p02.html)
  `human-video` `gradient-update` · DAML 元学习从单条人类示范进行跨域适应的方法，任务适应需要更新策略参数。

- **[2017 · CoRL 2017] One-Shot Visual Imitation Learning via Meta-Learning** — [Paper](https://proceedings.mlr.press/v78/finn17a.html)
  `visual-demo` `gradient-update` · 早期梯度型元模仿方法；只需一条示范不等于测试时不更新参数。


<a id="adjacent"></a>

## 相关视频与技能学习方法

因表征、数据或动作落地的关联而收录；这些协议不等同于人类示范 ICL。

- **[2026 · preprint] VICX: Generalizable Robot Manipulation via Video Generation and In-Context Operator Network** — [Paper](https://arxiv.org/abs/2606.12028) · [Project](https://scaling-group.github.io/vicx/)
  `visual-plan` `retrieval` · 借助检索的图像—状态对，将生成的视觉计划落到机器人轨迹；其上下文不是人类任务视频。

- **[2024 · ICLR 2025] Video In-context Learning: Autoregressive Transformers are Zero-Shot Video Imitators** — [Paper](https://arxiv.org/abs/2407.07356)
  `video-context` `video-only` · 通过视频生成迁移示范中的视觉动态，本身不提供可执行机器人动作。

- **[2023 · CoRL 2023] MimicPlay: Long-Horizon Imitation Learning by Watching Human Play** — [Paper](https://arxiv.org/abs/2302.12422) · [Project](https://mimic-play.github.io/) · [Code](https://github.com/j96w/MimicPlay)
  `human-play` `hierarchical-policy` · 用 human play 学习高层意图、机器人示范学习底层控制；是相关数据迁移路线，不能直接等同于 demo/query ICL 协议。

<a id="industrial"></a>

## 工业发布

以下是公司自述，不等同于同行评审论文或独立复现。未公开的架构、参数规模与数据细节不做推断。

- **[2026] Skild S1** — [官方博客](https://skild.ai/blogs/s1)
  描述使用上下文视频示范指定任务、无需微调的操作能力；披露了示范条件化的高层训练思路，但没有足够实现细节来还原其架构。

- **[2026] GEN-1.5** — [官方博客](https://generalistai.com/blog/gen-1.5)
  区分零梯度 ICL 与少步梯度适应；主要 physical-prompt 协议使用传感器及动作轨迹，也展示从机器人相机观察人手的案例。不能将所有演示都归为纯视频或同一种输入协议。

<a id="datasets"></a>

## 数据与采集资源

下表区分数据已经提供的内容与需要另行构建的配对。原生对应、语义伪配对、重定向和视频生成不能视为同一种监督。完整人类视频 ICL 样本仍需机器人 RGB／状态与目标动作的可靠时间对齐；各版本访问条件和许可请查看原始来源。

| 资源 | 类型 | 实际内容与限制 |
| --- | --- | --- |
| [H&R / HumanAndRobot](https://huggingface.co/datasets/dannyXSC/HumanAndRobot) | 原生对应 | 同步人机视频，含机器人位姿和夹爪记录。v1 的 /action 是机器人坐标系中的人手姿态，不能直接当作已执行机器人动作。 |
| [RH20T](https://rh20t.github.io/) | 原生对应 | 同时提供对应人类示范目录与多模态机器人执行。任务对应不等于人机视频逐帧同步。 |
| [MIME](https://sites.google.com/view/mimedataset/home) | 原生对应 | 包含人类示范视频与 Baxter 拖动示教轨迹，是早期人机对应数据集。 |
| [MimicDroid Dataset](https://huggingface.co/datasets/Rutav/MimicDroidDataset) | 派生监督 | 基于 human play 与重定向构建；属于派生动作监督，不是独立测得的真实机器人 GT。 |
| [RHyME release](https://huggingface.co/datasets/prithwishdan/RHyME) | 伪配对 | 发布仿真示范者／机器人数据及自动配对代码，不能标为现成的真实人类视频库。 |
| [BC-Z](https://sites.google.com/view/bc-z/home) | 任务级 | 人类视频任务描述与机器人示范；使用前应检查发布内容，不能默认轨迹级对齐。 |
| [ICRT-MT](https://huggingface.co/datasets/Ravenh97/ICRT-MT) | 机器人侧 | ICRT 发布的机器人感知动作数据，可用于 robot-demo/query 实验，不是人类视频来源。 |
| [DROID](https://droid-dataset.github.io/) | 机器人侧 | 真实机器人 RGB、本体状态与动作；同任务跨 episode 配对仍需清洗整理。 |
| [Open X-Embodiment](https://robotics-transformer-x.github.io/) | 机器人侧 | 异构机器人数据合集，动作空间、任务标签和各子集许可不同。 |
| [AgiBot World Alpha](https://huggingface.co/datasets/agibot-world/AgiBotWorld-Alpha) | 机器人侧 | 机器人 RGB／动作轨迹，可用于 query 侧或机器人示范训练，但本身不提供所需的人类 prompt_video。 |
| [RoboMIND](https://x-humanoid-robomind.github.io/) | 机器人侧 | 多本体机器人示范，仍需处理控制器差异和动作归一化。 |
| [UMI](https://umi-gripper.github.io/) | 采集接口 | 手持夹爪采集系统及相关发布；记录带设备的人类运动，并非普通徒手视频。 |
| [iPhUMI](https://github.com/real-stanford/iPhUMI) | 采集接口 | 带运动信息示范的采集与处理接口；BPP 仓库链接具体任务的数据和权重。 |
| [HumanEgo](https://huggingface.co/datasets/Leo-TX/HumanEgo) | 人类视频 | 第一视角人类视频来源；只有人类视频不提供配对机器人动作目标。 |
| [HumanGen (announced)](https://github.com/robbyant-research/Zero-WAM) | 待发布 | Zero-WAM 描述的生成式人类视频／机器人轨迹配对数据；截至 2026-09-03，数据仍待发布。 |

<a id="benchmarks"></a>

## 评测基准

- [LIBERO / LIBERO-Gen / DrawAnything](https://github.com/real-stanford/behavior_prompting) — BPP 提供示范条件化训练与评测资源；必须使用相应任务划分，不能只复用环境名称。
- [RoboTwin 2.0](https://robotwin-platform.github.io/) — 双臂仿真与轨迹生成；ICL 需要额外设置未见任务和独立采样示范。
- [MimicDroid benchmark](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) — 基于 RoboCasa，区分物体与环境泛化等级。
- [Zeva Atomic5 and PIM protocols](https://github.com/air-embodied-brain/Zeva) — 区分冻结策略、无重试的基准评测与固定种子的跨尝试案例。
- [VIMA-Bench](https://vimalabs.github.io/) — 程序化生成的多模态任务描述及泛化划分。

最低评测要求：任务级隔离、独立示范／执行 episode、替换或移除 `prompt_video` 的消融，以及相同的重试与适应预算。仅随机切分视频帧不能证明未见任务 ICL。

<a id="related"></a>

## 相关 awesome 仓库

本主题已有直接相关列表。本仓库定位为操作任务与复现证据的精选入口，不主张填补无人整理的空白；欢迎优先向已有列表贡献更正。

- [Awesome Embodied In-Context Learning](https://github.com/asimfish/awesome_ICL) — 直接同主题，包含较广的文献汇总与中文研究笔记。
- [Awesome In-Context Learning in Robot](https://github.com/BraveBoBo/awesome-in-context-learning--in-robot) — 自动摘要及按日期归档，已收录 Zeva；不是单一完整精选目录。
- [Awesome Test-Time Robot Learning](https://github.com/Oliverbansk/Awesome-Test-Time-Robot-Learning) — 更广的部署时适应，包括 ICL、TTT 和策略引导。
- [Awesome Robot Learning from Human Videos](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos) — 人类视频到机器人学习，包含不属于 ICL 的离线训练方法。
- [Awesome WAM](https://github.com/OpenMOSS/Awesome-WAM) — 世界动作模型、数据与评测，与视觉未来路线的 ICL 有交集。
- [Awesome In-Context RL](https://github.com/dunnolab/awesome-in-context-rl) — 上下文强化学习及利用交互历史学习的相关工作。

<a id="contributing"></a>

## 贡献

直接编辑 README 中相应条目即可，无需维护 JSON 或运行生成器。也可通过 issue 提交一手来源；另一语言版本可由维护者协助同步。详见 [贡献指南](CONTRIBUTING.md)。

[MIT License](LICENSE)。所链接论文、代码、数据和媒体保留各自的许可；本仓库不重新分发它们。
