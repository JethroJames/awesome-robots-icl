# 上下文条件策略

[← 分类首页](../README_zh-CN.md) · [English](policy.md)

预训练与参数更新工作在相应分支中列出，作为对照。

按首次公开时间倒序。论文链接优先使用 arXiv，缺省时使用正式出版页；`—` 表示暂无已核实的官方代码链接。

## 分类导航

- [示范条件动作生成](#demo)
- [空间对应与动作表示](#spatial)
- [动作检索与细化](#retrieval)
- [交互历史与物理适应](#history)
- [记忆与长上下文策略](#memory)
- [预训练策略与跨任务能力](#prior)
- [参数适应与策略改进](#update)

<a id="demo"></a>

## 示范条件动作生成

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Embodied In-Context Learning for GPT-6 Astra <!-- paper:extra_roboicl --> | <a href="https://mosi-ai.github.io/RoboICL-GPT6-Astra.github.io/"><img src="https://img.shields.io/badge/Report-52616b.svg?style=flat-square" alt="Report" height="24"></a> | [Code ↗](https://github.com/Mosi-AI/RoboICL) |
| ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models <!-- paper:yang2026icivla --> | <a href="https://arxiv.org/abs/2609.07581"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| ContextFlow: In-Context Flow Matching for Robot Manipulation <!-- paper:ding2026contextflow --> | <a href="https://arxiv.org/abs/2609.06852"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/dingjiansw101/ContextFlow) |
| PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control <!-- paper:choi2026ponderpounce --> | <a href="https://arxiv.org/abs/2608.24115"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/worv-ai/PonderPounce) |
| GEN-1.5: Embodied Foundation Models are One-Shot Learners <!-- paper:generalist2026gen15 --> | <a href="https://generalistai.com/blog/gen-1.5"><img src="https://img.shields.io/badge/Report-52616b.svg?style=flat-square" alt="Report" height="24"></a> | — |
| Introducing S1: In-Context Learning for Robotics <!-- paper:skild2026s1 --> | <a href="https://www.skild.ai/blogs/s1"><img src="https://img.shields.io/badge/Report-52616b.svg?style=flat-square" alt="Report" height="24"></a> | — |
| StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models <!-- paper:xu2026stellavla --> | <a href="https://arxiv.org/abs/2608.11671"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Behavior Prompting Policy: Demonstrations as Prompts for Manipulation <!-- paper:patel2026bpp --> | <a href="https://arxiv.org/abs/2606.30457"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/real-stanford/behavior_prompting) |
| SynthICL: Scalable In-context Imitation Learning with Synthetic Data <!-- paper:qian2026synthicl --> | <a href="https://arxiv.org/abs/2606.08154"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Instant-Fold: In-Context Imitation Learning for Deformable Object Manipulation <!-- paper:wang2026instantfold --> | <a href="https://arxiv.org/abs/2606.04269"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/kelthuzadyl/Instant-Fold) |
| SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos <!-- paper:son2026seetraceact --> | <a href="https://arxiv.org/abs/2606.02745"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics <!-- paper:fateh2026histat --> | <a href="https://arxiv.org/abs/2604.15215"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| ICLR: In-Context Imitation Learning with Visual Reasoning <!-- paper:nguyen2026iclr --> | <a href="https://arxiv.org/abs/2603.07530"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/toannguyen1904/ICLR) |
| Mimic Intent, Not Just Trajectories <!-- paper:huang2026mint --> | <a href="https://arxiv.org/abs/2602.08602"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/RenMing-Huang/MINT) |
| See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations <!-- paper:chen2025vivla --> | <a href="https://arxiv.org/abs/2512.07582"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| RoboSSM: Scalable In-context Imitation Learning via State-Space Models <!-- paper:extra250919658 --> | <a href="https://arxiv.org/abs/2509.19658"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/youngjuY/RoboSSM) |
| MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos <!-- paper:shah2025mimicdroid --> | <a href="https://arxiv.org/abs/2509.09769"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) |
| RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models <!-- paper:sridhar2025ricl --> | <a href="https://arxiv.org/abs/2508.02062"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/ricl-vla/ricl_openpi) |
| Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt <!-- paper:extra250520795 --> | <a href="https://arxiv.org/abs/2505.20795"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Action Tokenizer Matters in In-Context Imitation Learning <!-- paper:vuong2025actiontokenizer --> | <a href="https://arxiv.org/abs/2503.01206"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/andvg3/LipVQ-VAE) |
| One-Shot Imitation under Mismatched Execution <!-- paper:kedia2024rhyme --> | <a href="https://arxiv.org/abs/2409.06615"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/portal-cornell/rhyme) |
| In-Context Imitation Learning via Next-Token Prediction <!-- paper:fu2024icrt --> | <a href="https://arxiv.org/abs/2408.15980"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/Max-Fu/icrt) |
| Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers <!-- paper:jain2024vid2robot --> | <a href="https://arxiv.org/abs/2403.12943"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| VIMA: General Robot Manipulation with Multimodal Prompts <!-- paper:jiang2022vima --> | <a href="https://arxiv.org/abs/2210.03094"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/vimalabs/VIMA) |
| BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning <!-- paper:jang2022bcz --> | <a href="https://arxiv.org/abs/2202.02005"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Towards More Generalizable One-shot Visual Imitation Learning <!-- paper:mandi2021mosaic --> | <a href="https://arxiv.org/abs/2110.13423"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/rll-research/mosaic) |
| Transformers for One-Shot Visual Imitation <!-- paper:dasari2020tosil --> | <a href="https://arxiv.org/abs/2011.05970"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/SudeepDasari/one_shot_transformers) |
| Learning One-Shot Imitation from Humans without Humans <!-- paper:bonardi2019humans --> | <a href="https://arxiv.org/abs/1911.01103"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Task-Embedded Control Networks for Few-Shot Imitation Learning <!-- paper:james2018tec --> | <a href="https://arxiv.org/abs/1810.03237"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| One-Shot Imitation Learning <!-- paper:duan2017oneshot --> | <a href="https://arxiv.org/abs/1703.07326"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="spatial"></a>

