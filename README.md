# Robot In-Context Learning

An awesome list of **in-context learning for robotics**.

[简体中文](README_zh-CN.md) · [Papers](#papers) · [Data](#data) · [Benchmarks](#benchmarks) · [Data notes](notes/reproducibility.md)

<a id="papers"></a>

## Papers

Years refer to the first preprint.

### From human video

| Work | Main idea | Resources |
| --- | --- | --- |
| **[Zero-WAM](https://arxiv.org/abs/2608.26103)** · 2026<br>[![arXiv 2608.26103](https://img.shields.io/badge/arXiv-2608.26103-b31b1b)](https://arxiv.org/abs/2608.26103) | Human `prompt_video` → future robot frames and actions. | [Project](https://robbyant-research.github.io/Zero-WAM/) · [Code](https://github.com/robbyant-research/Zero-WAM) · [Pretrained weights](https://huggingface.co/robbyant-research/zero-wam-pretrain) · [RoboTwin weights](https://huggingface.co/robbyant-research/zero-wam-posttrain-robotwin) |
| **[HOST](https://arxiv.org/abs/2607.20033)** · 2026<br>[![arXiv 2607.20033](https://img.shields.io/badge/arXiv-2607.20033-b31b1b)](https://arxiv.org/abs/2607.20033) | Align task progress, predict robot futures, decode actions. | [Code](https://github.com/CGuangyan-BIT/HOST) · [Weights](https://huggingface.co/Guangyan/HOST) |
| **[ViVLA](https://arxiv.org/abs/2512.07582)** · 2025<br>[![arXiv 2512.07582](https://img.shields.io/badge/arXiv-2512.07582-b31b1b)](https://arxiv.org/abs/2512.07582) | Train on expert–agent pairs for video-conditioned action prediction. | — |
| **[MimicDroid](https://arxiv.org/abs/2509.09769)** · 2025<br>[![arXiv 2509.09769](https://img.shields.io/badge/arXiv-2509.09769-b31b1b)](https://arxiv.org/abs/2509.09769) | Mine human-play pairs; retarget wrist motion for supervision. | [Benchmark](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) · [Data](https://huggingface.co/datasets/Rutav/MimicDroidDataset) |
| **[RHyME](https://arxiv.org/abs/2409.06615)** · 2024<br>[![arXiv 2409.06615](https://img.shields.io/badge/arXiv-2409.06615-b31b1b)](https://arxiv.org/abs/2409.06615) | Retrieve and compose demonstration clips for robot trajectories. | [Code](https://github.com/portal-cornell/rhyme) · [Sim data](https://huggingface.co/datasets/prithwishdan/RHyME) |
| **[Vid2Robot](https://www.roboticsproceedings.org/rss20/p052.html)** · 2024<br>[![arXiv 2403.12943](https://img.shields.io/badge/arXiv-2403.12943-b31b1b)](https://arxiv.org/abs/2403.12943) | Cross-attention from `prompt_video` and current observations to actions. | [Project](https://vid2robot.github.io/) |

### From instrumented demonstrations

| Work | Demonstration input | Main idea / resources |
| --- | --- | --- |
| **[BPP](https://arxiv.org/abs/2606.30457)** · 2026<br>[![arXiv 2606.30457](https://img.shields.io/badge/arXiv-2606.30457-b31b1b)](https://arxiv.org/abs/2606.30457) | iPhUMI sensorimotor demonstration | Demonstration-conditioned manipulation. [Code](https://github.com/real-stanford/behavior_prompting) |
| **[RICL](https://proceedings.mlr.press/v305/sridhar25a.html)** · 2025<br>[![arXiv 2508.02062](https://img.shields.io/badge/arXiv-2508.02062-b31b1b)](https://arxiv.org/abs/2508.02062) | Retrieved robot demonstrations | Add context conditioning to a pretrained VLA; uses 10–20 target-task demos. [Code](https://github.com/ricl-vla/ricl_openpi) |
| **[Instant Policy](https://arxiv.org/abs/2411.12633)** · 2024<br>[![arXiv 2411.12633](https://img.shields.io/badge/arXiv-2411.12633-b31b1b)](https://arxiv.org/abs/2411.12633) | Point clouds + gripper poses/states | Graph diffusion trained on pseudo-demonstrations. [Code](https://github.com/vv19/instant_policy) |
| **[ICRT](https://arxiv.org/abs/2408.15980)** · 2024<br>[![arXiv 2408.15980](https://img.shields.io/badge/arXiv-2408.15980-b31b1b)](https://arxiv.org/abs/2408.15980) | Robot observations + states + actions | Next-token prediction over demonstration and execution sequences. [Code](https://github.com/Max-Fu/icrt) · [Data](https://huggingface.co/datasets/Ravenh97/ICRT-MT) |

### From interaction — and the TTT boundary

| Work | What changes at test time? | Main idea / resources |
| --- | --- | --- |
| **[Zeva](https://arxiv.org/abs/2608.30880)** · 2026<br>[![arXiv 2608.30880](https://img.shields.io/badge/arXiv-2608.30880-b31b1b)](https://arxiv.org/abs/2608.30880) | External memory; policy frozen | Retrieve action-induced state changes across attempts. [Code](https://github.com/air-embodied-brain/Zeva) |
| **[LocoFormer](https://proceedings.mlr.press/v305/liu25a.html)** · 2025<br>[![arXiv 2509.23745](https://img.shields.io/badge/arXiv-2509.23745-b31b1b)](https://arxiv.org/abs/2509.23745) | Interaction context | Long-context adaptation for locomotion. [Project](https://generalist-locomotion.github.io/) |
| **[RoboTTT](https://arxiv.org/abs/2607.15275)** · 2026<br>[![arXiv 2607.15275](https://img.shields.io/badge/arXiv-2607.15275-b31b1b)](https://arxiv.org/abs/2607.15275) | Fast weights, through gradients | Compress long visuomotor histories into adaptive memory. [Project](https://research.nvidia.com/labs/gear/robottt/) |
| **[WAM-TTT](https://arxiv.org/abs/2607.06988)** · 2026<br>[![arXiv 2607.06988](https://img.shields.io/badge/arXiv-2607.06988-b31b1b)](https://arxiv.org/abs/2607.06988) | Lightweight memory, through gradients | Adapt a frozen WAM by predicting human-video dynamics. |

<details>
<summary>Earlier work and other approaches — 52 papers</summary>

### Foundations

- **[One-Shot Imitation Learning](https://papers.nips.cc/paper/2017/hash/ba3866600c3540f67c1e9575e213be0a-Abstract.html)** · 2017 — Demonstration-pair training. [![arXiv 1703.07326](https://img.shields.io/badge/arXiv-1703.07326-b31b1b)](https://arxiv.org/abs/1703.07326)
- **[MOSAIC](https://arxiv.org/abs/2110.13423)** · 2021 — Attention and temporal contrastive learning. [Code](https://github.com/rll-research/mosaic) [![arXiv 2110.13423](https://img.shields.io/badge/arXiv-2110.13423-b31b1b)](https://arxiv.org/abs/2110.13423)
- **[BC-Z](https://proceedings.mlr.press/v164/jang22a.html)** · 2022 — Language- or human-video-conditioned policies. [Project](https://sites.google.com/view/bc-z/home) [![arXiv 2202.02005](https://img.shields.io/badge/arXiv-2202.02005-b31b1b)](https://arxiv.org/abs/2202.02005)
- **[VIMA](https://proceedings.mlr.press/v202/jiang23b.html)** · 2022 — Multimodal task specifications. [Code](https://github.com/vimalabs/VIMA) [![arXiv 2210.03094](https://img.shields.io/badge/arXiv-2210.03094-b31b1b)](https://arxiv.org/abs/2210.03094)

### More demonstration-conditioned policies

- **[MINT](https://www.roboticsproceedings.org/rss22/p206.html)** · 2026 — MINT-Zero injects coarse intent tokens from one robot action demonstration, then predicts finer execution tokens without test-time fine-tuning. [Code](https://github.com/RenMing-Huang/MINT) · [Transfer weights](https://huggingface.co/huangrm/MINT-light-zero) [![arXiv 2602.08602](https://img.shields.io/badge/arXiv-2602.08602-b31b1b)](https://arxiv.org/abs/2602.08602)
- **[ICI-VLA](https://arxiv.org/abs/2609.07581)** · 2026 — Retrieve phase-aligned robot micro-demonstrations for a fixed text-action VLA; train with action-prefix masking. [![arXiv 2609.07581](https://img.shields.io/badge/arXiv-2609.07581-b31b1b)](https://arxiv.org/abs/2609.07581)
- **[ContextFlow](https://arxiv.org/abs/2609.06852)** · 2026 — Compress robot RGB, state, and action demonstrations to condition continuous action chunks through flow matching. [Project](https://dingjiansw101.github.io/contextflow-page/) · [Code](https://github.com/dingjiansw101/ContextFlow) · [Data](https://huggingface.co/datasets/vo2yager/aloha_incontext) [![arXiv 2609.06852](https://img.shields.io/badge/arXiv-2609.06852-b31b1b)](https://arxiv.org/abs/2609.06852)
- **[ReCAP](https://arxiv.org/abs/2606.15631)** · 2026 — Condition a frozen WAM on retrieved cross-embodiment state–action chunks; add tasks by extending the demonstration pool. [Project](https://recap-robot.github.io/) [![arXiv 2606.15631](https://img.shields.io/badge/arXiv-2606.15631-b31b1b)](https://arxiv.org/abs/2606.15631)
- **[SynthICL](https://arxiv.org/abs/2606.08154)** · 2026 — Synthetic demonstrations for RGB-based flow policies. [![arXiv 2606.08154](https://img.shields.io/badge/arXiv-2606.08154-b31b1b)](https://arxiv.org/abs/2606.08154)
- **[Instant-Fold](https://arxiv.org/abs/2606.04269)** · 2026 — RGB-D demonstration conditioning for cloth folding. [Project](https://instant-fold.github.io/) [![arXiv 2606.04269](https://img.shields.io/badge/arXiv-2606.04269-b31b1b)](https://arxiv.org/abs/2606.04269)
- **[HiST-AT](https://arxiv.org/abs/2604.15215)** · 2026 — Hierarchical action tokenization. [![arXiv 2604.15215](https://img.shields.io/badge/arXiv-2604.15215-b31b1b)](https://arxiv.org/abs/2604.15215)
- **[ICLR](https://arxiv.org/abs/2603.07530)** · 2026 — Visual reasoning traces and action prediction. [![arXiv 2603.07530](https://img.shields.io/badge/arXiv-2603.07530-b31b1b)](https://arxiv.org/abs/2603.07530)
- **[RoboSSM](https://arxiv.org/abs/2509.19658)** · 2025 — Recurrently encode robot RGB and proprioceptive demonstrations with Longhorn for action prediction without test-time weight updates. [Code](https://github.com/youngjuY/RoboSSM) [![arXiv 2509.19658](https://img.shields.io/badge/arXiv-2509.19658-b31b1b)](https://arxiv.org/abs/2509.19658)
- **[Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt](https://arxiv.org/abs/2505.20795)** · 2025 — Cross-prediction pretraining and shared action representations. [![arXiv 2505.20795](https://img.shields.io/badge/arXiv-2505.20795-b31b1b)](https://arxiv.org/abs/2505.20795)
- **[Human2Robot](https://arxiv.org/abs/2502.16587)** · 2025 — Paired human–robot videos and decoupled action decoding. [Data](https://huggingface.co/datasets/dannyXSC/HumanAndRobot) [![arXiv 2502.16587](https://img.shields.io/badge/arXiv-2502.16587-b31b1b)](https://arxiv.org/abs/2502.16587)
- **[XSkill](https://arxiv.org/abs/2307.09955)** · 2023 — Cross-embodiment skill discovery and composition. [Code](https://github.com/real-stanford/xskill) [![arXiv 2307.09955](https://img.shields.io/badge/arXiv-2307.09955-b31b1b)](https://arxiv.org/abs/2307.09955)

### Structured transfer and replay

- **[V2-STRep](https://arxiv.org/abs/2609.20582)** · 2026 — Extract motion phases and geometric constraints from generated videos, then transfer object motion through RGB-D grounding and trajectory optimization. [![arXiv 2609.20582](https://img.shields.io/badge/arXiv-2609.20582-b31b1b)](https://arxiv.org/abs/2609.20582)
- **[GPT-Policy](https://arxiv.org/abs/2609.19138)** · 2026 — Condition a fixed VLM on demonstration frames and interaction feedback to issue Cartesian robot-tool commands. [Project](https://cheng-haha.github.io/GPT-Policy/) · [Code preview](https://github.com/cheng-haha/GPT-Policy) [![arXiv 2609.19138](https://img.shields.io/badge/arXiv-2609.19138-b31b1b)](https://arxiv.org/abs/2609.19138)
- **[VLBiMan++](https://arxiv.org/abs/2609.14310)** · 2026 — Geometrically adapt and recompose skills from one kinesthetic dual-arm demonstration, using recorded end-effector poses and gripper states without policy retraining. [Project](https://hnuzhy.github.io/projects/VLBiManPlus) · [Code](https://github.com/hnuzhy/BiRoMan) [![arXiv 2609.14310](https://img.shields.io/badge/arXiv-2609.14310-b31b1b)](https://arxiv.org/abs/2609.14310)
- **[Show-Harness](https://arxiv.org/abs/2609.10522)** · 2026 — Convert demonstration video into a task outline; execute through semantic motion units and embodiment-specific interpreters. [Project](https://showlab.github.io/Show-Harness/) · [Code](https://github.com/showlab/Show-Harness) · [Adapters](https://huggingface.co/showlab/Show-Harness-VLMs) · [Data](https://huggingface.co/datasets/showlab/Show-Harness-Data) [![arXiv 2609.10522](https://img.shields.io/badge/arXiv-2609.10522-b31b1b)](https://arxiv.org/abs/2609.10522)
- **[CFAM](https://arxiv.org/abs/2609.04552)** · 2026 — Geometrically adapt stored skill capsules and retain verified within-family variations without updating the backbone. [![arXiv 2609.04552](https://img.shields.io/badge/arXiv-2609.04552-b31b1b)](https://arxiv.org/abs/2609.04552)
- **[StellaVLA](https://arxiv.org/abs/2608.11671)** · 2026 — Retrieve structured plans and motion descriptions. [![arXiv 2608.11671](https://img.shields.io/badge/arXiv-2608.11671-b31b1b)](https://arxiv.org/abs/2608.11671)
- **[ManiLong-Shot](https://ojs.aaai.org/index.php/AAAI/article/view/38881)** · 2025 — Interaction primitives and geometric matching. [Project](https://sites.google.com/view/manilong-shot) [![arXiv 2512.16302](https://img.shields.io/badge/arXiv-2512.16302-b31b1b)](https://arxiv.org/abs/2512.16302)
- **[Robust Instant Policy](https://arxiv.org/abs/2506.15157)** · 2025 — Robust aggregation of LLM-generated trajectories. [![arXiv 2506.15157](https://img.shields.io/badge/arXiv-2506.15157-b31b1b)](https://arxiv.org/abs/2506.15157)
- **[R+X](https://arxiv.org/abs/2407.12957)** · 2024 — Human-video retrieval with a keypoint action interface. [Code](https://github.com/gpapagiannis/r-plus-x-hand2actions) [![arXiv 2407.12957](https://img.shields.io/badge/arXiv-2407.12957-b31b1b)](https://arxiv.org/abs/2407.12957)
- **[ORION](https://link.springer.com/article/10.1007/s10514-026-10253-8)** · 2024 — Object-graph plans from a human demonstration. [Project](https://ut-austin-rpl.github.io/ORION-release/) [![arXiv 2405.20321](https://img.shields.io/badge/arXiv-2405.20321-b31b1b)](https://arxiv.org/abs/2405.20321)
- **[RoboPrompt](https://arxiv.org/abs/2410.12782)** · 2024 — Encode object poses and keyframe actions as text examples for a frozen LLM. [Code](https://github.com/davidyyd/roboprompt) [![arXiv 2410.12782](https://img.shields.io/badge/arXiv-2410.12782-b31b1b)](https://arxiv.org/abs/2410.12782)
- **[Keypoint Action Tokens](https://arxiv.org/abs/2403.19578)** · 2024 — Keypoints and actions as context for an LLM. [Project](https://www.robot-learning.uk/keypoint-action-tokens) [![arXiv 2403.19578](https://img.shields.io/badge/arXiv-2403.19578-b31b1b)](https://arxiv.org/abs/2403.19578)
- **[DOME](https://arxiv.org/abs/2204.02863)** · 2022 — Visual servoing followed by motion replay. [Project](https://www.robot-learning.uk/dome) [![arXiv 2204.02863](https://img.shields.io/badge/arXiv-2204.02863-b31b1b)](https://arxiv.org/abs/2204.02863)
- **[Coarse-to-Fine Imitation](https://arxiv.org/abs/2105.06411)** · 2021 — Reach an interaction bottleneck, then replay. [Project](https://www.robot-learning.uk/coarse-to-fine-imitation-learning) [![arXiv 2105.06411](https://img.shields.io/badge/arXiv-2105.06411-b31b1b)](https://arxiv.org/abs/2105.06411)

### Adaptation and adjacent work

- **[TraceFlow](https://arxiv.org/abs/2609.20646)** · 2026 — Guide a frozen flow-matching policy with progress-aligned success and failure action traces; expand the trace bank using binary rollout outcomes. [![arXiv 2609.20646](https://img.shields.io/badge/arXiv-2609.20646-b31b1b)](https://arxiv.org/abs/2609.20646)
- **[Learning and Transferring Closed-Loop Robot Software](https://arxiv.org/abs/2609.19906)** · 2026 — Reuse execution-improved robot programs as examples for new RoboCasa tasks; revise target controllers from demonstrations and feedback, then freeze them for execution. [![arXiv 2609.19906](https://img.shields.io/badge/arXiv-2609.19906-b31b1b)](https://arxiv.org/abs/2609.19906)
- **[FaRe](https://arxiv.org/abs/2609.18016)** · 2026 — Compare full, recovered-prefix, and reset KV histories to recover a frozen autoregressive WAM from stalled execution. [![arXiv 2609.18016](https://img.shields.io/badge/arXiv-2609.18016-b31b1b)](https://arxiv.org/abs/2609.18016)
- **[WetRobo](https://arxiv.org/abs/2609.18435)** · 2026 — Supply robot demonstrations and a lab-control kit for coding agents to revise and retain site-specific manipulation programs. [Code](https://github.com/tsudalab/WetRobo) [![arXiv 2609.18435](https://img.shields.io/badge/arXiv-2609.18435-b31b1b)](https://arxiv.org/abs/2609.18435)
- **[TEMPO](https://arxiv.org/abs/2609.16864)** · 2026 — Fine-tune a VLA with motion features from a frozen video encoder and compressed robot action history for dynamic manipulation. [Project](https://tempo-robot.github.io/) · [Code](https://github.com/tempo-robot/TEMPO) [![arXiv 2609.16864](https://img.shields.io/badge/arXiv-2609.16864-b31b1b)](https://arxiv.org/abs/2609.16864)
- **[MessyMem](https://arxiv.org/abs/2609.15976)** · 2026 — Update a persistent 3D scene graph with interaction outcomes and linked keyframes; retrieve this memory across tasks to plan over existing motion primitives. [Project](https://messymem.github.io/) [![arXiv 2609.15976](https://img.shields.io/badge/arXiv-2609.15976-b31b1b)](https://arxiv.org/abs/2609.15976)
- **[CLAW](https://arxiv.org/abs/2609.12278)** · 2026 — Generate world-model LoRA adapters from interaction transitions without test-time gradients, changing effective weights over a frozen base. [![arXiv 2609.12278](https://img.shields.io/badge/arXiv-2609.12278-b31b1b)](https://arxiv.org/abs/2609.12278)
- **[SafeMem](https://arxiv.org/abs/2609.08444)** · 2026 — Retain an RGB-D scene graph across observations to detect out-of-view hazards and replan over a fixed robot skill library. [Project](https://sites.google.com/view/safemem) · [Code](https://github.com/lty759/SafeMem) [![arXiv 2609.08444](https://img.shields.io/badge/arXiv-2609.08444-b31b1b)](https://arxiv.org/abs/2609.08444)
- **[WIZARD](https://arxiv.org/abs/2606.07217)** · 2026 — Generate task-specific VLA LoRA weights from language and robot demonstration video, without target-task action labels or test-time gradients. [Project](https://Fascetta.github.io/WIZARD/) [![arXiv 2606.07217](https://img.shields.io/badge/arXiv-2606.07217-b31b1b)](https://arxiv.org/abs/2606.07217)
- **[2AM](https://arxiv.org/abs/2609.11308)** · 2026 — Convert agent-side history into subtask language and 2D grasp, place, and motion hints for an action policy without episodic memory. [![arXiv 2609.11308](https://img.shields.io/badge/arXiv-2609.11308-b31b1b)](https://arxiv.org/abs/2609.11308)
- **[MaP-WAM](https://arxiv.org/abs/2609.11561)** · 2026 — Turn episodic memory into language–visual plans; execute with fixed-length context and progress-based replanning. [Project](https://sizhezhao.github.io/projects/MaP-WAM/) [![arXiv 2609.11561](https://img.shields.io/badge/arXiv-2609.11561-b31b1b)](https://arxiv.org/abs/2609.11561)
- **[UniMPA](https://arxiv.org/abs/2609.11875)** · 2026 — Retrieve action prototypes to initialize flow matching, then refine them using predicted transition features. [Project](https://jiutian-vl.github.io/UniMPA-page/) [![arXiv 2609.11875](https://img.shields.io/badge/arXiv-2609.11875-b31b1b)](https://arxiv.org/abs/2609.11875)
- **[SimpleMemVLA](https://arxiv.org/abs/2609.05533)** · 2026 — Use timestamped video history as native context; generated subtask representations condition a flow-matching action head. [Code](https://github.com/wadeKeith/SimpleMemVLA) [![arXiv 2609.05533](https://img.shields.io/badge/arXiv-2609.05533-b31b1b)](https://arxiv.org/abs/2609.05533)
- **[AGM](https://arxiv.org/abs/2608.29537)** · 2026 — Use verified grasp and placement outcomes to advance or roll back task-progress memory around a frozen VLA. [![arXiv 2608.29537](https://img.shields.io/badge/arXiv-2608.29537-b31b1b)](https://arxiv.org/abs/2608.29537)
- **[CorrectVLA](https://arxiv.org/abs/2608.29967)** · 2026 — Translate task-level language feedback into time-localized action biases for a frozen VLA. [![arXiv 2608.29967](https://img.shields.io/badge/arXiv-2608.29967-b31b1b)](https://arxiv.org/abs/2608.29967)
- **[ICWM](https://arxiv.org/abs/2606.26025)** · 2026 — Infer the control setup from task-agnostic observation–action transitions, without test-time weight updates. [![arXiv 2606.26025](https://img.shields.io/badge/arXiv-2606.26025-b31b1b)](https://arxiv.org/abs/2606.26025)
- **[WHIRL](https://arxiv.org/abs/2207.09450)** · 2022 — Human-video initialization, then online robot optimization. [Project](https://human2robot.github.io/) [![arXiv 2207.09450](https://img.shields.io/badge/arXiv-2207.09450-b31b1b)](https://arxiv.org/abs/2207.09450)
- **[DAML](https://www.roboticsproceedings.org/rss14/p02.html)** · 2018 — Gradient-based adaptation from human video. [![arXiv 1802.01557](https://img.shields.io/badge/arXiv-1802.01557-b31b1b)](https://arxiv.org/abs/1802.01557)
- **[One-Shot Visual Imitation via Meta-Learning](https://proceedings.mlr.press/v78/finn17a.html)** · 2017 — Gradient-based meta-imitation. [![arXiv 1709.04905](https://img.shields.io/badge/arXiv-1709.04905-b31b1b)](https://arxiv.org/abs/1709.04905)
- **[VICX](https://arxiv.org/abs/2606.12028)** · 2026 — Ground generated visual plans using retrieved image–state pairs. [Project](https://scaling-group.github.io/vicx/) [![arXiv 2606.12028](https://img.shields.io/badge/arXiv-2606.12028-b31b1b)](https://arxiv.org/abs/2606.12028)
- **[Video In-context Learning](https://arxiv.org/abs/2407.07356)** · 2024 — Video imitation; no executable action output. [![arXiv 2407.07356](https://img.shields.io/badge/arXiv-2407.07356-b31b1b)](https://arxiv.org/abs/2407.07356)
- **[MimicPlay](https://arxiv.org/abs/2302.12422)** · 2023 — Human-play intent with robot low-level control. [Code](https://github.com/j96w/MimicPlay) [![arXiv 2302.12422](https://img.shields.io/badge/arXiv-2302.12422-b31b1b)](https://arxiv.org/abs/2302.12422)

</details>

**Industry:** [Skild S1](https://skild.ai/blogs/s1) — video-conditioned, no fine-tuning. [GEN-1.5](https://generalistai.com/blog/gen-1.5) — sensorimotor examples; reports both ICL and gradient adaptation. Architecture details remain limited.

<a id="data"></a>

## Data

For human-video ICL: **human `prompt_video` + robot RGB/state + aligned robot action targets**.

| Resource | Useful for | Notes |
| --- | --- | --- |
| [H&R](https://huggingface.co/datasets/dannyXSC/HumanAndRobot) | Human–robot video pairs | v1 `/action` is human-hand pose, not executed robot action. |
| [RH20T](https://rh20t.github.io/) | Human demos + robot trajectories | Task correspondence, not framewise human–robot synchronization. |
| [MIME](https://sites.google.com/view/mimedataset/home) | Human demos + Baxter trajectories | Legacy platform and data format. |
| [DROID](https://droid-dataset.github.io/) / [AgiBot World](https://huggingface.co/datasets/agibot-world/AgiBotWorld-Alpha) | Robot query-side RGB/actions | Human `prompt_video` must be sourced separately. |
| [ICRT-MT](https://huggingface.co/datasets/Ravenh97/ICRT-MT) | Robot-demo/query experiments | Robot demonstrations, not human video. |
| [UMI](https://umi-gripper.github.io/) / [iPhUMI](https://github.com/real-stanford/iPhUMI) | Instrumented human demonstrations | Handheld grippers, not bare-hand video. |

<details>
<summary>More data resources</summary>

- [HuRo](https://3587jjh.github.io/HuRo/) — human videos converted into rendered robot observations and retargeted action targets for VLA pretraining; pipeline code released, full dataset forthcoming. [Code](https://github.com/3587jjh/HuRo) [![arXiv 2609.10706](https://img.shields.io/badge/arXiv-2609.10706-b31b1b)](https://arxiv.org/abs/2609.10706)
- [ContextFlow ALOHA](https://huggingface.co/datasets/vo2yager/aloha_incontext) — teleoperated robot demonstrations for in-context single-arm and bimanual manipulation.
- [MimicDroid](https://huggingface.co/datasets/Rutav/MimicDroidDataset) — retargeted action supervision.
- [RHyME](https://huggingface.co/datasets/prithwishdan/RHyME) — simulation pairs.
- [BC-Z](https://sites.google.com/view/bc-z/home) — task-level human-video conditioning.
- [Open X-Embodiment](https://robotics-transformer-x.github.io/) / [RoboMIND](https://x-humanoid-robomind.github.io/) — multi-embodiment robot data.
- [HumanEgo](https://huggingface.co/datasets/Leo-TX/HumanEgo) — human video only.
- [HumanGen](https://huggingface.co/datasets/robbyant-research/HumanGen) — synthesized human videos paired with robot RGB/actions and precomputed video latents; RoboTwin and five external-source subsets released. [Data guide](https://github.com/robbyant-research/Zero-WAM#humangen-data)

</details>

<a id="benchmarks"></a>

## Benchmarks

- [VA-Bench](https://arxiv.org/abs/2609.19554) · 2026 — 14 simulated manipulation tasks using RGB robot-demonstration summaries, active viewpoints, and metric commands; includes execution and recovery diagnostics. [Code](https://github.com/zhangzhongbo2213/VABench) [![arXiv 2609.19554](https://img.shields.io/badge/arXiv-2609.19554-b31b1b)](https://arxiv.org/abs/2609.19554)
- [RoboReel](https://roboreel.github.io/) · 2026 — real human videos paired with simulated robot trajectories across 10 tasks and four evaluation suites; code and data forthcoming. [![arXiv 2609.08209](https://img.shields.io/badge/arXiv-2609.08209-b31b1b)](https://arxiv.org/abs/2609.08209)
- [MEMOBench](https://github.com/Collab-Gen/MEMOBench) · 2026 — 30 history-dependent tasks with 4,200 checkpoints for memory storage, update, and compression. [Data](https://huggingface.co/datasets/SunSeaLucky/MEMOBench) [![arXiv 2609.07047](https://img.shields.io/badge/arXiv-2609.07047-b31b1b)](https://arxiv.org/abs/2609.07047)
- [BPP: LIBERO / LIBERO-Gen / DrawAnything](https://github.com/real-stanford/behavior_prompting) — demonstration-conditioned evaluation.
- [RoboTwin 2.0](https://robotwin-platform.github.io/) / [MimicDroid](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) / [VIMA-Bench](https://vimalabs.github.io/) — task and environment generalization.
- [Zeva Atomic5 & PIM](https://github.com/air-embodied-brain/Zeva) — frozen-policy evaluation and separate cross-attempt case studies.

## Related lists

[Embodied ICL](https://github.com/asimfish/awesome_ICL) · [ICL in Robot](https://github.com/BraveBoBo/awesome-in-context-learning--in-robot) · [Test-Time Robot Learning](https://github.com/Oliverbansk/Awesome-Test-Time-Robot-Learning) · [Learning from Human Videos](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos) · [WAM](https://github.com/OpenMOSS/Awesome-WAM) · [In-Context RL](https://github.com/dunnolab/awesome-in-context-rl)

[Contribute](CONTRIBUTING.md) · [MIT](LICENSE) · Updated 2026-09-19. Linked resources retain their own licenses.
