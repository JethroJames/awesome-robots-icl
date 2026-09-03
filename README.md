# Robot In-Context Learning

An awesome list of **in-context learning for robotics**.

[简体中文](README_zh-CN.md) · [Papers](#papers) · [Data](#data) · [Benchmarks](#benchmarks) · [Data notes](notes/reproducibility.md)

<a id="papers"></a>

## Papers

Years refer to the first preprint.

### From human video

| Work | Main idea | Resources |
| --- | --- | --- |
| **[Zero-WAM](https://arxiv.org/abs/2608.26103)** · 2026<br>[![arXiv 2608.26103](https://img.shields.io/badge/arXiv-2608.26103-b31b1b)](https://arxiv.org/abs/2608.26103) | Human `prompt_video` → future robot frames and actions. | [Project](https://robbyant-research.github.io/Zero-WAM/) · [Release plan](https://github.com/robbyant-research/Zero-WAM) |
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
<summary>Earlier work and other approaches — 25 papers</summary>

### Foundations

- **[One-Shot Imitation Learning](https://papers.nips.cc/paper/2017/hash/ba3866600c3540f67c1e9575e213be0a-Abstract.html)** · 2017 — Demonstration-pair training. [![arXiv 1703.07326](https://img.shields.io/badge/arXiv-1703.07326-b31b1b)](https://arxiv.org/abs/1703.07326)
- **[MOSAIC](https://arxiv.org/abs/2110.13423)** · 2021 — Attention and temporal contrastive learning. [Code](https://github.com/rll-research/mosaic) [![arXiv 2110.13423](https://img.shields.io/badge/arXiv-2110.13423-b31b1b)](https://arxiv.org/abs/2110.13423)
- **[BC-Z](https://proceedings.mlr.press/v164/jang22a.html)** · 2022 — Language- or human-video-conditioned policies. [Project](https://sites.google.com/view/bc-z/home) [![arXiv 2202.02005](https://img.shields.io/badge/arXiv-2202.02005-b31b1b)](https://arxiv.org/abs/2202.02005)
- **[VIMA](https://proceedings.mlr.press/v202/jiang23b.html)** · 2022 — Multimodal task specifications. [Code](https://github.com/vimalabs/VIMA) [![arXiv 2210.03094](https://img.shields.io/badge/arXiv-2210.03094-b31b1b)](https://arxiv.org/abs/2210.03094)

### More demonstration-conditioned policies

- **[SynthICL](https://arxiv.org/abs/2606.08154)** · 2026 — Synthetic demonstrations for RGB-based flow policies. [![arXiv 2606.08154](https://img.shields.io/badge/arXiv-2606.08154-b31b1b)](https://arxiv.org/abs/2606.08154)
- **[Instant-Fold](https://arxiv.org/abs/2606.04269)** · 2026 — RGB-D demonstration conditioning for cloth folding. [Project](https://instant-fold.github.io/) [![arXiv 2606.04269](https://img.shields.io/badge/arXiv-2606.04269-b31b1b)](https://arxiv.org/abs/2606.04269)
- **[HiST-AT](https://arxiv.org/abs/2604.15215)** · 2026 — Hierarchical action tokenization. [![arXiv 2604.15215](https://img.shields.io/badge/arXiv-2604.15215-b31b1b)](https://arxiv.org/abs/2604.15215)
- **[ICLR](https://arxiv.org/abs/2603.07530)** · 2026 — Visual reasoning traces and action prediction. [![arXiv 2603.07530](https://img.shields.io/badge/arXiv-2603.07530-b31b1b)](https://arxiv.org/abs/2603.07530)
- **[Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt](https://arxiv.org/abs/2505.20795)** · 2025 — Cross-prediction pretraining and shared action representations. [![arXiv 2505.20795](https://img.shields.io/badge/arXiv-2505.20795-b31b1b)](https://arxiv.org/abs/2505.20795)
- **[Human2Robot](https://arxiv.org/abs/2502.16587)** · 2025 — Paired human–robot videos and decoupled action decoding. [Data](https://huggingface.co/datasets/dannyXSC/HumanAndRobot) [![arXiv 2502.16587](https://img.shields.io/badge/arXiv-2502.16587-b31b1b)](https://arxiv.org/abs/2502.16587)
- **[XSkill](https://arxiv.org/abs/2307.09955)** · 2023 — Cross-embodiment skill discovery and composition. [Code](https://github.com/real-stanford/xskill) [![arXiv 2307.09955](https://img.shields.io/badge/arXiv-2307.09955-b31b1b)](https://arxiv.org/abs/2307.09955)

### Structured transfer and replay

- **[StellaVLA](https://arxiv.org/abs/2608.11671)** · 2026 — Retrieve structured plans and motion descriptions. [![arXiv 2608.11671](https://img.shields.io/badge/arXiv-2608.11671-b31b1b)](https://arxiv.org/abs/2608.11671)
- **[ManiLong-Shot](https://arxiv.org/abs/2512.16302)** · 2025 — Interaction primitives and geometric matching. [Project](https://sites.google.com/view/manilong-shot) [![arXiv 2512.16302](https://img.shields.io/badge/arXiv-2512.16302-b31b1b)](https://arxiv.org/abs/2512.16302)
- **[Robust Instant Policy](https://arxiv.org/abs/2506.15157)** · 2025 — Robust aggregation of LLM-generated trajectories. [![arXiv 2506.15157](https://img.shields.io/badge/arXiv-2506.15157-b31b1b)](https://arxiv.org/abs/2506.15157)
- **[R+X](https://arxiv.org/abs/2407.12957)** · 2024 — Human-video retrieval with a keypoint action interface. [Code](https://github.com/gpapagiannis/r-plus-x-hand2actions) [![arXiv 2407.12957](https://img.shields.io/badge/arXiv-2407.12957-b31b1b)](https://arxiv.org/abs/2407.12957)
- **[ORION](https://link.springer.com/article/10.1007/s10514-026-10253-8)** · 2024 — Object-graph plans from a human demonstration. [Project](https://ut-austin-rpl.github.io/ORION-release/) [![arXiv 2405.20321](https://img.shields.io/badge/arXiv-2405.20321-b31b1b)](https://arxiv.org/abs/2405.20321)
- **[Keypoint Action Tokens](https://arxiv.org/abs/2403.19578)** · 2024 — Keypoints and actions as context for an LLM. [Project](https://www.robot-learning.uk/keypoint-action-tokens) [![arXiv 2403.19578](https://img.shields.io/badge/arXiv-2403.19578-b31b1b)](https://arxiv.org/abs/2403.19578)
- **[DOME](https://arxiv.org/abs/2204.02863)** · 2022 — Visual servoing followed by motion replay. [Project](https://www.robot-learning.uk/dome) [![arXiv 2204.02863](https://img.shields.io/badge/arXiv-2204.02863-b31b1b)](https://arxiv.org/abs/2204.02863)
- **[Coarse-to-Fine Imitation](https://arxiv.org/abs/2105.06411)** · 2021 — Reach an interaction bottleneck, then replay. [Project](https://www.robot-learning.uk/coarse-to-fine-imitation-learning) [![arXiv 2105.06411](https://img.shields.io/badge/arXiv-2105.06411-b31b1b)](https://arxiv.org/abs/2105.06411)

### Adaptation and adjacent work

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

- [MimicDroid](https://huggingface.co/datasets/Rutav/MimicDroidDataset) — retargeted action supervision.
- [RHyME](https://huggingface.co/datasets/prithwishdan/RHyME) — simulation pairs.
- [BC-Z](https://sites.google.com/view/bc-z/home) — task-level human-video conditioning.
- [Open X-Embodiment](https://robotics-transformer-x.github.io/) / [RoboMIND](https://x-humanoid-robomind.github.io/) — multi-embodiment robot data.
- [HumanEgo](https://huggingface.co/datasets/Leo-TX/HumanEgo) — human video only.
- [HumanGen](https://github.com/robbyant-research/Zero-WAM) — announced; data release pending.

</details>

<a id="benchmarks"></a>

## Benchmarks

- [BPP: LIBERO / LIBERO-Gen / DrawAnything](https://github.com/real-stanford/behavior_prompting) — demonstration-conditioned evaluation.
- [RoboTwin 2.0](https://robotwin-platform.github.io/) / [MimicDroid](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) / [VIMA-Bench](https://vimalabs.github.io/) — task and environment generalization.
- [Zeva Atomic5 & PIM](https://github.com/air-embodied-brain/Zeva) — frozen-policy evaluation and separate cross-attempt case studies.

## Related lists

[Embodied ICL](https://github.com/asimfish/awesome_ICL) · [ICL in Robot](https://github.com/BraveBoBo/awesome-in-context-learning--in-robot) · [Test-Time Robot Learning](https://github.com/Oliverbansk/Awesome-Test-Time-Robot-Learning) · [Learning from Human Videos](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos) · [WAM](https://github.com/OpenMOSS/Awesome-WAM) · [In-Context RL](https://github.com/dunnolab/awesome-in-context-rl)

[Contribute](CONTRIBUTING.md) · [MIT](LICENSE) · Updated 2026-09-03. Linked resources retain their own licenses.