## 空间对应与动作表示

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| MatchingPolicy: Correspondence-Aware Policy Enables Cross-Object In-Context Learning <!-- paper:she2026matchingpolicy --> | <a href="https://arxiv.org/abs/2608.16715"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances <!-- paper:oh2026vlaff --> | <a href="https://arxiv.org/abs/2608.05215"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Bimanual Robot Manipulation via Multi-Agent In-Context Learning <!-- paper:palma2026bicicle --> | <a href="https://arxiv.org/abs/2604.20348"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Robust Instant Policy: Leveraging Student&#x27;s t-Regression Model for Robust In-context Imitation Learning of Robot Manipulation <!-- paper:oh2025rip --> | <a href="https://arxiv.org/abs/2506.15157"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Point Policy: Unifying Observations and Actions with Key Points for Robot Manipulation <!-- paper:haldar2025pointpolicy --> | <a href="https://arxiv.org/abs/2502.20391"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/siddhanthaldar/Point-Policy) |
| SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model <!-- paper:qu2025spatialvla --> | <a href="https://arxiv.org/abs/2501.15830"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/SpatialVLA/SpatialVLA) |
| Instant Policy: In-Context Imitation Learning via Graph Diffusion <!-- paper:vosylius2024instantpolicy --> | <a href="https://arxiv.org/abs/2411.12633"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/vv19/instant_policy) |
| In-Context Learning Enables Robot Action Prediction in LLMs <!-- paper:yin2024roboprompt --> | <a href="https://arxiv.org/abs/2410.12782"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/davidyyd/roboprompt) |
| Keypoint Abstraction using Large Models for Object-Relative Imitation Learning <!-- paper:fang2024kalm --> | <a href="https://arxiv.org/abs/2410.23254"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/FANG-Xiaolin/KALM) |
| Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics <!-- paper:dipalo2024keypoint --> | <a href="https://arxiv.org/abs/2403.19578"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="retrieval"></a>

