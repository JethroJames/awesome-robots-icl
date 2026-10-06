# World-model-based control

[← All categories](../README.md) · [简体中文](world.zh-CN.md)

Pretrained and parameter-updating methods appear in the corresponding branches for comparison.

First public release, newest first; year only where the month is unavailable. Paper links point to arXiv or the original source.

## Browse

- [Demonstration-conditioned future generation](#futures)
- [Predictive planning, memory, and recovery](#planning)
- [Model adaptation and self-improvement](#update)

<a id="futures"></a>

## Demonstration-conditioned future generation

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑10 | Keep the Effect, Drop the Actor: Programmable Effect-to-Execution World-Action Models <!-- paper:arxiv261002398 --> | <a href="https://arxiv.org/abs/2610.02398"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | [In-context Robot Learning Made Simple: A Democratized Recipe for Manipulation Tasks](https://simpleicl.github.io/simpleicl/) <!-- paper:arxiv260938173 --> | <a href="https://arxiv.org/abs/2609.38173"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | TADreamer: Zero-Shot Language-Guided 3D Navigation for Terrestrial-Aerial Bimodal Robots via Video Imagination <!-- paper:arxiv260919824 --> | <a href="https://arxiv.org/abs/2609.19824"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Memory as Plans: World-Action Modeling with Memory-Grounded Planning <!-- paper:extra260911561 --> | <a href="https://arxiv.org/abs/2609.11561"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/aipixel/MaP-WAM) |
| 2026‑08 | Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization <!-- paper:zhou2026zerowam --> | <a href="https://arxiv.org/abs/2608.26103"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/robbyant-research/Zero-WAM) |
| 2026‑07 | HOST: Robots Acquire Manipulation Skills in Seconds from a Single Human Video <!-- paper:chen2026host --> | <a href="https://arxiv.org/abs/2607.20033"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/CGuangyan-BIT/HOST) |
| 2026‑07 | WorldScape Policy 2.0: Empowering Steerable World Action Modeling with Reasoning-Augmented Memory <!-- paper:arxiv260718840 --> | <a href="https://arxiv.org/abs/2607.18840"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | Retrieve, Don&#x27;t Retrain: Extending Vision Language Action Models to New Tasks at Test Time <!-- paper:park2026recap --> | <a href="https://arxiv.org/abs/2606.15631"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/jeongeun980906/ReCAP-Cosmos-Policy) |
| 2026‑06 | VICX: Generalizable Robot Manipulation via Video Generation and In-Context Operator Network <!-- paper:extra260612028 --> | <a href="https://arxiv.org/abs/2606.12028"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑05 | Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation <!-- paper:he2026demojepa --> | <a href="https://arxiv.org/abs/2605.20811"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑05 | OSVI-WM: One-Shot Visual Imitation for Unseen Tasks using World-Model-Guided Trajectory Generation <!-- paper:goswami2025osviwm --> | <a href="https://arxiv.org/abs/2505.20425"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/raktimgg/osvi-wm) |
| 2025‑02 | Human2Robot: Learning Robot Actions from Paired Human-Robot Videos <!-- paper:extra250216587 --> | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/38086"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | [Code](https://github.com/SII-dannyXSC/Human2Robot) |

<a id="planning"></a>

## Predictive planning, memory, and recovery

World models can take the form of learned predictors or explicit physics simulators. In [SIMPACT](https://simpact-bot.github.io/), a scene reconstructed from RGB-D supports simulated action rollouts; their images and states enter the VLM context to refine candidate plans without additional training. This places simulation in the decision loop, with predicted consequences guiding the next proposal.

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑10 | [Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation](https://dagroup-pku.github.io/ViGAR/) <!-- paper:arxiv261002368 --> | <a href="https://arxiv.org/abs/2610.02368"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/DAGroup-PKU/ViGAR) |
| 2026‑09 | [DeepJEPA: Scaling World Models from Within](https://deepjepa.github.io/) <!-- paper:arxiv261000368 --> | <a href="https://arxiv.org/abs/2610.00368"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Test-Time Spatial Reasoning for Robot Manipulation Using Generative Real-to-Sim <!-- paper:arxiv260933982 --> | <a href="https://arxiv.org/abs/2609.33982"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning <!-- paper:arxiv260919315 --> | <a href="https://arxiv.org/abs/2609.19315"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Causal-History Test-Time Scaling for Failure Recovery in Autoregressive World-Action Models <!-- paper:extra260918016 --> | <a href="https://arxiv.org/abs/2609.18016"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | τ₀-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation <!-- paper:arxiv260816885 --> | <a href="https://arxiv.org/abs/2608.16885"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/sii-research/tau-0-vla) |
| 2026‑08 | Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models <!-- paper:core2026realignment --> | <a href="https://arxiv.org/abs/2608.14822"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models <!-- paper:shi2026memoryvlapp --> | <a href="https://arxiv.org/abs/2606.09827"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/shihao1895/MemoryVLA) |
| 2025‑12 | [SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models](https://simpact-bot.github.io/) (CVPR 2026) <!-- paper:liu2025simpact --> | <a href="https://arxiv.org/abs/2512.05955"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/ShaoxiongYao/simpact) |
| 2023‑05 | MetaDiffuser: Diffusion Model as Conditional Planner for Offline Meta-RL <!-- paper:ni2023metadiffuser --> | <a href="https://arxiv.org/abs/2305.19923"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑10 | Decomposed Mutual Information Optimization for Generalized Context in Meta-Reinforcement Learning <!-- paper:mu2022domino --> | <a href="https://arxiv.org/abs/2210.04209"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2018‑10 | Robustness via Retrying: Closed-Loop Robotic Manipulation with Self-Supervised Learning <!-- paper:ebert2018retrying --> | <a href="https://arxiv.org/abs/1810.03043"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/febert/robustness_via_retrying) |
| 2018‑04 | Universal Planning Networks <!-- paper:srinivas2018upn --> | <a href="https://arxiv.org/abs/1804.00645"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="update"></a>

## Model adaptation and self-improvement

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | [RoboCoach: World Models as Active Coaches for Compositional Robot Skills](https://robocoach-ai.github.io/) <!-- paper:arxiv260939685 --> | <a href="https://arxiv.org/abs/2609.39685"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [CoachWorld code](https://github.com/RoboCoach-AI/CoachWorld) · [Weights](https://huggingface.co/JEdward/CoachWorld) |
| 2026‑09 | Online Sim-to-Real Adaptation via Closed-Loop System Modeling <!-- paper:arxiv260928878 --> | <a href="https://arxiv.org/abs/2609.28878"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models <!-- paper:arxiv260921740 --> | <a href="https://arxiv.org/abs/2609.21740"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | MetaPusher: Meta Learning and Planning for Nonprehensile Manipulation of Unseen Objects with Rapid Online Adaption <!-- paper:arxiv260921122 --> | <a href="https://arxiv.org/abs/2609.21122"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning <!-- paper:extra260912278 --> | <a href="https://arxiv.org/abs/2609.12278"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Motus2: A Self-Evolving General World Model for Dexterous Manipulation <!-- paper:bi2026motus2 --> | <a href="https://arxiv.org/abs/2608.30237"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time <!-- paper:arxiv260706988 --> | <a href="https://arxiv.org/abs/2607.06988"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑06 | Self-Improving Loops for Visual Robotic Planning <!-- paper:luo2025silvr --> | <a href="https://arxiv.org/abs/2506.06658"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/brown-palm/silvr) |
