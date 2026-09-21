# Robot In-Context Learning

**Robot In-Context Learning: Methods and Applications** 的配套文献库，按照综述分类学整理。每项工作仅在其主要类别下收录一次。

[English](README.md) · 简体中文

条目按首次公开时间倒序排列。链接优先使用 arXiv；无 arXiv 版本时链接正式出版物或官方报告。`—` 表示尚未核实到官方代码仓库。

## 目录

- [方法分类](#methods)
    - [上下文条件策略](#policy)
    - [几何示范迁移](#geometry)
    - [基于世界模型的控制](#world)
    - [基于技能与智能体的执行](#agent)
- [共享的对应与记忆机制](#shared)
- [数据与采集接口](#data)
- [训练与改进](#training)
- [任务落地与失败评估](#grounding)
- [基准与评估](#evaluation)
- [基础与相关综述](#foundations)

<a id="methods"></a>

## 方法分类

四类方法按上下文转化为行为的执行接口划分；预训练、参数更新和自我改进工作保留在对应分支中，用于对比。

<a id="policy"></a>

### 上下文条件策略

#### 示范条件动作生成

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Embodied In-Context Learning for GPT-6 Astra <!-- paper:extra_roboicl --> | [![Report](https://img.shields.io/badge/Report-52616b.svg)](https://mosi-ai.github.io/RoboICL-GPT6-Astra.github.io/) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Mosi-AI/RoboICL) |
| ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models <!-- paper:yang2026icivla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.07581) | — |
| ContextFlow: In-Context Flow Matching for Robot Manipulation <!-- paper:ding2026contextflow --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.06852) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/dingjiansw101/ContextFlow) |
| PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control <!-- paper:choi2026ponderpounce --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.24115) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/worv-ai/PonderPounce) |
| GEN-1.5: Embodied Foundation Models are One-Shot Learners <!-- paper:generalist2026gen15 --> | [![Report](https://img.shields.io/badge/Report-52616b.svg)](https://generalistai.com/blog/gen-1.5) | — |
| Introducing S1: In-Context Learning for Robotics <!-- paper:skild2026s1 --> | [![Report](https://img.shields.io/badge/Report-52616b.svg)](https://www.skild.ai/blogs/s1) | — |
| StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models <!-- paper:xu2026stellavla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.11671) | — |
| Behavior Prompting Policy: Demonstrations as Prompts for Manipulation <!-- paper:patel2026bpp --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.30457) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/real-stanford/behavior_prompting) |
| SynthICL: Scalable In-context Imitation Learning with Synthetic Data <!-- paper:qian2026synthicl --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.08154) | — |
| Instant-Fold: In-Context Imitation Learning for Deformable Object Manipulation <!-- paper:wang2026instantfold --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.04269) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/kelthuzadyl/Instant-Fold) |
| SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos <!-- paper:son2026seetraceact --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.02745) | — |
| A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics <!-- paper:fateh2026histat --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.15215) | — |
| ICLR: In-Context Imitation Learning with Visual Reasoning <!-- paper:nguyen2026iclr --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.07530) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/toannguyen1904/ICLR) |
| Mimic Intent, Not Just Trajectories <!-- paper:huang2026mint --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.08602) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/RenMing-Huang/MINT) |
| See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations <!-- paper:chen2025vivla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.07582) | — |
| RoboSSM: Scalable In-context Imitation Learning via State-Space Models <!-- paper:extra250919658 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.19658) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/youngjuY/RoboSSM) |
| MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos <!-- paper:shah2025mimicdroid --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.09769) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) |
| RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models <!-- paper:sridhar2025ricl --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.02062) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/ricl-vla/ricl_openpi) |
| Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt <!-- paper:extra250520795 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.20795) | — |
| Action Tokenizer Matters in In-Context Imitation Learning <!-- paper:vuong2025actiontokenizer --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.01206) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/andvg3/LipVQ-VAE) |
| One-Shot Imitation under Mismatched Execution <!-- paper:kedia2024rhyme --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2409.06615) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/portal-cornell/rhyme) |
| In-Context Imitation Learning via Next-Token Prediction <!-- paper:fu2024icrt --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2408.15980) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Max-Fu/icrt) |
| Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers <!-- paper:jain2024vid2robot --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2403.12943) | — |
| VIMA: General Robot Manipulation with Multimodal Prompts <!-- paper:jiang2022vima --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2210.03094) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/vimalabs/VIMA) |
| BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning <!-- paper:jang2022bcz --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2202.02005) | — |
| Towards More Generalizable One-shot Visual Imitation Learning <!-- paper:mandi2021mosaic --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2110.13423) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/rll-research/mosaic) |
| Transformers for One-Shot Visual Imitation <!-- paper:dasari2020tosil --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2011.05970) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/SudeepDasari/one_shot_transformers) |
| Learning One-Shot Imitation from Humans without Humans <!-- paper:bonardi2019humans --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1911.01103) | — |
| Task-Embedded Control Networks for Few-Shot Imitation Learning <!-- paper:james2018tec --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1810.03237) | — |
| One-Shot Imitation Learning <!-- paper:duan2017oneshot --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1703.07326) | — |

#### 空间对应与动作表示

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| MatchingPolicy: Correspondence-Aware Policy Enables Cross-Object In-Context Learning <!-- paper:she2026matchingpolicy --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.16715) | — |
| VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances <!-- paper:oh2026vlaff --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.05215) | — |
| Bimanual Robot Manipulation via Multi-Agent In-Context Learning <!-- paper:palma2026bicicle --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.20348) | — |
| Robust Instant Policy: Leveraging Student&#x27;s t-Regression Model for Robust In-context Imitation Learning of Robot Manipulation <!-- paper:oh2025rip --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.15157) | — |
| Point Policy: Unifying Observations and Actions with Key Points for Robot Manipulation <!-- paper:haldar2025pointpolicy --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.20391) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/siddhanthaldar/Point-Policy) |
| SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model <!-- paper:qu2025spatialvla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2501.15830) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/SpatialVLA/SpatialVLA) |
| Instant Policy: In-Context Imitation Learning via Graph Diffusion <!-- paper:vosylius2024instantpolicy --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.12633) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/vv19/instant_policy) |
| In-Context Learning Enables Robot Action Prediction in LLMs <!-- paper:yin2024roboprompt --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.12782) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/davidyyd/roboprompt) |
| Keypoint Abstraction using Large Models for Object-Relative Imitation Learning <!-- paper:fang2024kalm --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.23254) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/FANG-Xiaolin/KALM) |
| Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics <!-- paper:dipalo2024keypoint --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2403.19578) | — |