## 动作检索与细化

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| TraceFlow: Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces <!-- paper:extra260920646 --> | <a href="https://arxiv.org/abs/2609.20646"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation <!-- paper:arxiv260920648 --> | <a href="https://arxiv.org/abs/2609.20648"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| UniMPA: A Unified Memory-Prediction-Action Model via Action-Grounded Transition Modeling <!-- paper:extra260911875 --> | <a href="https://arxiv.org/abs/2609.11875"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/JiuTian-VL/UniMPA) |
| Retrieve in Time, Correct in Frequency <!-- paper:fan2026rtcf --> | <a href="https://arxiv.org/abs/2608.04527"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| SAIL: Test-Time Scaling for In-Context Imitation Learning with VLM <!-- paper:sato2026sail --> | <a href="https://arxiv.org/abs/2603.08269"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy <!-- paper:park2025demodiffusion --> | <a href="https://arxiv.org/abs/2506.20668"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/demodiffusion/demodiffusion) |
| RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models <!-- paper:arxiv250617811 --> | <a href="https://arxiv.org/abs/2506.17811"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments <!-- paper:sridhar2024regent --> | <a href="https://arxiv.org/abs/2412.04759"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/regent-research/regent) |
| The Surprising Effectiveness of Representation Learning for Visual Imitation <!-- paper:pari2021vinn --> | <a href="https://arxiv.org/abs/2112.01511"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/jyopari/VINN) |

<a id="history"></a>

## 交互历史与物理适应

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| TEMPO: Learning Temporal Context for Dynamic Robot Manipulation <!-- paper:extra260916864 --> | <a href="https://arxiv.org/abs/2609.16864"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/tempo-robot/TEMPO) |
| CR-VLA-Force: Learning Control-aware Compliance VLA Model for Robust Contact-rich Robotic Manipulation <!-- paper:mai2026crvlaforce --> | <a href="https://arxiv.org/abs/2609.05832"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation <!-- paper:chen2026zeva --> | <a href="https://arxiv.org/abs/2608.30880"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/air-embodied-brain/Zeva) |
| TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback <!-- paper:arxiv260825798 --> | <a href="https://arxiv.org/abs/2608.25798"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| In-Context World Modeling for Robotic Control <!-- paper:wang2026icwm --> | <a href="https://arxiv.org/abs/2606.26025"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| AdaTracker: Learning Adaptive In-Context Policy for Cross-Embodiment Active Visual Tracking <!-- paper:wu2026adatracker --> | <a href="https://arxiv.org/abs/2604.20305"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Gated Memory Policy: In-Context Memorization and Adaptation <!-- paper:gao2026gmp --> | <a href="https://arxiv.org/abs/2604.18933"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/real-stanford/gated-memory-policy) |
| LocoFormer: Generalist Locomotion via Long-context Adaptation <!-- paper:liu2025locoformer --> | <a href="https://arxiv.org/abs/2509.23745"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Behavioral Exploration: Learning to Explore via In-Context Adaptation <!-- paper:wagenmaker2025exploration --> | <a href="https://arxiv.org/abs/2507.09041"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| ReLIC: A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI <!-- paper:elawady2024relic --> | <a href="https://arxiv.org/abs/2410.02751"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/aielawady/relic) |
| AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents <!-- paper:grigsby2023amago --> | <a href="https://arxiv.org/abs/2310.09971"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/UT-Austin-RPL/amago) |
| In-context Reinforcement Learning with Algorithm Distillation <!-- paper:laskin2022ad --> | <a href="https://arxiv.org/abs/2210.14215"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Prompting Decision Transformer for Few-Shot Policy Generalization <!-- paper:xu2022promptdt --> | <a href="https://arxiv.org/abs/2206.13499"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/mxu34/prompt-dt) |
| Robust Task Representations for Offline Meta-Reinforcement Learning via Contrastive Learning <!-- paper:yuan2022corro --> | <a href="https://arxiv.org/abs/2206.10442"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/PKU-AI-Edge/CORRO) |
| RMA: Rapid Motor Adaptation for Legged Robots <!-- paper:kumar2021rma --> | <a href="https://arxiv.org/abs/2107.04034"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/antonilo/rl_locomotion) |
| Modeling Task Uncertainty for Safe Meta-Imitation Learning <!-- paper:matsushima2020uncertainty --> | <a href="https://doi.org/10.3389/frobt.2020.606361"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| FOCAL: Efficient Fully-Offline Meta-Reinforcement Learning via Distance Metric Learning and Behavior Regularization <!-- paper:li2020focal --> | <a href="https://arxiv.org/abs/2010.01112"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/LanqingLi1993/FOCAL-ICLR) |
| MetaCURE: Meta Reinforcement Learning with Empowerment-Driven Exploration <!-- paper:zhang2020metacure --> | <a href="https://arxiv.org/abs/2006.08170"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| VariBAD: A Very Good Method for Bayes-Adaptive Deep RL via Meta-Learning <!-- paper:zintgraf2019varibad --> | <a href="https://arxiv.org/abs/1910.08348"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/lmzintgraf/varibad) |
| Watch, Try, Learn: Meta-Learning from Demonstrations and Reward <!-- paper:zhou2019wtl --> | <a href="https://arxiv.org/abs/1906.03352"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context Variables <!-- paper:rakelly2019pearl --> | <a href="https://arxiv.org/abs/1903.08254"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/katerakelly/oyster) |
| A Simple Neural Attentive Meta-Learner <!-- paper:mishra2017snail --> | <a href="https://arxiv.org/abs/1707.03141"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Preparing for the Unknown: Learning a Universal Policy with Online System Identification <!-- paper:yu2017uposi --> | <a href="https://arxiv.org/abs/1702.02453"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| RL²: Fast Reinforcement Learning via Slow Reinforcement Learning <!-- paper:duan2016rl2 --> | <a href="https://arxiv.org/abs/1611.02779"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="memory"></a>

