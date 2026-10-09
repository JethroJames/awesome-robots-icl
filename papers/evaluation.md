# Benchmarks and evaluation

[← All categories](../README.md) · [简体中文](evaluation.zh-CN.md)

First public release, newest first; year only where the month is unavailable. Paper links point to arXiv or the original source.

## Browse

- [Demonstration use and task transfer](#transfer)
- [Memory and physical adaptation](#memory)
- [Physical execution and predictive evaluation](#execution)

<a id="transfer"></a>

## Demonstration use and task transfer

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑10 | Encoded but Not in Control: Revealing the Grounding Gap in Vision-Language Robot Policies <!-- paper:arxiv261006235 --> | <a href="https://arxiv.org/abs/2610.06235"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑10 | When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models <!-- paper:arxiv261005492 --> | <a href="https://arxiv.org/abs/2610.05492"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents <!-- paper:arxiv260925636 --> | <a href="https://arxiv.org/abs/2609.25636"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/AutoLab-SAI-SJTU/RoboFollow) |
| 2026‑09 | H2RBench: A Real-to-Sim Benchmark for Evaluating Human-to-Robot Transfer <!-- paper:arxiv260924778 --> | <a href="https://arxiv.org/abs/2609.24778"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/xiaochy/H2RBench) |
| 2026‑09 | Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation <!-- paper:gu2026roboreel --> | <a href="https://arxiv.org/abs/2609.08209"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks <!-- paper:arxiv260830536 --> | <a href="https://arxiv.org/abs/2608.30536"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/nubot-nudt/Behavior-Skill) |
| 2026‑08 | The Imitator Game: Benchmarking Robot Imitative Ability Beyond Action Prediction <!-- paper:zhou2026imitator --> | <a href="https://arxiv.org/abs/2608.22301"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/imitator-game/The-Imitator-Game) |
| 2026‑06 | What Are We Actually Benchmarking in Robot Manipulation? <!-- paper:jiang2026benchmarkaudit --> | <a href="https://arxiv.org/abs/2606.04233"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/ripl/ManipulationBenchmarkAudit) |
| 2026‑06 | RoboSemanticBench: Diagnosing Semantic Grounding in Action Prediction for VLA Models <!-- paper:arxiv260602277 --> | <a href="https://arxiv.org/abs/2606.02277"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/ZGC-EmbodyAI/RoboSemanticBench) |
| 2026‑03 | ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies <!-- paper:arxiv260317300 --> | <a href="https://arxiv.org/abs/2603.17300"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑02 | When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs <!-- paper:arxiv260217659 --> | <a href="https://arxiv.org/abs/2602.17659"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/yuffish/LIBERO-CF) |
| 2025‑10 | LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models <!-- paper:fei2025liberoplus --> | <a href="https://arxiv.org/abs/2510.13626"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑10 | LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization <!-- paper:zhou2025liberopro --> | <a href="https://arxiv.org/abs/2510.03827"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Zxy-MLlab/LIBERO-PRO) |
| 2025‑06 | RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation <!-- paper:chen2025robotwin2 --> | <a href="https://arxiv.org/abs/2506.18088"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/RoboTwin-Platform/RoboTwin) |
| 2025‑05 | On Path to Multimodal Generalist: General-Level and General-Bench <!-- paper:fei2025generallevel --> | <a href="https://arxiv.org/abs/2505.04620"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑12 | LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations <!-- paper:ruoss2025lmact --> | <a href="https://arxiv.org/abs/2412.01441"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/google-deepmind/lm_act) |
| 2023‑06 | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning <!-- paper:liu2023libero --> | <a href="https://arxiv.org/abs/2306.03310"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| 2023‑02 | ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills <!-- paper:gu2023maniskill2 --> | <a href="https://arxiv.org/abs/2302.04659"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/haosulab/ManiSkill2) |
| 2019‑10 | Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning <!-- paper:yu2019metaworld --> | <a href="https://arxiv.org/abs/1910.10897"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/rlworkgroup/metaworld) |
| 2019‑09 | RLBench: The Robot Learning Benchmark &amp; Learning Environment <!-- paper:james2019rlbench --> | <a href="https://arxiv.org/abs/1909.12271"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/stepjam/RLBench) |

<a id="memory"></a>