#### 动作检索与细化

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| TraceFlow: Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces <!-- paper:extra260920646 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.20646) | — |
| SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation <!-- paper:arxiv260920648 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.20648) | — |
| UniMPA: A Unified Memory-Prediction-Action Model via Action-Grounded Transition Modeling <!-- paper:extra260911875 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.11875) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/JiuTian-VL/UniMPA) |
| Retrieve in Time, Correct in Frequency <!-- paper:fan2026rtcf --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.04527) | — |
| SAIL: Test-Time Scaling for In-Context Imitation Learning with VLM <!-- paper:sato2026sail --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.08269) | — |
| DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy <!-- paper:park2025demodiffusion --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.20668) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/demodiffusion/demodiffusion) |
| RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models <!-- paper:arxiv250617811 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.17811) | — |
| REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments <!-- paper:sridhar2024regent --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.04759) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/regent-research/regent) |
| The Surprising Effectiveness of Representation Learning for Visual Imitation <!-- paper:pari2021vinn --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2112.01511) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/jyopari/VINN) |

#### 交互历史与物理适应

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| TEMPO: Learning Temporal Context for Dynamic Robot Manipulation <!-- paper:extra260916864 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.16864) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/tempo-robot/TEMPO) |
| CR-VLA-Force: Learning Control-aware Compliance VLA Model for Robust Contact-rich Robotic Manipulation <!-- paper:mai2026crvlaforce --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.05832) | — |
| Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation <!-- paper:chen2026zeva --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.30880) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/air-embodied-brain/Zeva) |
| TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback <!-- paper:arxiv260825798 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.25798) | — |
| In-Context World Modeling for Robotic Control <!-- paper:wang2026icwm --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.26025) | — |
| AdaTracker: Learning Adaptive In-Context Policy for Cross-Embodiment Active Visual Tracking <!-- paper:wu2026adatracker --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.20305) | — |
| Gated Memory Policy: In-Context Memorization and Adaptation <!-- paper:gao2026gmp --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.18933) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/real-stanford/gated-memory-policy) |
| LocoFormer: Generalist Locomotion via Long-context Adaptation <!-- paper:liu2025locoformer --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.23745) | — |
| Behavioral Exploration: Learning to Explore via In-Context Adaptation <!-- paper:wagenmaker2025exploration --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.09041) | — |
| ReLIC: A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI <!-- paper:elawady2024relic --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.02751) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/aielawady/relic) |
| AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents <!-- paper:grigsby2023amago --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.09971) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/UT-Austin-RPL/amago) |
| In-context Reinforcement Learning with Algorithm Distillation <!-- paper:laskin2022ad --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2210.14215) | — |
| Prompting Decision Transformer for Few-Shot Policy Generalization <!-- paper:xu2022promptdt --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2206.13499) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/mxu34/prompt-dt) |
| Robust Task Representations for Offline Meta-Reinforcement Learning via Contrastive Learning <!-- paper:yuan2022corro --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2206.10442) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/PKU-AI-Edge/CORRO) |
| RMA: Rapid Motor Adaptation for Legged Robots <!-- paper:kumar2021rma --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2107.04034) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/antonilo/rl_locomotion) |
| Modeling Task Uncertainty for Safe Meta-Imitation Learning <!-- paper:matsushima2020uncertainty --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://doi.org/10.3389/frobt.2020.606361) | — |
| FOCAL: Efficient Fully-Offline Meta-Reinforcement Learning via Distance Metric Learning and Behavior Regularization <!-- paper:li2020focal --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2010.01112) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/LanqingLi1993/FOCAL-ICLR) |
| MetaCURE: Meta Reinforcement Learning with Empowerment-Driven Exploration <!-- paper:zhang2020metacure --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2006.08170) | — |
| VariBAD: A Very Good Method for Bayes-Adaptive Deep RL via Meta-Learning <!-- paper:zintgraf2019varibad --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1910.08348) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/lmzintgraf/varibad) |
| Watch, Try, Learn: Meta-Learning from Demonstrations and Reward <!-- paper:zhou2019wtl --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1906.03352) | — |
| Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context Variables <!-- paper:rakelly2019pearl --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1903.08254) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/katerakelly/oyster) |
| A Simple Neural Attentive Meta-Learner <!-- paper:mishra2017snail --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1707.03141) | — |
| Preparing for the Unknown: Learning a Universal Policy with Online System Identification <!-- paper:yu2017uposi --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1702.02453) | — |
| RL²: Fast Reinforcement Learning via Slow Reinforcement Learning <!-- paper:duan2016rl2 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1611.02779) | — |

#### 记忆与长上下文策略

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision <!-- paper:extra260920820 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.20820) | — |
| LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation <!-- paper:arxiv260919796 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.19796) | — |
| SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models <!-- paper:yin2026simplememvla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.05533) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/wadeKeith/SimpleMemVLA) |
| TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation <!-- paper:arxiv260826821 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.26821) | — |
| Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control <!-- paper:shah2026halo --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.25136) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/UT-Austin-RobIn/HALO) |
| EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies <!-- paper:yang2026eventvla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.20092) | — |
| μVLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models <!-- paper:cherepanov2026muvla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.12497) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/CognitiveAISystems/muVLA) |
| ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries <!-- paper:li2026rememvla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.12942) | — |
| MEM: Multi-Scale Embodied Memory for Vision Language Action Models <!-- paper:torne2026mem --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.03596) | — |
| MemER: Scaling Up Memory for Robot Control via Experience Retrieval <!-- paper:sridhar2025memer --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.20328) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/memer-policy/memer) |
| MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation <!-- paper:shi2025memoryvla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.19236) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/shihao1895/MemoryVLA) |
| Learning Long-Context Diffusion Policies via Past-Token Prediction <!-- paper:torne2025ptp --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.09561) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/long-context-dp/ldp) |