## 记忆与长上下文策略

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision <!-- paper:extra260920820 --> | <a href="https://arxiv.org/abs/2609.20820"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation <!-- paper:arxiv260919796 --> | <a href="https://arxiv.org/abs/2609.19796"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models <!-- paper:yin2026simplememvla --> | <a href="https://arxiv.org/abs/2609.05533"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/wadeKeith/SimpleMemVLA) |
| TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation <!-- paper:arxiv260826821 --> | <a href="https://arxiv.org/abs/2608.26821"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control <!-- paper:shah2026halo --> | <a href="https://arxiv.org/abs/2606.25136"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/UT-Austin-RobIn/HALO) |
| EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies <!-- paper:yang2026eventvla --> | <a href="https://arxiv.org/abs/2606.20092"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| μVLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models <!-- paper:cherepanov2026muvla --> | <a href="https://arxiv.org/abs/2606.12497"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/CognitiveAISystems/muVLA) |
| ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries <!-- paper:li2026rememvla --> | <a href="https://arxiv.org/abs/2603.12942"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| MEM: Multi-Scale Embodied Memory for Vision Language Action Models <!-- paper:torne2026mem --> | <a href="https://arxiv.org/abs/2603.03596"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| MemER: Scaling Up Memory for Robot Control via Experience Retrieval <!-- paper:sridhar2025memer --> | <a href="https://arxiv.org/abs/2510.20328"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/memer-policy/memer) |
| MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation <!-- paper:shi2025memoryvla --> | <a href="https://arxiv.org/abs/2508.19236"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/shihao1895/MemoryVLA) |
| Learning Long-Context Diffusion Policies via Past-Token Prediction <!-- paper:torne2025ptp --> | <a href="https://arxiv.org/abs/2505.09561"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/long-context-dp/ldp) |

<a id="prior"></a>

