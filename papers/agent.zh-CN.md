# 基于技能与智能体的执行

[← 分类首页](../README_zh-CN.md) · [English](agent.md)

预训练与参数更新工作在相应分支中列出，作为对照。

按首次公开时间倒序。论文链接优先使用 arXiv，缺省时使用正式出版页；`—` 表示暂无已核实的官方代码链接。

## 分类导航

- [技能序列与任务结构](#skills)
- [程序、工具与分层控制](#programs)
- [保留指导与知识复用](#memory)
- [落地执行、反馈与失败恢复](#grounding)
- [智能体驱动学习与自我改进](#improvement)

<a id="skills"></a>

## 技能序列与任务结构

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation <!-- paper:arxiv260920791 --> | <a href="https://arxiv.org/abs/2609.20791"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations <!-- paper:kim2025uniskill --> | <a href="https://arxiv.org/abs/2505.08787"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/KimHanjung/UniSkill) |
| Enabling Long(er) Horizon Imitation for Manipulation Tasks by Modeling Subgoal Transitions <!-- paper:jain2025transitions --> | <a href="https://proceedings.mlr.press/v305/jain25b.html"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | [Code ↗](https://github.com/shivam89jain/SGPT-long-horizon-imitation) |
| Vision-based Manipulation from Single Human Video with Open-World Object Graphs <!-- paper:zhu2024orion --> | <a href="https://arxiv.org/abs/2405.20321"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| XSkill: Cross Embodiment Skill Discovery <!-- paper:xu2023xskill --> | <a href="https://arxiv.org/abs/2307.09955"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/real-stanford/xskill) |
| MimicPlay: Long-Horizon Imitation Learning by Watching Human Play <!-- paper:wang2023mimicplay --> | <a href="https://arxiv.org/abs/2302.12422"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/j96w/MimicPlay) |
| One-shot Visual Imitation via Attributed Waypoints and Demonstration Augmentation <!-- paper:chang2023awda --> | <a href="https://arxiv.org/abs/2302.04856"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/MatthewChang/osvi-awda) |
| Neural Task Programming: Learning to Generalize Across Hierarchical Tasks <!-- paper:xu2017ntp --> | <a href="https://arxiv.org/abs/1710.01813"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/StanfordVL/ntp) |

<a id="programs"></a>

## 程序、工具与分层控制

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control <!-- paper:arxiv260919554 --> | <a href="https://arxiv.org/abs/2609.19554"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/zhangzhongbo2213/VABench) |
| Navi-Agent: Unlocalized Monocular Navigation Agent <!-- paper:arxiv260920388 --> | <a href="https://arxiv.org/abs/2609.20388"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories <!-- paper:extra260918435 --> | <a href="https://arxiv.org/abs/2609.18435"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/tsudalab/WetRobo) |
| In-Context Robot Learning with VLM Agents <!-- paper:cheng2026gptpolicyeval --> | <a href="https://arxiv.org/abs/2609.19138"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/cheng-haha/GPT-Policy) |
| Show-Harness: Just a VLM Agent Can Play Robots <!-- paper:chen2026showharness --> | <a href="https://arxiv.org/abs/2609.10522"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/showlab/Show-Harness) |
| ETA: A New Agentic Paradigm for Embodied Tasks <!-- paper:chen2026eta --> | <a href="https://arxiv.org/abs/2608.03924"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/OpenMOSS/OpenETA) |
| A Few Words Go a Long Way: Language Guided Robot Policy Synthesis <!-- paper:chen2026architect --> | <a href="https://arxiv.org/abs/2607.23784"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/robo-architect/architect-franka) |
| Addressing the Orchestration Gap in Generalist Robots via Physical Agency <!-- paper:galanti2026physicalagency --> | <a href="https://arxiv.org/abs/2607.21725"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents <!-- paper:arxiv260708448 --> | <a href="https://arxiv.org/abs/2607.08448"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/RLinf/RPent) |
| What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents <!-- paper:hu2026orchestrating --> | <a href="https://arxiv.org/abs/2606.10267"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution <!-- paper:arxiv260514504 --> | <a href="https://arxiv.org/abs/2605.14504"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation <!-- paper:arxiv260322435 --> | <a href="https://arxiv.org/abs/2603.22435"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks <!-- paper:cui2026roboclaw --> | <a href="https://arxiv.org/abs/2603.11558"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/RoboClaw-Robotics/RoboClaw) |
| Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control <!-- paper:chen2026steerable --> | <a href="https://arxiv.org/abs/2602.13193"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/steerable-policies/steerable-policies-bridge) |
| MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation <!-- paper:singh2024malmm --> | <a href="https://arxiv.org/abs/2411.17636"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Select2Plan: Training-Free ICL-Based Planning Through VQA and Memory Retrieval <!-- paper:buoso2024select2plan --> | <a href="https://arxiv.org/abs/2411.04006"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/lambdavi/S2P) |
| Trust the PRoC3S: Solving Long-Horizon Robotics Problems with LLMs and Constraint Satisfaction <!-- paper:curtis2025proc3s --> | <a href="https://arxiv.org/abs/2406.05572"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/Learning-and-Intelligent-Systems/proc3s) |
| VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models <!-- paper:huang2023voxposer --> | <a href="https://arxiv.org/abs/2307.05973"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/huangwl18/VoxPoser) |
| SayTap: Language to Quadrupedal Locomotion <!-- paper:tang2023saytap --> | <a href="https://arxiv.org/abs/2306.07580"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| ProgPrompt: Generating Situated Robot Task Plans using Large Language Models <!-- paper:singh2022progprompt --> | <a href="https://arxiv.org/abs/2209.11302"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/NVlabs/progprompt-vh) |
| Code as Policies: Language Model Programs for Embodied Control <!-- paper:liang2022codeaspolicies --> | <a href="https://arxiv.org/abs/2209.07753"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/google-research/google-research/tree/master/code_as_policies) |
| Inner Monologue: Embodied Reasoning through Planning with Language Models <!-- paper:huang2022monologue --> | <a href="https://arxiv.org/abs/2207.05608"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Do As I Can, Not As I Say: Grounding Language in Robotic Affordances <!-- paper:ahn2022saycan --> | <a href="https://arxiv.org/abs/2204.01691"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/google-research/google-research/tree/master/saycan) |