#### 预训练策略与跨任务能力

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories <!-- paper:xiaomi2026robotics1 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.15330) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) |
| Wall-OSS-0.5 Technical Report <!-- paper:yu2026walloss05 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.30877) | — |
| π₀.₇: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities <!-- paper:arxiv260415483 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.15483) | — |
| Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning <!-- paper:huang2026fastthinkact --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.09708) | — |
| Emergence of Human to Robot Transfer in Vision-Language-Action Models <!-- paper:arxiv251222414 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.22414) | — |
| Galaxea Open-World Dataset and G0 Dual-System VLA Model <!-- paper:galaxea2025 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.00576) | — |
| GR00T N1: An Open Foundation Model for Generalist Humanoid Robots <!-- paper:nvidia2025gr00t --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.14734) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/NVIDIA/Isaac-GR00T) |
| π₀: A Vision-Language-Action Flow Model for General Robot Control <!-- paper:black2024pi0 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.24164) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Physical-Intelligence/openpi) |
| RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation <!-- paper:liu2024rdt --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.07864) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/thu-ml/RoboticsDiffusionTransformer) |
| Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers <!-- paper:hpt2024 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2409.20537) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/liruiw/HPT) |
| Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation <!-- paper:doshi2024crossformer --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2408.11812) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/rail-berkeley/crossformer) |
| OpenVLA: An Open-Source Vision-Language-Action Model <!-- paper:kim2024openvla --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.09246) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/openvla/openvla) |
| Octo: An Open-Source Generalist Robot Policy <!-- paper:octo2024 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.12213) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/octo-models/octo) |
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models <!-- paper:oxe2023 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.08864) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/google-deepmind/open_x_embodiment) |
| RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking <!-- paper:bharadhwaj2023roboagent --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.01918) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/robopen/roboagent) |
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control <!-- paper:brohan2023rt2 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.15818) | — |
| Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware <!-- paper:zhao2023act --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.13705) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/tonyzhaozh/act) |
| RT-1: Robotics Transformer for Real-World Control at Scale <!-- paper:brohan2022rt1 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2212.06817) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/google-research/robotics_transformer) |

#### 参数适应与策略改进

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface <!-- paper:arxiv260920659 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.20659) | — |
| Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On-Policy Corrections <!-- paper:xu2026bimanualscaling --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.03591) | — |
| Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning <!-- paper:arxiv260821204 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.21204) | — |
| In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use <!-- paper:arxiv260805738 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.05738) | — |
| RoboTTT: Context Scaling for Robot Policies <!-- paper:jiang2026robottt --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.15275) | — |
| Robotic Policy Adaptation via Weight-Space Meta-Learning <!-- paper:extra260607217 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.07217) | — |
| Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis <!-- paper:arxiv260313528 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.13528) | — |
| VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model <!-- paper:arxiv260212063 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.12063) | — |
| World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy <!-- paper:arxiv260206508 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.06508) | — |
| π*₀.₆: a VLA That Learns From Experience <!-- paper:arxiv251114759 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.14759) | — |
| RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation <!-- paper:bousmalis2023robocat --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.11706) | — |
| One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning <!-- paper:yu2018domainadaptive --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1802.01557) | — |
| One-Shot Visual Imitation Learning via Meta-Learning <!-- paper:finn2017mil --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1709.04905) | — |

<a id="geometry"></a>

### 几何示范迁移

#### 视觉对齐与参考跟踪

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| One-Shot Imitation Learning with Invariance Matching for Robotic Manipulation <!-- paper:zhang2024imop --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.13178) | — |
| One-Shot Imitation Learning: A Pose Estimation Perspective <!-- paper:vitiello2023pose --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.12077) | — |
| RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation <!-- paper:vecerik2023robotap --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.15975) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/google-deepmind/tapnet) |
| DINOBot: Robot Manipulation via Retrieval and Alignment with Vision Foundation Models <!-- paper:dipalo2023dinobot --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.13181) | — |
| Demonstrate Once, Imitate Immediately (DOME): Learning Visual Servoing for One-Shot Imitation Learning <!-- paper:valassakis2022dome --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2204.02863) | — |
| Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration <!-- paper:extra210506411 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2105.06411) | — |
| FlowControl: Optical Flow Based Visual Servoing <!-- paper:argus2020flowcontrol --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2007.00291) | — |

#### 轨迹重建与重定向

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| V2-STRep: VLM-Grounded Structured Task Representations for Reusable Robot Skills Acquired from Generated Videos <!-- paper:extra260920582 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.20582) | — |
| Demonstrate once, execute on many: Kinematic intelligence for cross-robot skill transfer <!-- paper:gupta2026kinematic --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://doi.org/10.1126/scirobotics.aea1995) | — |
| HRT1: One-Shot Human-to-Robot Trajectory Transfer for Mobile Manipulation <!-- paper:allu2025hrt1 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.21026) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/IRVLUTD/HRT1) |
| Elastic Motion Policy: An Adaptive Dynamical System for Robust and Efficient One-Shot Imitation Learning <!-- paper:li2025emp --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.08029) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/penn-figueroa-lab/emp) |
| R+X: Retrieval and Execution from Everyday Human Videos <!-- paper:extra240712957 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2407.12957) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/gpapagiannis/r-plus-x-hand2actions) |
| ScrewMimic: Bimanual Imitation from Human Videos with Screw Space Projection <!-- paper:bahety2024screwmimic --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.03666) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/UT-Austin-RobIn/ScrewMimic) |
| DITTO: Demonstration Imitation by Trajectory Transformation <!-- paper:heppert2024ditto --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2403.15203) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/robot-learning-freiburg/DITTO) |
| One-shot Imitation Learning via Interaction Warping <!-- paper:biza2023warping --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.12392) | — |

