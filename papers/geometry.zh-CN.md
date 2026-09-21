# 几何示范迁移

[← 分类首页](../README_zh-CN.md) · [English](geometry.md)

预训练与参数更新工作在相应分支中列出，作为对照。

按首次公开时间倒序。论文链接优先使用 arXiv，缺省时使用正式出版页；`—` 表示暂无已核实的官方代码链接。

## 分类导航

- [视觉对齐与参考跟踪](#alignment)
- [轨迹重建与重定向](#retarget)
- [功能对应与物体替换](#functional)
- [多阶段迁移与可复用技能库](#repertoire)

<a id="alignment"></a>

## 视觉对齐与参考跟踪

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| One-Shot Imitation Learning with Invariance Matching for Robotic Manipulation <!-- paper:zhang2024imop --> | <a href="https://arxiv.org/abs/2405.13178"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| One-Shot Imitation Learning: A Pose Estimation Perspective <!-- paper:vitiello2023pose --> | <a href="https://arxiv.org/abs/2310.12077"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation <!-- paper:vecerik2023robotap --> | <a href="https://arxiv.org/abs/2308.15975"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/google-deepmind/tapnet) |
| DINOBot: Robot Manipulation via Retrieval and Alignment with Vision Foundation Models <!-- paper:dipalo2023dinobot --> | <a href="https://arxiv.org/abs/2402.13181"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Demonstrate Once, Imitate Immediately (DOME): Learning Visual Servoing for One-Shot Imitation Learning <!-- paper:valassakis2022dome --> | <a href="https://arxiv.org/abs/2204.02863"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration <!-- paper:extra210506411 --> | <a href="https://arxiv.org/abs/2105.06411"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| FlowControl: Optical Flow Based Visual Servoing <!-- paper:argus2020flowcontrol --> | <a href="https://arxiv.org/abs/2007.00291"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="retarget"></a>

## 轨迹重建与重定向

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| V2-STRep: VLM-Grounded Structured Task Representations for Reusable Robot Skills Acquired from Generated Videos <!-- paper:extra260920582 --> | <a href="https://arxiv.org/abs/2609.20582"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Demonstrate once, execute on many: Kinematic intelligence for cross-robot skill transfer <!-- paper:gupta2026kinematic --> | <a href="https://doi.org/10.1126/scirobotics.aea1995"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| HRT1: One-Shot Human-to-Robot Trajectory Transfer for Mobile Manipulation <!-- paper:allu2025hrt1 --> | <a href="https://arxiv.org/abs/2510.21026"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/IRVLUTD/HRT1) |
| Elastic Motion Policy: An Adaptive Dynamical System for Robust and Efficient One-Shot Imitation Learning <!-- paper:li2025emp --> | <a href="https://arxiv.org/abs/2503.08029"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/penn-figueroa-lab/emp) |
| R+X: Retrieval and Execution from Everyday Human Videos <!-- paper:extra240712957 --> | <a href="https://arxiv.org/abs/2407.12957"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/gpapagiannis/r-plus-x-hand2actions) |
| ScrewMimic: Bimanual Imitation from Human Videos with Screw Space Projection <!-- paper:bahety2024screwmimic --> | <a href="https://arxiv.org/abs/2405.03666"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/UT-Austin-RobIn/ScrewMimic) |
| DITTO: Demonstration Imitation by Trajectory Transformation <!-- paper:heppert2024ditto --> | <a href="https://arxiv.org/abs/2403.15203"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/robot-learning-freiburg/DITTO) |
| One-shot Imitation Learning via Interaction Warping <!-- paper:biza2023warping --> | <a href="https://arxiv.org/abs/2306.12392"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="functional"></a>

## 功能对应与物体替换

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Sparse Meets Dense: Correspondence Guided Robotic Manipulation with Rigid-Deformable Interactions <!-- paper:zhu2026sparsedense --> | <a href="https://arxiv.org/abs/2608.01083"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| SemAnCorr: Semantic Anchored Correspondence for Zero-Shot Manipulation Skill Transfer <!-- paper:dong2026semancorr --> | <a href="https://arxiv.org/abs/2607.28382"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/semancorr/SemAnCorr) |
| One-Shot Cross-Geometry Skill Transfer through Part Decomposition <!-- paper:thompson2026parttransfer --> | <a href="https://arxiv.org/abs/2604.15455"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| GIFT: Geometry-Induced Functional Transfer for Category-level Object Manipulation <!-- paper:defarias2025gift --> | <a href="https://arxiv.org/abs/2503.15371"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| FUNCTO: Function-Centric One-Shot Imitation Learning for Tool Manipulation <!-- paper:tang2025functo --> | <a href="https://arxiv.org/abs/2502.11744"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| One-Shot Manipulation Strategy Learning by Making Contact Analogies <!-- paper:liu2024magic --> | <a href="https://arxiv.org/abs/2411.09627"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/nature21/magic) |
| SE(3)-Equivariant Relational Rearrangement with Neural Descriptor Fields <!-- paper:simeonov2023rndf --> | <a href="https://arxiv.org/abs/2211.09786"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/anthonysimeonov/relational_ndf) |

<a id="repertoire"></a>

## 多阶段迁移与可复用技能库

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| VLBiMan++: Expanding the Generalization Boundary of Vision-Language Anchored One-Shot Bimanual Manipulation <!-- paper:extra260914310 --> | <a href="https://arxiv.org/abs/2609.14310"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/hnuzhy/BiRoMan) |
| Continual Field-Adaptive Models (CFAMs) for Post-Deployment Physical AI <!-- paper:extra260904552 --> | <a href="https://arxiv.org/abs/2609.04552"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation <!-- paper:chen2025manilong --> | <a href="https://arxiv.org/abs/2512.16302"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Learning a Thousand Tasks in a Day <!-- paper:dreczkowski2025mt3 --> | <a href="https://arxiv.org/abs/2511.10110"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/kamil-dreczkowski/learning_thousand_tasks) |
| Annotation-Free One-Shot Imitation Learning for Multi-Step Manipulation Tasks <!-- paper:wichitwechkarn2025annotationfree --> | <a href="https://arxiv.org/abs/2509.24972"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| One-Shot Dual-Arm Imitation Learning <!-- paper:wang2025odil --> | <a href="https://arxiv.org/abs/2503.06831"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/kelthuzadyl/ODIL) |
