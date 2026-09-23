# 基于世界模型的控制

[← 分类首页](../README_zh-CN.md) · [English](world.md)

预训练与参数更新工作在相应分支中列出，作为对照。

按首次公开时间倒序。论文链接优先使用 arXiv，缺省时使用正式出版页；`—` 表示暂无已核实的官方代码链接。

## 分类导航

- [示范条件未来生成](#futures)
- [预测规划、记忆与恢复](#planning)
- [模型适应与自我改进](#update)

<a id="futures"></a>

## 示范条件未来生成

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| TADreamer: Zero-Shot Language-Guided 3D Navigation for Terrestrial-Aerial Bimodal Robots via Video Imagination <!-- paper:arxiv260919824 --> | <a href="https://arxiv.org/abs/2609.19824"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Memory as Plans: World-Action Modeling with Memory-Grounded Planning <!-- paper:extra260911561 --> | <a href="https://arxiv.org/abs/2609.11561"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/aipixel/MaP-WAM) |
| Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization <!-- paper:zhou2026zerowam --> | <a href="https://arxiv.org/abs/2608.26103"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/robbyant-research/Zero-WAM) |
| HOST: Robots Acquire Manipulation Skills in Seconds from a Single Human Video <!-- paper:chen2026host --> | <a href="https://arxiv.org/abs/2607.20033"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/CGuangyan-BIT/HOST) |
| WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory <!-- paper:arxiv260718840 --> | <a href="https://arxiv.org/abs/2607.18840"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Retrieve, Don&#x27;t Retrain: Extending Vision Language Action Models to New Tasks at Test Time <!-- paper:park2026recap --> | <a href="https://arxiv.org/abs/2606.15631"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/jeongeun980906/ReCAP-Cosmos-Policy) |
| VICX: Generalizable Robot Manipulation via Video Generation and In-Context Operator Network <!-- paper:extra260612028 --> | <a href="https://arxiv.org/abs/2606.12028"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation <!-- paper:he2026demojepa --> | <a href="https://arxiv.org/abs/2605.20811"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation <!-- paper:goswami2025osviwm --> | <a href="https://arxiv.org/abs/2505.20425"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/raktimgg/osvi-wm) |
| Human2Robot: Learning Robot Actions from Paired Human-Robot Videos <!-- paper:extra250216587 --> | <a href="https://arxiv.org/abs/2502.16587"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="planning"></a>

## 预测规划、记忆与恢复

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning <!-- paper:arxiv260919315 --> | <a href="https://arxiv.org/abs/2609.19315"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Causal-History Test-Time Scaling for Failure Recovery in Autoregressive World-Action Models <!-- paper:extra260918016 --> | <a href="https://arxiv.org/abs/2609.18016"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| τ₀-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation <!-- paper:arxiv260816885 --> | <a href="https://arxiv.org/abs/2608.16885"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/sii-research/tau-0-vla) |
| Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models <!-- paper:core2026realignment --> | <a href="https://arxiv.org/abs/2608.14822"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models <!-- paper:shi2026memoryvlapp --> | <a href="https://arxiv.org/abs/2606.09827"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/shihao1895/MemoryVLA) |
| MetaDiffuser: Diffusion Model as Conditional Planner for Offline Meta-RL <!-- paper:ni2023metadiffuser --> | <a href="https://arxiv.org/abs/2305.19923"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Decomposed Mutual Information Optimization for Generalized Context in Meta-Reinforcement Learning <!-- paper:mu2022domino --> | <a href="https://arxiv.org/abs/2210.04209"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Robustness via Retrying: Closed-Loop Robotic Manipulation with Self-Supervised Learning <!-- paper:ebert2018retrying --> | <a href="https://arxiv.org/abs/1810.03043"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/febert/robustness_via_retrying) |
| Universal Planning Networks <!-- paper:srinivas2018upn --> | <a href="https://arxiv.org/abs/1804.00645"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="update"></a>

## 模型适应与自我改进

| 论文标题 | 论文 | 代码 |
| :--- | :---: | :---: |
| Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models <!-- paper:arxiv260921740 --> | <a href="https://arxiv.org/abs/2609.21740"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| MetaPusher: Meta Learning and Planning for Nonprehensile Manipulation of Unseen Objects with Rapid Online Adaption <!-- paper:arxiv260921122 --> | <a href="https://arxiv.org/abs/2609.21122"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning <!-- paper:extra260912278 --> | <a href="https://arxiv.org/abs/2609.12278"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Motus2: A Self-Evolving General World Model for Dexterous Manipulation <!-- paper:bi2026motus2 --> | <a href="https://arxiv.org/abs/2608.30237"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time <!-- paper:arxiv260706988 --> | <a href="https://arxiv.org/abs/2607.06988"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| Self-Improving Loops for Visual Robotic Planning <!-- paper:luo2025silvr --> | <a href="https://arxiv.org/abs/2506.06658"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code ↗](https://github.com/brown-palm/silvr) |