#### 功能对应与物体替换

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Sparse Meets Dense: Correspondence Guided Robotic Manipulation with Rigid-Deformable Interactions <!-- paper:zhu2026sparsedense --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.01083) | — |
| SemAnCorr: Semantic Anchored Correspondence for Zero-Shot Manipulation Skill Transfer <!-- paper:dong2026semancorr --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.28382) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/semancorr/SemAnCorr) |
| One-Shot Cross-Geometry Skill Transfer through Part Decomposition <!-- paper:thompson2026parttransfer --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.15455) | — |
| GIFT: Geometry-Induced Functional Transfer for Category-level Object Manipulation <!-- paper:defarias2025gift --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.15371) | — |
| FUNCTO: Function-Centric One-Shot Imitation Learning for Tool Manipulation <!-- paper:tang2025functo --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.11744) | — |
| One-Shot Manipulation Strategy Learning by Making Contact Analogies <!-- paper:liu2024magic --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.09627) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/nature21/magic) |
| SE(3)-Equivariant Relational Rearrangement with Neural Descriptor Fields <!-- paper:simeonov2023rndf --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2211.09786) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/anthonysimeonov/relational_ndf) |

#### 多阶段迁移与可复用技能库

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| VLBiMan++: Expanding the Generalization Boundary of Vision-Language Anchored One-Shot Bimanual Manipulation <!-- paper:extra260914310 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.14310) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/hnuzhy/BiRoMan) |
| Continual Field-Adaptive Models (CFAMs) for Post-Deployment Physical AI <!-- paper:extra260904552 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.04552) | — |
| ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation <!-- paper:chen2025manilong --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.16302) | — |
| Learning a Thousand Tasks in a Day <!-- paper:dreczkowski2025mt3 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.10110) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/kamil-dreczkowski/learning_thousand_tasks) |
| Annotation-Free One-Shot Imitation Learning for Multi-Step Manipulation Tasks <!-- paper:wichitwechkarn2025annotationfree --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.24972) | — |
| One-Shot Dual-Arm Imitation Learning <!-- paper:wang2025odil --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.06831) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/kelthuzadyl/ODIL) |

<a id="world"></a>

### 基于世界模型的控制

#### 示范条件未来生成

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| TADreamer: Zero-Shot Language-Guided 3D Navigation for Terrestrial-Aerial Bimodal Robots via Video Imagination <!-- paper:arxiv260919824 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.19824) | — |
| Memory as Plans: World-Action Modeling with Memory-Grounded Planning <!-- paper:extra260911561 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.11561) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/aipixel/MaP-WAM) |
| Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization <!-- paper:zhou2026zerowam --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.26103) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/robbyant-research/Zero-WAM) |
| HOST: Robots Acquire Manipulation Skills in Seconds from a Single Human Video <!-- paper:chen2026host --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.20033) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/CGuangyan-BIT/HOST) |
| WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory <!-- paper:arxiv260718840 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.18840) | — |
| Retrieve, Don&#x27;t Retrain: Extending Vision Language Action Models to New Tasks at Test Time <!-- paper:park2026recap --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.15631) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/jeongeun980906/ReCAP-Cosmos-Policy) |
| VICX: Generalizable Robot Manipulation via Video Generation and In-Context Operator Network <!-- paper:extra260612028 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.12028) | — |
| Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation <!-- paper:he2026demojepa --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.20811) | — |
| OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation <!-- paper:goswami2025osviwm --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.20425) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/raktimgg/osvi-wm) |
| Human2Robot: Learning Robot Actions from Paired Human-Robot Videos <!-- paper:extra250216587 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.16587) | — |

#### 预测规划、记忆与恢复

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning <!-- paper:arxiv260919315 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.19315) | — |
| Causal-History Test-Time Scaling for Failure Recovery in Autoregressive World-Action Models <!-- paper:extra260918016 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.18016) | — |
| τ₀-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation <!-- paper:arxiv260816885 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.16885) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/sii-research/tau-0-vla) |
| Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models <!-- paper:core2026realignment --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.14822) | — |
| MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models <!-- paper:shi2026memoryvlapp --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.09827) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/shihao1895/MemoryVLA) |
| MetaDiffuser: Diffusion Model as Conditional Planner for Offline Meta-RL <!-- paper:ni2023metadiffuser --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.19923) | — |
| Decomposed Mutual Information Optimization for Generalized Context in Meta-Reinforcement Learning <!-- paper:mu2022domino --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2210.04209) | — |
| Robustness via Retrying: Closed-Loop Robotic Manipulation with Self-Supervised Learning <!-- paper:ebert2018retrying --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1810.03043) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/febert/robustness_via_retrying) |
| Universal Planning Networks <!-- paper:srinivas2018upn --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1804.00645) | — |

#### 模型适应与自我改进

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning <!-- paper:extra260912278 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.12278) | — |
| Motus2: A Self-Evolving General World Model for Dexterous Manipulation <!-- paper:bi2026motus2 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.30237) | — |
| WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time <!-- paper:arxiv260706988 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.06988) | — |
| Self-Improving Loops for Visual Robotic Planning <!-- paper:luo2025silvr --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.06658) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/brown-palm/silvr) |

<a id="agent"></a>

### 基于技能与智能体的执行

#### 技能序列与任务结构

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation <!-- paper:arxiv260920791 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.20791) | — |
| UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations <!-- paper:kim2025uniskill --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.08787) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/KimHanjung/UniSkill) |
| Enabling Long(er) Horizon Imitation for Manipulation Tasks by Modeling Subgoal Transitions <!-- paper:jain2025transitions --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://proceedings.mlr.press/v305/jain25b.html) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/shivam89jain/SGPT-long-horizon-imitation) |
| Vision-based Manipulation from Single Human Video with Open-World Object Graphs <!-- paper:zhu2024orion --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.20321) | — |
| XSkill: Cross Embodiment Skill Discovery <!-- paper:xu2023xskill --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.09955) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/real-stanford/xskill) |
| MimicPlay: Long-Horizon Imitation Learning by Watching Human Play <!-- paper:wang2023mimicplay --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2302.12422) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/j96w/MimicPlay) |
| One-shot Visual Imitation via Attributed Waypoints and Demonstration Augmentation <!-- paper:chang2023awda --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2302.04856) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/MatthewChang/osvi-awda) |
| Neural Task Programming: Learning to Generalize Across Hierarchical Tasks <!-- paper:xu2017ntp --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1710.01813) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/StanfordVL/ntp) |