<a id="memory"></a>

## 保留指导与知识复用

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Learning and Transferring Closed-Loop Robot Software <!-- paper:arxiv260919906 --> | <a href="https://arxiv.org/abs/2609.19906"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| CoreSense: Traceable Failure Recall and Conflict-Aware Belief Gating for Auditable Robot Decisions <!-- paper:arxiv260919512 --> | <a href="https://arxiv.org/abs/2609.19512"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| MessyMem: Learning-from-Doing Memory for Mobile Manipulation <!-- paper:extra260915976 --> | <a href="https://arxiv.org/abs/2609.15976"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation <!-- paper:extra260911308 --> | <a href="https://arxiv.org/abs/2609.11308"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Safe Task Planning with Long-Term Graph Memory for Embodied Agents <!-- paper:extra260908444 --> | <a href="https://arxiv.org/abs/2609.08444"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/lty759/SafeMem) |
| AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies <!-- paper:arxiv260829537 --> | <a href="https://arxiv.org/abs/2608.29537"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning <!-- paper:huang2026roboharness --> | <a href="https://arxiv.org/abs/2607.18060"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| ASPIRE: Agentic /Skills Discovery for Robotics <!-- paper:lu2026aspire --> | <a href="https://arxiv.org/abs/2607.00272"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/NVlabs/ASPIRE) |
| Guava: An Effective and Universal Harness for Embodied Manipulation <!-- paper:liu2026guava --> | <a href="https://arxiv.org/abs/2606.18363"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents <!-- paper:ju2026embodiskill --> | <a href="https://arxiv.org/abs/2605.10332"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation <!-- paper:xie2026uniskillrepo --> | <a href="https://arxiv.org/abs/2603.02623"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation <!-- paper:kumar2026aor --> | <a href="https://arxiv.org/abs/2603.04466"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills <!-- paper:arxiv250918597 --> | <a href="https://arxiv.org/abs/2509.18597"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models <!-- paper:tziafas2024lrll --> | <a href="https://arxiv.org/abs/2406.18746"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought <!-- paper:sarch2024ical --> | <a href="https://arxiv.org/abs/2406.14596"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/Gabesarch/ICAL) |
| Learning to Learn Faster from Human Feedback with Language Model Predictive Control <!-- paper:liang2024lmpc --> | <a href="https://arxiv.org/abs/2402.11450"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections <!-- paper:zha2023droc --> | <a href="https://arxiv.org/abs/2311.10678"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/Stanford-ILIAD/droc) |