## 预训练策略与跨任务能力

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories <!-- paper:xiaomi2026robotics1 --> | <a href="https://arxiv.org/abs/2607.15330"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) |
| Wall-OSS-0.5 Technical Report <!-- paper:yu2026walloss05 --> | <a href="https://arxiv.org/abs/2605.30877"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| π₀.₇: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities <!-- paper:arxiv260415483 --> | <a href="https://arxiv.org/abs/2604.15483"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning <!-- paper:huang2026fastthinkact --> | <a href="https://arxiv.org/abs/2601.09708"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Emergence of Human to Robot Transfer in Vision-Language-Action Models <!-- paper:arxiv251222414 --> | <a href="https://arxiv.org/abs/2512.22414"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Galaxea Open-World Dataset and G0 Dual-System VLA Model <!-- paper:galaxea2025 --> | <a href="https://arxiv.org/abs/2509.00576"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| GR00T N1: An Open Foundation Model for Generalist Humanoid Robots <!-- paper:nvidia2025gr00t --> | <a href="https://arxiv.org/abs/2503.14734"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/NVIDIA/Isaac-GR00T) |
| π₀: A Vision-Language-Action Flow Model for General Robot Control <!-- paper:black2024pi0 --> | <a href="https://arxiv.org/abs/2410.24164"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/Physical-Intelligence/openpi) |
| RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation <!-- paper:liu2024rdt --> | <a href="https://arxiv.org/abs/2410.07864"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/thu-ml/RoboticsDiffusionTransformer) |
| Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers <!-- paper:hpt2024 --> | <a href="https://arxiv.org/abs/2409.20537"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/liruiw/HPT) |
| Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation <!-- paper:doshi2024crossformer --> | <a href="https://arxiv.org/abs/2408.11812"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/rail-berkeley/crossformer) |
| OpenVLA: An Open-Source Vision-Language-Action Model <!-- paper:kim2024openvla --> | <a href="https://arxiv.org/abs/2406.09246"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/openvla/openvla) |
| Octo: An Open-Source Generalist Robot Policy <!-- paper:octo2024 --> | <a href="https://arxiv.org/abs/2405.12213"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/octo-models/octo) |
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models <!-- paper:oxe2023 --> | <a href="https://arxiv.org/abs/2310.08864"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/google-deepmind/open_x_embodiment) |
| RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking <!-- paper:bharadhwaj2023roboagent --> | <a href="https://arxiv.org/abs/2309.01918"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/robopen/roboagent) |
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control <!-- paper:brohan2023rt2 --> | <a href="https://arxiv.org/abs/2307.15818"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware <!-- paper:zhao2023act --> | <a href="https://arxiv.org/abs/2304.13705"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/tonyzhaozh/act) |
| RT-1: Robotics Transformer for Real-World Control at Scale <!-- paper:brohan2022rt1 --> | <a href="https://arxiv.org/abs/2212.06817"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/google-research/robotics_transformer) |

<a id="update"></a>

## 参数适应与策略改进

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface <!-- paper:arxiv260920659 --> | <a href="https://arxiv.org/abs/2609.20659"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On-Policy Corrections <!-- paper:xu2026bimanualscaling --> | <a href="https://arxiv.org/abs/2609.03591"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning <!-- paper:arxiv260821204 --> | <a href="https://arxiv.org/abs/2608.21204"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use <!-- paper:arxiv260805738 --> | <a href="https://arxiv.org/abs/2608.05738"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| RoboTTT: Context Scaling for Robot Policies <!-- paper:jiang2026robottt --> | <a href="https://arxiv.org/abs/2607.15275"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Robotic Policy Adaptation via Weight-Space Meta-Learning <!-- paper:extra260607217 --> | <a href="https://arxiv.org/abs/2606.07217"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis <!-- paper:arxiv260313528 --> | <a href="https://arxiv.org/abs/2603.13528"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model <!-- paper:arxiv260212063 --> | <a href="https://arxiv.org/abs/2602.12063"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy <!-- paper:arxiv260206508 --> | <a href="https://arxiv.org/abs/2602.06508"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| π*₀.₆: a VLA That Learns From Experience <!-- paper:arxiv251114759 --> | <a href="https://arxiv.org/abs/2511.14759"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation <!-- paper:bousmalis2023robocat --> | <a href="https://arxiv.org/abs/2306.11706"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning <!-- paper:yu2018domainadaptive --> | <a href="https://arxiv.org/abs/1802.01557"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| One-Shot Visual Imitation Learning via Meta-Learning <!-- paper:finn2017mil --> | <a href="https://arxiv.org/abs/1709.04905"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