#### 程序、工具与分层控制

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control <!-- paper:arxiv260919554 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.19554) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/zhangzhongbo2213/VABench) |
| Navi-Agent: Unlocalized Monocular Navigation Agent <!-- paper:arxiv260920388 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.20388) | — |
| WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories <!-- paper:extra260918435 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.18435) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/tsudalab/WetRobo) |
| In-Context Robot Learning with VLM Agents <!-- paper:cheng2026gptpolicyeval --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.19138) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/cheng-haha/GPT-Policy) |
| Show-Harness: Just a VLM Agent Can Play Robots <!-- paper:chen2026showharness --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.10522) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/showlab/Show-Harness) |
| A Few Words Go a Long Way: Language Guided Robot Policy Synthesis <!-- paper:chen2026architect --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.23784) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/robo-architect/architect-franka) |
| Addressing the Orchestration Gap in Generalist Robots via Physical Agency <!-- paper:galanti2026physicalagency --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.21725) | — |
| Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents <!-- paper:arxiv260708448 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.08448) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/RLinf/RPent) |
| What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents <!-- paper:hu2026orchestrating --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.10267) | — |
| When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution <!-- paper:arxiv260514504 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.14504) | — |
| CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation <!-- paper:arxiv260322435 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.22435) | — |
| RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks <!-- paper:cui2026roboclaw --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.11558) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/RoboClaw-Robotics/RoboClaw) |
| Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control <!-- paper:chen2026steerable --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.13193) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/steerable-policies/steerable-policies-bridge) |
| MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation <!-- paper:singh2024malmm --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.17636) | — |
| Trust the PRoC3S: Solving Long-Horizon Robotics Problems with LLMs and Constraint Satisfaction <!-- paper:curtis2025proc3s --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.05572) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Learning-and-Intelligent-Systems/proc3s) |
| VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models <!-- paper:huang2023voxposer --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.05973) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/huangwl18/VoxPoser) |
| SayTap: Language to Quadrupedal Locomotion <!-- paper:tang2023saytap --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.07580) | — |
| ProgPrompt: Generating Situated Robot Task Plans using Large Language Models <!-- paper:singh2022progprompt --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2209.11302) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/NVlabs/progprompt-vh) |
| Code as Policies: Language Model Programs for Embodied Control <!-- paper:liang2022codeaspolicies --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2209.07753) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/google-research/google-research/tree/master/code_as_policies) |
| Inner Monologue: Embodied Reasoning through Planning with Language Models <!-- paper:huang2022monologue --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2207.05608) | — |
| Do As I Can, Not As I Say: Grounding Language in Robotic Affordances <!-- paper:ahn2022saycan --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2204.01691) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/google-research/google-research/tree/master/saycan) |

#### 保留指导与知识复用

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Learning and Transferring Closed-Loop Robot Software <!-- paper:arxiv260919906 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.19906) | — |
| CoreSense: Traceable Failure Recall and Conflict-Aware Belief Gating for Auditable Robot Decisions <!-- paper:arxiv260919512 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.19512) | — |
| MessyMem: Learning-from-Doing Memory for Mobile Manipulation <!-- paper:extra260915976 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.15976) | — |
| 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation <!-- paper:extra260911308 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.11308) | — |
| Safe Task Planning with Long-Term Graph Memory for Embodied Agents <!-- paper:extra260908444 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.08444) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/lty759/SafeMem) |
| AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies <!-- paper:arxiv260829537 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.29537) | — |
| ASPIRE: Agentic /Skills Discovery for Robotics <!-- paper:lu2026aspire --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.00272) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/NVlabs/ASPIRE) |
| Guava: An Effective and Universal Harness for Embodied Manipulation <!-- paper:liu2026guava --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.18363) | — |
| EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents <!-- paper:ju2026embodiskill --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.10332) | — |
| Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation <!-- paper:xie2026uniskillrepo --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.02623) | — |
| Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation <!-- paper:kumar2026aor --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.04466) | — |
| Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills <!-- paper:arxiv250918597 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.18597) | — |
| Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models <!-- paper:tziafas2024lrll --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.18746) | — |
| VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought <!-- paper:sarch2024ical --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.14596) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Gabesarch/ICAL) |
| Learning to Learn Faster from Human Feedback with Language Model Predictive Control <!-- paper:liang2024lmpc --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.11450) | — |
| Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections <!-- paper:zha2023droc --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.10678) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Stanford-ILIAD/droc) |

#### 落地执行、反馈与失败恢复

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Training-Free Action Correction for VLA Model Failures via Language Feedback <!-- paper:arxiv260829967 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.29967) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/owenk3/correct_vla) |
| PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration <!-- paper:physcap2026 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.21031) | — |
| PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents <!-- paper:arxiv260817129 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.17129) | — |
| VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation <!-- paper:chen2026volo --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.07723) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/NVlabs/VoLoAgent) |
| Where to Look: Can Foundation Models Reach a Target Viewpoint Through Active Exploration? <!-- paper:arxiv260601247 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.01247) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/aim-uofa/TVRBench) |
| From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation <!-- paper:arxiv260511951 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.11951) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/EDEM-AI/AgentChord) |
| In-Context Iterative Policy Improvement for Dynamic Manipulation <!-- paper:merwe2025icpi --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.15021) | — |
| In-situ Value-aligned Human-Robot Interactions with Physical Constraints <!-- paper:li2025iclhf --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.07606) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/ICLHF/ICLHF) |
| RACER: Rich Language-Guided Failure Recovery Policies for Imitation Learning <!-- paper:dai2024racer --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2409.14674) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/sled-group/RACER) |
| Introspective Planning: Aligning Robots&#x27; Uncertainty with Inherent Task Ambiguity <!-- paper:liang2024introplan --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.06529) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/kevinliang888/IntroPlan) |
| Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners <!-- paper:ren2023knowno --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.01928) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/google-research/google-research/tree/master/language_model_uncertainty) |
| REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction <!-- paper:liu2023reflect --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.15724) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/columbia-ai-robotics/reflect) |