<a id="grounding"></a>

## 落地执行、反馈与失败恢复

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Training-Free Action Correction for VLA Model Failures via Language Feedback <!-- paper:arxiv260829967 --> | <a href="https://arxiv.org/abs/2608.29967"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/owenk3/correct_vla) |
| PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration <!-- paper:physcap2026 --> | <a href="https://arxiv.org/abs/2608.21031"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents <!-- paper:arxiv260817129 --> | <a href="https://arxiv.org/abs/2608.17129"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation <!-- paper:chen2026volo --> | <a href="https://arxiv.org/abs/2606.07723"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/NVlabs/VoLoAgent) |
| Where to Look: Can Foundation Models Reach a Target Viewpoint Through Active Exploration? <!-- paper:arxiv260601247 --> | <a href="https://arxiv.org/abs/2606.01247"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/aim-uofa/TVRBench) |
| From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation <!-- paper:arxiv260511951 --> | <a href="https://arxiv.org/abs/2605.11951"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/EDEM-AI/AgentChord) |
| In-Context Iterative Policy Improvement for Dynamic Manipulation <!-- paper:merwe2025icpi --> | <a href="https://arxiv.org/abs/2508.15021"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| In-situ Value-aligned Human-Robot Interactions with Physical Constraints <!-- paper:li2025iclhf --> | <a href="https://arxiv.org/abs/2508.07606"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/ICLHF/ICLHF) |
| VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments <!-- paper:elnoor2024vlmgronav --> | <a href="https://arxiv.org/abs/2409.20445"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| RACER: Rich Language-Guided Failure Recovery Policies for Imitation Learning <!-- paper:dai2024racer --> | <a href="https://arxiv.org/abs/2409.14674"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/sled-group/RACER) |
| Introspective Planning: Aligning Robots&#x27; Uncertainty with Inherent Task Ambiguity <!-- paper:liang2024introplan --> | <a href="https://arxiv.org/abs/2402.06529"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/kevinliang888/IntroPlan) |
| Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners <!-- paper:ren2023knowno --> | <a href="https://arxiv.org/abs/2307.01928"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/google-research/google-research/tree/master/language_model_uncertainty) |
| REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction <!-- paper:liu2023reflect --> | <a href="https://arxiv.org/abs/2306.15724"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/columbia-ai-robotics/reflect) |

<a id="improvement"></a>

## 智能体驱动学习与自我改进

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention <!-- paper:arxiv260914633 --> | <a href="https://arxiv.org/abs/2609.14633"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| RoboRSI: Stable, Efficient, and Reusable Robot Self-Evolution in Complex Real-World Environments <!-- paper:noematrix2026roborsi --> | <a href="https://lab.noematrix.ai/blog/2-roborsi/"><img src="https://img.shields.io/badge/Research_Blog-52616b.svg?style=flat-square" alt="Research_Blog" height="24"></a> | [Code ↗](https://github.com/nssmd/RoboRSI) |
| SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies <!-- paper:arxiv260831167 --> | <a href="https://arxiv.org/abs/2608.31167"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| EXIMO: VLM Guided Exploration of VLA Policies <!-- paper:arxiv260819891 --> | <a href="https://arxiv.org/abs/2608.19891"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence <!-- paper:arxiv260816590 --> | <a href="https://arxiv.org/abs/2608.16590"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Teach and Grow: An Agent-Centered Architecture for General Robot Learning <!-- paper:arxiv260817209 --> | <a href="https://arxiv.org/abs/2608.17209"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/IRMVLab/TGL) |
| Self-Evolving Embodied Agents via Skill-Harness Evolution <!-- paper:wang2026shaper --> | <a href="https://arxiv.org/abs/2608.11350"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| ENPIRE: Agentic Robot Policy Self-Improvement in the Real World <!-- paper:xiao2026enpire --> | <a href="https://arxiv.org/abs/2606.19980"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Playful Agentic Robot Learning <!-- paper:arxiv260619419 --> | <a href="https://arxiv.org/abs/2606.19419"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/Playful-RATs/rats) |
| AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents <!-- paper:ahn2024autort --> | <a href="https://arxiv.org/abs/2401.12963"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