## Memory and physical adaptation

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑10 | [RoboQuest: Generalist Physical Agents that Search, Inspect and Test](https://declare-lab.github.io/RoboQuest/) <!-- paper:arxiv261010388 --> | <a href="https://arxiv.org/abs/2610.10388"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/declare-lab/RoboQuest) · [Data](https://huggingface.co/datasets/declare-lab/RoboQuest) |
| 2026‑10 | Lifelong small-object navigation in changing object layouts: a benchmark and method <!-- paper:arxiv261010125 --> | <a href="https://arxiv.org/abs/2610.10125"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Benchmark code](https://github.com/hhhhhjg/LiSoNav-Benchmark/tree/main) |
| 2026‑10 | Grounded in Time: A Multi-Source Dataset and Benchmark for Temporal Grounding in Robotic Manipulation <!-- paper:arxiv261004255 --> | <a href="https://arxiv.org/abs/2610.04255"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑10 | Watch, Infer, Coordinate: Inferring Robot Partner Constraints for Zero-Shot Coordination <!-- paper:arxiv261002170 --> | <a href="https://arxiv.org/abs/2610.02170"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | [MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation](https://mikasarobo.github.io/) <!-- paper:arxiv261000604 --> | <a href="https://arxiv.org/abs/2610.00604"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/CognitiveAISystems/MIKASA-Robo) · [Data](https://huggingface.co/datasets/mikasa-robo/mikasa-robo-vla-lerobot) |
| 2026‑09 | [Benchmarking and Enhancing Skill-Level Memory for Partially Observable Robotic Manipulation](https://nanamma.github.io/HIDE-SEEK/) <!-- paper:arxiv260938886 --> | <a href="https://arxiv.org/abs/2609.38886"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | MemTransfer: Benchmarking Memory Beyond Matched Experience in Embodied Decision-Making <!-- paper:arxiv260932313 --> | <a href="https://arxiv.org/abs/2609.32313"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Memory That Changes Action Is Not Memory That Guides It: Counterfactual Auditing of History-Conditioned Robot Policies <!-- paper:arxiv260927247 --> | <a href="https://arxiv.org/abs/2609.27247"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation <!-- paper:sun2026memobench --> | <a href="https://arxiv.org/abs/2609.07047"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Collab-Gen/MEMOBench) |
| 2026‑08 | PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments <!-- paper:arxiv260814441 --> | <a href="https://arxiv.org/abs/2608.14441"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/thunlp/PACE-Bench) |
| 2026‑06 | WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents <!-- paper:arxiv260618847 --> | <a href="https://arxiv.org/abs/2606.18847"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](https://proceedings.mlr.press/v306/dai26c.html) (ICML 2026) <!-- paper:dai2026robomme --> | <a href="https://arxiv.org/abs/2603.04639"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/RoboMME/robomme_benchmark) |
| 2025‑02 | Memory, Benchmark &amp; Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning <!-- paper:cherepanov2025mikasa --> | <a href="https://arxiv.org/abs/2502.10550"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/CognitiveAISystems/MIKASA-Robo) |

<a id="execution"></a>

## Physical execution and predictive evaluation

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑10 | RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments <!-- paper:arxiv261010409 --> | <a href="https://arxiv.org/abs/2610.10409"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑10 | BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation <!-- paper:arxiv261007594 --> | <a href="https://arxiv.org/abs/2610.07594"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑10 | Does a Learned Corrector Beat a Simple Retreat? Evidence from a Frozen VLA <!-- paper:arxiv261006921 --> | <a href="https://arxiv.org/abs/2610.06921"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | LIBERO-Agent: Evaluating General-Purpose Agents for Direct Embodied Manipulation <!-- paper:arxiv260939507 --> | <a href="https://arxiv.org/abs/2609.39507"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | CodeActionBench: Evaluating Agentic Code-as-Policy for Embodied Manipulation <!-- paper:arxiv260933807 --> | <a href="https://arxiv.org/abs/2609.33807"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/lyhkk/CodeActionBench) |
| 2026‑09 | Audit Before You Commit: Locating Belief Failures in Active Identification for One-Shot Manipulation <!-- paper:arxiv260930608 --> | <a href="https://arxiv.org/abs/2609.30608"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | GPT-6-Astra Lights Up Embodied Navigation: Evaluation in Zero-Shot Vision-and-Language Navigation in Continuous Environments <!-- paper:arxiv260929861 --> | <a href="https://arxiv.org/abs/2609.29861"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | RoboRecover: Benchmarking Robot Policy Recovery under Execution Deviations <!-- paper:arxiv260928952 --> | <a href="https://arxiv.org/abs/2609.28952"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/RUCKBReasoning/RoboRecover) |
| 2026‑08 | SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation <!-- paper:arxiv260818701 --> | <a href="https://arxiv.org/abs/2608.18701"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories <!-- paper:arxiv260818618 --> | <a href="https://arxiv.org/abs/2608.18618"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models <!-- paper:arxiv260813049 --> | <a href="https://arxiv.org/abs/2608.13049"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | No Place to Hide: Benchmarking Video Hallucination with Background-Controlled Pairs <!-- paper:huang2026vidpairhalluc --> | <a href="https://arxiv.org/abs/2606.31933"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑05 | RoboStressBench: Benchmarking VLM Robustness to Physical Visual Stress in Embodied Scenes <!-- paper:wu2026robostressbench --> | <a href="https://arxiv.org/abs/2606.00828"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑05 | ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop <!-- paper:arxiv260518746 --> | <a href="https://arxiv.org/abs/2605.18746"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/ESI-Bench/ESI-Bench) |
| 2025‑09 | EvoEmpirBench: Dynamic Spatial Reasoning with Agent-ExpVer <!-- paper:arxiv250912718 --> | <a href="https://ojs.aaai.org/index.php/AAAI/article/view/40979"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 2018‑07 | On Evaluation of Embodied Navigation Agents <!-- paper:anderson2018naveval --> | <a href="https://arxiv.org/abs/1807.06757"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