#### 智能体驱动学习与自我改进

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention <!-- paper:arxiv260914633 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.14633) | — |
| SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies <!-- paper:arxiv260831167 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.31167) | — |
| EXIMO: VLM Guided Exploration of VLA Policies <!-- paper:arxiv260819891 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.19891) | — |
| Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence <!-- paper:arxiv260816590 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.16590) | — |
| Teach and Grow: An Agent-Centered Architecture for General Robot Learning <!-- paper:arxiv260817209 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.17209) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/IRMVLab/TGL) |
| Self-Evolving Embodied Agents via Skill-Harness Evolution <!-- paper:wang2026shaper --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.11350) | — |
| ENPIRE: Agentic Robot Policy Self-Improvement in the Real World <!-- paper:xiao2026enpire --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.19980) | — |
| Playful Agentic Robot Learning <!-- paper:arxiv260619419 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.19419) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Playful-RATs/rats) |
| AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents <!-- paper:ahn2024autort --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.12963) | — |

<a id="shared"></a>

## 共享的对应与记忆机制

### 跨具身表示

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics <!-- paper:yuan2024robopoint --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.10721) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/wentaoyuan/RoboPoint) |
| XIRL: Cross-embodiment Inverse Reinforcement Learning <!-- paper:zakka2021xirl --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2106.03911) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/google-research/google-research/tree/master/xirl) |
| Time-Contrastive Networks: Self-Supervised Learning from Video <!-- paper:sermanet2017tcn --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1704.06888) | — |

### 持久场景与世界表示

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| HitMem: Hierarchical Temporal 3D Memory with Multi-Modal Context-Aware Retrieval for Dynamic Environments <!-- paper:arxiv260900950 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.00950) | — |
| DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments <!-- paper:arxiv260900619 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.00619) | — |
| LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding <!-- paper:arxiv260819059 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.19059) | — |
| Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation <!-- paper:arxiv260618960 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.18960) | — |
| Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments <!-- paper:arxiv260101075 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.01075) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/hlillemark/flowm) |

<a id="data"></a>

## 数据与采集接口

### 机器人示范与遥操作

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| AGIBOT WORLD 2026 Theme 3: Reinforcement Learning <!-- paper:agibot2026corrections --> | [![Report](https://img.shields.io/badge/Report-52616b.svg)](https://agibot.com/article/231/detail/95.html) | — |
| AgiBot World 2026 <!-- paper:agibot2026release --> | [![Dataset](https://img.shields.io/badge/Dataset-52616b.svg)](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026) | — |
| RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dataset for Generalizable Embodied Intelligence <!-- paper:robomind2025v2 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.24653) | — |
| RoboCOIN: An Open-Sourced Bimanual Robotic Data Collection for Integrated Manipulation <!-- paper:robocoin2025 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.17441) | — |
| AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems <!-- paper:agibot2025 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.06669) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/OpenDriveLab/AgiBot-World) |
| RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation <!-- paper:robomind2024 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.13877) | — |
| DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset <!-- paper:khazatsky2024droid --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2403.12945) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/droid-dataset/droid) |
| BridgeData V2: A Dataset for Robot Learning at Scale <!-- paper:walke2023bridge --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.12952) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/rail-berkeley/bridge_data_v2) |
| RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot <!-- paper:fang2023rh20t --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.00595) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/rh20t/rh20t_api) |
| Bridge Data: Boosting Generalization of Robotic Skills with Cross-Domain Datasets <!-- paper:bridge2021 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2109.13396) | — |

### 手持与通用操作接口

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone <!-- paper:simpleai2026hifiumi --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.25895) | — |
| YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale <!-- paper:ohkawa2026yubi --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.10244) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/airoa-org/yubi-sw) |
| OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction <!-- paper:luo2026omniumi --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.10647) | — |
| FastUMI: A Scalable and Hardware-Independent Universal Manipulation Interface with Dataset <!-- paper:zhaxizhuoma2024fastumi --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2409.19499) | — |
| UMI on Legs: Making Manipulation Policies Mobile with Manipulation-Centric Whole-body Controllers <!-- paper:ha2024umilegs --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2407.10353) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/real-stanford/umi-on-legs) |
| Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots <!-- paper:chi2024umi --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.10329) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/real-stanford/universal_manipulation_interface) |

### 人类视频与第一视角数据

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine <!-- paper:cao2026acedata --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.28625) | — |
| Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning <!-- paper:aoe2026openaoe --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.14183) | — |
| ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining <!-- paper:li2026aceego --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.17200) | — |
| EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World <!-- paper:punamiya2026egoverse --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.07607) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/GaTech-RL2/EgoVerse) |
| EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data <!-- paper:egoscale2026 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.16710) | — |
| EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video <!-- paper:egodex2025 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.11709) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/apple/ml-egodex) |
| HOT3D: Hand and Object Tracking in 3D from Egocentric Multi-View Videos <!-- paper:hot3d2025 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.19167) | — |
| Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives <!-- paper:grauman2023egoexo4d --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.18259) | — |
| HoloAssist: an Egocentric Human Interaction Dataset for Interactive AI Assistants in the Real World <!-- paper:holoassist2023 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.17024) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Ember-HoloAssist/holoassist-release) |
| Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities <!-- paper:assembly1012022 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2203.14712) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/assembly-101/assembly101-temporal-action-segmentation) |
| HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction <!-- paper:hoi4d2022 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2203.01577) | — |
| Ego4D: Around the World in 3,000 Hours of Egocentric Video <!-- paper:grauman2021ego4d --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2110.07058) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/EGO4D/episodic-memory) |
| Rescaling Egocentric Vision <!-- paper:damen2020epic100 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2006.13256) | — |
| The &quot;something something&quot; video database for learning and evaluating visual common sense <!-- paper:goyal2017something --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1706.04261) | — |

### 仿真与示范合成

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| HuRo: Robotizing Human Videos for Scalable VLA Pretraining <!-- paper:extra260910706 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.10706) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/3587jjh/HuRo) |
| RoboTok: An Internet-Scale Data Engine for Human Demonstration Retrieval and Dexterous Manipulation Learning <!-- paper:qian2026robotok --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.03199) | — |
| SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation <!-- paper:lin2026simdex --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.04196) | — |
| Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data <!-- paper:wang2026ego2robot --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.02580) | — |
| SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning <!-- paper:arxiv260509423 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.09423) | — |
| RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots <!-- paper:arxiv260304356 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.04356) | — |
| One-Shot Real-World Demonstration Synthesis for Scalable Bimanual Manipulation <!-- paper:zhou2026bidemosyn --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.09297) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/hnuzhy/BiRoMan) |
| Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation <!-- paper:robosplat2025 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.13175) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/InternRobotics/RoboSplat) |
| You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations <!-- paper:zhou2025yoto --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2501.14208) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/hnuzhy/YOTO) |
| RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots <!-- paper:robocasa2024 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.02523) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/robocasa/robocasa) |
| OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code <!-- paper:faldor2024omniepic --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.15568) | — |
| EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents <!-- paper:zala2024envgen --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2403.12014) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/aszala/envgen) |
| MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations <!-- paper:mandlekar2023mimicgen --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.17596) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/NVlabs/mimicgen_environments) |

<a id="training"></a>

## 训练与改进

### 训练覆盖与规模化

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Public Summary of Training Content for GPT-6 Astra <!-- paper:openai2026astratraining --> | [![Report](https://img.shields.io/badge/Report-52616b.svg)](https://cdn.openai.com/pdf/gpt-6-astra-eu-ai-act-public-summary-of-training-content.pdf) | — |
| Is Diversity All You Need for Scalable Robotic Manipulation? <!-- paper:arxiv250706219 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.06219) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/OpenDriveLab/AgiBot-World) |
| Scaling Instruction-Finetuned Language Models <!-- paper:chung2022flan --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2210.11416) | — |
| MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale <!-- paper:mtopt2021 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2104.08212) | — |

### 观察学习与具身迁移

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation <!-- paper:feng2026regrind --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.11874) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/yunhaif/regrind) |
| Human-to-Robot Imitation in the Wild <!-- paper:bahl2022whirl --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2207.09450) | — |
| REvolveR: Continuous Evolutionary Models for Robot-to-robot Policy Transfer <!-- paper:liu2022revolver --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2202.05244) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/xingyul/revolver) |
| Behavioral Cloning from Observation <!-- paper:torabi2018bco --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1805.01954) | — |

### 交互监督与预测训练

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| PhyWorld: Physics-Faithful World Model for Video Generation <!-- paper:arxiv260519242 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.19242) | — |
| Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training <!-- paper:arxiv260421741 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.21741) | — |
| World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry <!-- paper:arxiv260401985 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.01985) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/world-action-verifier/wav_robot) |
| Video In-context Learning: Autoregressive Transformers are Zero-Shot Video Imitators <!-- paper:extra240707356 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2407.07356) | — |
| ThriftyDAgger: Budget-Aware Novelty and Risk Gating for Interactive Imitation Learning <!-- paper:hoque2021thrifty --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2109.08273) | — |
| DART: Noise Injection for Robust Imitation Learning <!-- paper:laskey2017dart --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1703.09327) | — |
| A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning <!-- paper:ross2011dagger --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1011.0686) | — |

### 自主学习与自我改进

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Self-Improving Embodied Foundation Models <!-- paper:ghasemipour2025selfimproving --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.15155) | — |
| DrEureka: Language Model Guided Sim-To-Real Transfer <!-- paper:ma2024dreureka --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.01967) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/eureka-research/DrEureka) |
| Eureka: Human-Level Reward Design via Coding Large Language Models <!-- paper:ma2023eureka --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.12931) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/eureka-research/Eureka) |
| Self-Improving Robots: End-to-End Autonomous Visuomotor Reinforcement Learning <!-- paper:sharma2023medal --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.01488) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/rehaanahmad2013/self-improving-robots) |

<a id="grounding"></a>

## 任务落地与失败评估

### 进度、不确定性与失败检测

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents <!-- paper:arxiv260623085 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.23085) | — |
| Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies <!-- paper:xu2025faildetect --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.08558) | — |
| Vision Language Models are In-Context Value Learners <!-- paper:arxiv241104549 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.04549) | — |
| Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress <!-- paper:agia2024sentinel --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.04640) | — |
| AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation <!-- paper:duan2024aha --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.00371) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/NVlabs/AHA) |
| Designing Robot Learners that Ask Good Questions <!-- paper:cakmak2012questions --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://homes.cs.washington.edu/~mcakmak/pdfs/2012/cakmak2012hri.pdf) | — |

<a id="evaluation"></a>

## 基准与评估

### 示范利用与任务迁移

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation <!-- paper:gu2026roboreel --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.08209) | — |
| Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks <!-- paper:arxiv260830536 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.30536) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/nubot-nudt/Behavior-Skill) |
| The Imitator Game: Benchmarking Robot Imitative Ability Beyond Action Prediction <!-- paper:zhou2026imitator --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.22301) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/imitator-game/The-Imitator-Game) |
| What Are We Actually Benchmarking in Robot Manipulation? <!-- paper:jiang2026benchmarkaudit --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.04233) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/ripl/ManipulationBenchmarkAudit) |
| RoboSemanticBench: Diagnosing Semantic Grounding in Action Prediction for VLA Models <!-- paper:arxiv260602277 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.02277) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/ZGC-EmbodyAI/RoboSemanticBench) |
| ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies <!-- paper:arxiv260317300 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.17300) | — |
| When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs <!-- paper:arxiv260217659 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.17659) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/yuffish/LIBERO-CF) |
| LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models <!-- paper:fei2025liberoplus --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.13626) | — |
| LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization <!-- paper:zhou2025liberopro --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.03827) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Zxy-MLlab/LIBERO-PRO) |
| RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation <!-- paper:chen2025robotwin2 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.18088) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/RoboTwin-Platform/RoboTwin) |
| On Path to Multimodal Generalist: General-Level and General-Bench <!-- paper:fei2025generallevel --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.04620) | — |
| LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations <!-- paper:ruoss2025lmact --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.01441) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/google-deepmind/lm_act) |
| LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning <!-- paper:liu2023libero --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.03310) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills <!-- paper:gu2023maniskill2 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2302.04659) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/haosulab/ManiSkill2) |
| Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning <!-- paper:yu2019metaworld --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1910.10897) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/rlworkgroup/metaworld) |
| RLBench: The Robot Learning Benchmark &amp; Learning Environment <!-- paper:james2019rlbench --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1909.12271) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/stepjam/RLBench) |

### 记忆与物理适应

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation <!-- paper:sun2026memobench --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.07047) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Collab-Gen/MEMOBench) |
| PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments <!-- paper:arxiv260814441 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.14441) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/thunlp/PACE-Bench) |
| RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies <!-- paper:dai2026robomme --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.04639) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/RoboMME/robomme_benchmark) |
| Memory, Benchmark &amp; Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning <!-- paper:cherepanov2025mikasa --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.10550) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/CognitiveAISystems/MIKASA-Robo) |

### 物理执行与预测评估

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation <!-- paper:arxiv260818701 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.18701) | — |
| LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories <!-- paper:arxiv260818618 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.18618) | — |
| H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models <!-- paper:arxiv260813049 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.13049) | — |
| ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop <!-- paper:arxiv260518746 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.18746) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/ESI-Bench/ESI-Bench) |

<a id="foundations"></a>

## 基础与相关综述

### 机器人控制与学习基础

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation <!-- paper:kalashnikov2018qtopt --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1806.10293) | — |
| End-to-End Training of Deep Visuomotor Policies <!-- paper:levine2015visuomotor --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1504.00702) | — |
| Towards a Unified Behavior Trees Framework for Robot Control <!-- paper:marzinotto2014bt --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://www.csc.kth.se/~ccs/Publications/icra14b.html) | — |
| Hierarchical Task and Motion Planning in the Now <!-- paper:kaelbling2011hpn --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://people.csail.mit.edu/tlp/pdf/2011/hpnICRA11Final.pdf) | — |
| Visual Servo Control, Part I: Basic Approaches <!-- paper:chaumette2006visualservo --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://web.mit.edu/amcp/OldFiles/drg/Chaumette_Part_I.pdf) | — |
| A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation <!-- paper:khatib1987operational --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://khatib.stanford.edu/publications/pdfs/Khatib_1987_RA.pdf) | — |
| A Robust Layered Control System for a Mobile Robot <!-- paper:brooks1985subsumption --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://people.csail.mit.edu/brooks/papers/AIM-864.pdf) | — |
| STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving <!-- paper:fikes1971strips --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://www.sciencedirect.com/science/article/pii/0004370271900105) | — |

### 上下文学习机制

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Parallel Structures in Pre-training Data Yield In-Context Learning <!-- paper:chen2024parallel --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.12530) | — |
| The mechanistic basis of data dependence and abrupt learning in an in-context classification task <!-- paper:reddy2023abrupt --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.03002) | — |
| Position: Do Pretrained Transformers Learn In-Context by Gradient Descent? <!-- paper:shen2023gradient --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.08540) | — |
| Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression <!-- paper:raventos2023diversity --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.15063) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/mansheej/icl-task-diversity) |
| Are Emergent Abilities of Large Language Models a Mirage? <!-- paper:schaeffer2023mirage --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.15004) | — |
| Transformers Learn In-Context by Gradient Descent <!-- paper:vonoswald2022gradient --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2212.07677) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/google-research/self-organising-systems/tree/master/transformers_learn_icl_by_gd) |
| What Can Transformers Learn In-Context? A Case Study of Simple Function Classes <!-- paper:garg2022functions --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2208.01066) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/dtsip/in-context-learning) |
| Data Distributional Properties Drive Emergent In-Context Learning in Transformers <!-- paper:chan2022distribution --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2205.05055) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/deepmind/emergent_in_context_learning) |
| Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? <!-- paper:min2022demonstrations --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2202.12837) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Alrope123/rethinking-demonstrations) |
| An Explanation of In-context Learning as Implicit Bayesian Inference <!-- paper:xie2021bayesian --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2111.02080) | — |
| MetaICL: Learning to Learn In Context <!-- paper:min2022metaicl --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2110.15943) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/facebookresearch/MetaICL) |
| Language Models are Few-Shot Learners <!-- paper:brown2020fewshot --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2005.14165) | — |
| Causal Confusion in Imitation Learning <!-- paper:dehaan2019causal --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1905.11979) | — |
| Attention Is All You Need <!-- paper:vaswani2017attention --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1706.03762) | — |

### 综述与研究方向

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement <!-- paper:duan2026rsisurvey --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.11873) | — |
| The Embodiment Gap in Robot Foundation Models <!-- paper:domae2026embodimentgap --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.18433) | — |
| Data Pyramid for Embodied Manipulation: A Survey <!-- paper:arxiv260724744 --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.24744) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Jasper-aaa/Awesome-Embodied-Data-Pyramid) |
| In-Context Reinforcement Learning under Non-Stationarity: A Survey <!-- paper:run2026nonstationary --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.11906) | — |
| World Action Models: The Next Frontier in Embodied AI <!-- paper:survey2026wam --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.12090) | — |
| World Model for Robot Learning: A Comprehensive Survey <!-- paper:hou2026worldmodel --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.00080) | — |
| Robot Learning from Human Videos: A Survey <!-- paper:ma2026humanvideosurvey --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.27621) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos) |
| Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines <!-- paper:wang2026vladata --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.23001) | — |
| Memory in the Age of AI Agents <!-- paper:hu2025agentmemory --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.13564) | — |
| A Comprehensive Survey on World Models for Embodied AI <!-- paper:li2025embodiedwm --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.16732) | [![Code](https://img.shields.io/badge/Code-181717.svg?logo=github&logoColor=white)](https://github.com/Li-Zn-H/AwesomeWorldModels) |
| A Survey of In-Context Reinforcement Learning <!-- paper:moeini2025icrlsurvey --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.07978) | — |
| A Survey on In-context Learning <!-- paper:dong2024iclsurvey --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2301.00234) | — |
| Recent Advances in Robot Learning from Demonstration <!-- paper:ravichandar2020survey --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://www.annualreviews.org/content/journals/10.1146/annurev-control-100819-063206) | — |
| Meta-Learning in Neural Networks: A Survey <!-- paper:hospedales2022metalearning --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2004.05439) | — |
| Continual Learning for Robotics: Definition, Framework, Learning Strategies, Opportunities and Challenges <!-- paper:lesort2019continual --> | [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1907.00182) | — |
| A Survey of Robot Learning from Demonstration <!-- paper:argall2009survey --> | [![Paper](https://img.shields.io/badge/Paper-52616b.svg)](https://publications.ri.cmu.edu/a-survey-of-robot-learning-from-demonstration) | — |
