# Awesome Embodied In-Context Learning

A curated list of embodied in-context learning, with an emphasis on robot manipulation: demonstration-conditioned policies, interaction memory, historical foundations, datasets and benchmarks. Zero-gradient ICL, structured transfer and test-time training are distinguished rather than ranked together.

[简体中文](README_zh-CN.md) · [Reproducibility notes](notes/reproducibility.md) · Updated: 2026-09-03

## Contents

- [Demonstration-conditioned policies](#demo)
- [Interaction-history-conditioned policies](#memory)
- [Structured demonstration transfer](#structured)
- [Historical foundations](#history)
- [Test-time training and online optimization](#adapt)
- [Related video and skill-learning methods](#adjacent)
- [Industrial releases](#industrial)
- [Datasets and collection resources](#datasets)
- [Benchmarks](#benchmarks)
- [Related lists](#related)
- [Contributing](#contributing)

Entries show **first preprint year (or publication year if unavailable) · venue**. Venues follow proceedings, paper metadata or author project pages; unresolved venues are marked. A video demonstration is called `prompt_video`; `human-sensorimotor` additionally carries instrumented motion information. Resource links identify located releases, **not full reproduction guarantees**; an omitted link does not establish absence.

<a id="demo"></a>

## Demonstration-conditioned policies

Policies that infer behavior from demonstrations supplied at deployment. Visual-future prediction is an output-path tag, not a competing definition of ICL.

### 2026

- **[2026 · preprint] Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization** — [Paper](https://arxiv.org/abs/2608.26103) · [Project](https://robbyant-research.github.io/Zero-WAM/) · [Release plan](https://github.com/robbyant-research/Zero-WAM)
  `human-video` `visual-future` · Human video conditions future robot observations and actions; introduces HumanGen pairs and a future-chunk objective. Code, weights and data are planned, not yet released in the checked repository.

- **[2026 · preprint] HOST: Robots Acquire Manipulation Skills in Seconds from a Single Human Video** — [Paper](https://arxiv.org/abs/2607.20033) · [Code](https://github.com/CGuangyan-BIT/HOST) · [Weights](https://huggingface.co/Guangyan/HOST)
  `human-video` `visual-future` · Aligns task progress, predicts the robot's own future observations, then derives actions without task-specific updates.

- **[2026 · preprint] Behavior Prompting Policy: Demonstrations as Prompts for Manipulation** — [Paper](https://arxiv.org/abs/2606.30457) · [Project](https://behavior-prompting.github.io/) · [Code](https://github.com/real-stanford/behavior_prompting)
  `human-sensorimotor` `action-policy` · Conditions a visuomotor policy on one instrumented human demonstration; iPhUMI context is not ordinary camera-only human video.

- **[2026 · preprint] SynthICL: Scalable In-context Imitation Learning with Synthetic Data** — [Paper](https://arxiv.org/abs/2606.08154)
  `RGB-demo` `synthetic-data` · Trains an RGB-based flow-matching imitation policy on synthetic demonstrations with an auxiliary next-subgoal image objective.

- **[2026 · preprint] Instant-Fold: In-Context Imitation Learning for Deformable Object Manipulation** — [Paper](https://arxiv.org/abs/2606.04269) · [Project](https://instant-fold.github.io/)
  `human-demo` `RGB-D` · Uses deformation-aware representations and a demonstration-conditioned flow policy for folding; the project describes RGB-D cloth tokens.

- **[2026 · preprint] A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics** — [Paper](https://arxiv.org/abs/2604.15215)
  `robot-demo` `action-tokens` · HiST-AT studies hierarchical vector quantization and timestamp reconstruction for in-context action representations.

- **[2026 · IROS 2026] ICLR: In-Context Imitation Learning with Visual Reasoning** — [Paper](https://arxiv.org/abs/2603.07530)
  `robot-demo` `visual-future` · Jointly generates visual reasoning traces and low-level actions; ICLR is the method name, not the conference venue.

### 2025

- **[2025 · preprint] See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations** — [Paper](https://arxiv.org/abs/2512.07582)
  `human-video` `action-policy` · ViVLA learns from expert-agent pairs and predicts demonstrated action sequences alongside subsequent robot actions.

- **[2025 · ICRA 2026] MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos** — [Paper](https://arxiv.org/abs/2509.09769) · [Project](https://ut-austin-rpl.github.io/MimicDroid/) · [Benchmark](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) · [Data](https://huggingface.co/datasets/Rutav/MimicDroidDataset)
  `human-video` `retargeting` · Mines similar behavior pairs from human play and retargets wrist poses for action supervision; linked code is the released benchmark.

- **[2025 · CoRL 2025] RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models** — [Paper](https://proceedings.mlr.press/v305/sridhar25a.html) · [Project](https://ricl-vla.github.io/) · [Code](https://github.com/ricl-vla/ricl_openpi)
  `robot-sensorimotor` `retrieval` · Adds ICL to a pretrained VLA through offline retraining and retrieved demonstration segments; the paper uses 10–20 target-task demonstrations, not one-shot.

- **[2025 · ICRA 2026] Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt** — [Paper](https://arxiv.org/abs/2505.20795)
  `human-video` `shared-representation` · Combines cross-prediction video pretraining with a shared action representation for adaptation without target-task fine-tuning.

- **[2025 · AAAI 2026] Human2Robot: Learning Robot Actions from Paired Human-Robot Videos** — [Paper](https://arxiv.org/abs/2502.16587) · [Data](https://huggingface.co/datasets/dannyXSC/HumanAndRobot)
  `human-video` `visual-future` · Uses synchronized H&R videos to learn human-conditioned robot dynamics with a decoupled action decoder.

### 2024

- **[2024 · ICLR 2025] Instant Policy: In-Context Imitation Learning via Graph Diffusion** — [Paper](https://arxiv.org/abs/2411.12633) · [Project](https://www.robot-learning.uk/instant-policy) · [Code](https://github.com/vv19/instant_policy)
  `robot-sensorimotor` `point-cloud` · Learns graph-diffusion imitation from simulated pseudo-demonstrations; deployment consumes segmented point clouds, gripper poses and states.

- **[2024 · ICRA 2025] One-Shot Imitation under Mismatched Execution** — [Paper](https://arxiv.org/abs/2409.06615) · [Project](https://portal.cs.cornell.edu/rhyme/) · [Code](https://github.com/portal-cornell/rhyme) · [Data](https://huggingface.co/datasets/prithwishdan/RHyME)
  `human-video` `pseudo-pairing` · RHyME retrieves and composes demonstrator clips for robot trajectories using optimal transport; the linked dataset release is simulation-focused.

- **[2024 · ICRA 2025] In-Context Imitation Learning via Next-Token Prediction** — [Paper](https://arxiv.org/abs/2408.15980) · [Project](https://icrt.dev/) · [Code](https://github.com/Max-Fu/icrt) · [Data](https://huggingface.co/datasets/Ravenh97/ICRT-MT)
  `robot-sensorimotor` `action-policy` · ICRT predicts actions from robot observation, proprioception and action sequences with demonstration trajectories in context.

- **[2024 · RSS 2024] Vid2Robot: End-to-End Video-Conditioned Policy Learning with Cross-Attention Transformers** — [Paper](https://www.roboticsproceedings.org/rss20/p052.html) · [Project](https://vid2robot.github.io/)
  `human-video` `action-policy` · Cross-attention maps a demonstration video and current robot observations directly to actions.

### 2023

- **[2023 · CoRL 2023] XSkill: Cross Embodiment Skill Discovery** — [Paper](https://arxiv.org/abs/2307.09955) · [Project](https://xskill.cs.columbia.edu/) · [Code](https://github.com/real-stanford/xskill)
  `human-video` `skill-composition` · Discovers cross-embodiment skill prototypes from unlabelled videos, then composes skills according to a human demonstration.


<a id="memory"></a>

## Interaction-history-conditioned policies

Policies that adapt through accumulated execution context. Updating an external memory does not necessarily update neural parameters.

- **[2026 · preprint] Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation** — [Paper](https://arxiv.org/abs/2608.30880) · [Project](https://air-embodied-brain.github.io/Zeva/) · [Code](https://github.com/air-embodied-brain/Zeva)
  `interaction-history` `external-memory` · A frozen policy retrieves action-induced state changes from within- and cross-attempt memory; this is not camera-only human-video imitation.

- **[2025 · CoRL 2025] LocoFormer: Generalist Locomotion via Long-context Adaptation** — [Paper](https://proceedings.mlr.press/v305/liu25a.html) · [Project](https://generalist-locomotion.github.io/)
  `interaction-history` `locomotion` · A long-context locomotion policy adapts across episode boundaries and robot morphologies; included as a non-manipulation control precedent.


<a id="structured"></a>

## Structured demonstration transfer

Methods that explicitly transform, retrieve or replay demonstration structure. Retrieval also appears in learned policies above; this section emphasizes the structured execution interface.

- **[2026 · preprint] StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models** — [Paper](https://arxiv.org/abs/2608.11671)
  `structured-demo` `action-policy` · Converts trajectories offline into plans, subgoals and verbalized motion, then conditions the action expert on a retrieved structured example.

- **[2025 · AAAI 2026] ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation** — [Paper](https://arxiv.org/abs/2512.16302) · [Proceedings](https://ojs.aaai.org/index.php/AAAI/article/download/38881/42843) · [Project](https://sites.google.com/view/manilong-shot)
  `structured-demo` `geometry` · Decomposes demonstrations into interaction primitives and matches invariant regions to compute end-effector targets.

- **[2025 · preprint] Robust Instant Policy: Leveraging Student's t-Regression Model for Robust In-context Imitation Learning of Robot Manipulation** — [Paper](https://arxiv.org/abs/2506.15157)
  `structured-demo` `LLM` · Aggregates candidate LLM trajectories with Student's t-regression to reduce outlier actions; distinct from graph-diffusion Instant Policy.

- **[2024 · ICRA 2025] R+X: Retrieval and Execution from Everyday Human Videos** — [Paper](https://arxiv.org/abs/2407.12957) · [Code](https://github.com/gpapagiannis/r-plus-x-hand2actions)
  `human-video` `retrieval` · Retrieves relevant clips from everyday human video and transfers them through the KAT structured action interface.

- **[2024 · Autonomous Robots 2026] Vision-based Manipulation from Single Human Video with Open-World Object Graphs** — [Paper](https://link.springer.com/article/10.1007/s10514-026-10253-8) · [Project](https://ut-austin-rpl.github.io/ORION-release/)
  `human-video` `object-graph` · ORION extracts object-centric manipulation plans from a single RGB or RGB-D human demonstration.

- **[2024 · RSS 2024] Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics** — [Paper](https://arxiv.org/abs/2403.19578) · [Project](https://www.robot-learning.uk/keypoint-action-tokens)
  `structured-demo` `LLM` · KAT tokenizes visual keypoints and action trajectories for a text-pretrained transformer, without further model training.

- **[2022 · IROS 2022] Demonstrate Once, Imitate Immediately (DOME): Learning Visual Servoing for One-Shot Imitation Learning** — [Paper](https://arxiv.org/abs/2204.02863) · [Project](https://www.robot-learning.uk/dome)
  `robot-demo` `trajectory-replay` · Combines learned segmentation and visual servoing with replay of demonstrated end-effector velocities.

- **[2021 · ICRA 2021] Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration** — [Paper](https://arxiv.org/abs/2105.06411) · [Project](https://www.robot-learning.uk/coarse-to-fine-imitation-learning)
  `robot-demo` `trajectory-replay` · Reaches a visually estimated interaction bottleneck pose, then replays the demonstrated fine-motion velocities.


<a id="history"></a>

## Historical foundations

Selected precursors to current demonstration-conditioned policies; not every multimodal task interface is human-video ICL.

- **[2022 · ICML 2023] VIMA: Robot Manipulation with Multimodal Prompts** — [Paper](https://proceedings.mlr.press/v202/jiang23b.html) · [Project](https://vimalabs.github.io/) · [Code](https://github.com/vimalabs/VIMA)
  `multimodal-context` `simulation` · Unifies task specification through interleaved text and visual tokens; a multimodal-conditioning precursor, not exclusively human-video ICL.

- **[2022 · CoRL 2021] BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning** — [Paper](https://proceedings.mlr.press/v164/jang22a.html) · [Project](https://sites.google.com/view/bc-z/home)
  `human-video` `task-embedding` · Conditions a multi-task robot policy on language or human-video embeddings; an early large-scale task-conditioning baseline.

- **[2021 · ICRA 2022] Towards More Generalizable One-shot Visual Imitation Learning** — [Paper](https://arxiv.org/abs/2110.13423) · [Code](https://github.com/rll-research/mosaic)
  `robot-demo` `contrastive-learning` · MOSAIC combines attention and temporal contrastive learning for multi-task one-shot imitation, with separate zero-update and fine-tuning evaluations.

- **[2017 · NeurIPS 2017] One-Shot Imitation Learning** — [Paper](https://papers.nips.cc/paper/2017/hash/ba3866600c3540f67c1e9575e213be0a-Abstract.html)
  `robot-demo` `action-policy` · Trains on demonstration pairs: one trajectory specifies the task, while states from another supervise actions.


<a id="adapt"></a>

## Test-time training and online optimization

Comparators, not zero-gradient ICL. Report which parameters or fast states are optimized, and include adaptation and interaction budgets.

- **[2026 · preprint] RoboTTT: Context Scaling for Robot Policies** — [Paper](https://arxiv.org/abs/2607.15275) · [Project](https://research.nvidia.com/labs/gear/robottt/)
  `fast-weights` `gradient-update` · Compresses long visuomotor context into fast weights updated during training and inference; not zero-gradient ICL.

- **[2026 · preprint] WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time** — [Paper](https://arxiv.org/abs/2607.06988)
  `human-video` `gradient-update` · Adapts lightweight memory through human-video prediction while freezing the base WAM; paired human-robot data is used in meta-training.

- **[2022 · RSS 2022] Human-to-Robot Imitation in the Wild** — [Paper](https://arxiv.org/abs/2207.09450) · [Project](https://human2robot.github.io/)
  `human-video` `online-optimization` · WHIRL initializes behavior from a human video and improves through robot interaction and sampling-based optimization.

- **[2018 · RSS 2018] One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning** — [Paper](https://www.roboticsproceedings.org/rss14/p02.html)
  `human-video` `gradient-update` · DAML meta-learns cross-domain adaptation from one human demonstration; task adaptation updates policy parameters.

- **[2017 · CoRL 2017] One-Shot Visual Imitation Learning via Meta-Learning** — [Paper](https://proceedings.mlr.press/v78/finn17a.html)
  `visual-demo` `gradient-update` · An early gradient-based meta-imitation method; one-shot data efficiency does not imply zero test-time updates.


<a id="adjacent"></a>

## Related video and skill-learning methods

Included for representation, data or action-grounding connections; these protocols are not interchangeable with human-demonstration ICL.

- **[2026 · preprint] VICX: Generalizable Robot Manipulation via Video Generation and In-Context Operator Network** — [Paper](https://arxiv.org/abs/2606.12028) · [Project](https://scaling-group.github.io/vicx/)
  `visual-plan` `retrieval` · Grounds generated visual plans into robot trajectories using retrieved image-state pairs; the context is not a human task video.

- **[2024 · ICLR 2025] Video In-context Learning: Autoregressive Transformers are Zero-Shot Video Imitators** — [Paper](https://arxiv.org/abs/2407.07356)
  `video-context` `video-only` · Transfers demonstrated visual dynamics through video generation; does not itself supply executable robot actions.

- **[2023 · CoRL 2023] MimicPlay: Long-Horizon Imitation Learning by Watching Human Play** — [Paper](https://arxiv.org/abs/2302.12422) · [Project](https://mimic-play.github.io/) · [Code](https://github.com/j96w/MimicPlay)
  `human-play` `hierarchical-policy` · Uses human play to learn high-level intent and robot demonstrations for low-level control; related data-transfer work, not interchangeable with a demo/query ICL protocol.

<a id="industrial"></a>

## Industrial releases

Company descriptions, not peer-reviewed papers or independent reproductions. Unpublished architecture, model size and data details are left unspecified.

- **[2026] Skild S1** — [Official blog](https://skild.ai/blogs/s1)
  Describes video-demonstration-conditioned manipulation without fine-tuning and a high-level episodic training recipe; implementation details are insufficient to reconstruct the architecture.

- **[2026] GEN-1.5** — [Official blog](https://generalistai.com/blog/gen-1.5)
  Separates zero-gradient ICL from few-gradient-step adaptation. The main physical-example protocol uses sensor observations and action trajectories; the blog also shows human hands observed through robot cameras. These examples should not be collapsed into one input protocol.

<a id="datasets"></a>

## Datasets and collection resources

The table distinguishes existing correspondence from pairs that must still be constructed. Native, retrieved, retargeted and generated supervision are not equivalent. A complete human-video ICL training sample still requires robot RGB/state aligned with target actions. Check the original release for version-specific access and licensing.

| Resource | Type | Contents and limitations |
| --- | --- | --- |
| [H&R / HumanAndRobot](https://huggingface.co/datasets/dannyXSC/HumanAndRobot) | native | Synchronized human and robot videos; robot pose/gripper streams. v1 /action is human-hand pose in the robot frame, not automatically the executed robot action. |
| [RH20T](https://rh20t.github.io/) | native | Corresponding human demonstration folders and multimodal robot executions. Same-task correspondence is not framewise human/robot synchronization. |
| [MIME](https://sites.google.com/view/mimedataset/home) | native | Human demonstration videos and Baxter kinesthetic trajectories; an early human/robot correspondence dataset. |
| [MimicDroid Dataset](https://huggingface.co/datasets/Rutav/MimicDroidDataset) | derived | Human-play-based data and retargeting; derived action supervision rather than independently measured real-robot GT. |
| [RHyME release](https://huggingface.co/datasets/prithwishdan/RHyME) | pseudo-pairing | Released simulation demonstrator/robot data and automatic-pairing code; do not label the release as a raw real-human video corpus. |
| [BC-Z](https://sites.google.com/view/bc-z/home) | task-level | Human-video task descriptions and robot demonstrations; inspect the release before assuming trajectory-level alignment. |
| [ICRT-MT](https://huggingface.co/datasets/Ravenh97/ICRT-MT) | robot | Robot sensorimotor data released with ICRT; suitable for robot-demo/query experiments, not a human-video source. |
| [DROID](https://droid-dataset.github.io/) | robot | Real robot RGB, proprioception and actions; same-task cross-episode pairing needs additional curation. |
| [Open X-Embodiment](https://robotics-transformer-x.github.io/) | robot | Heterogeneous robot datasets; action spaces, task labels and component licenses differ. |
| [AgiBot World Alpha](https://huggingface.co/datasets/agibot-world/AgiBotWorld-Alpha) | robot | Robot RGB/action trajectories; useful for query-side or robot-demo training, but does not supply the required human prompt_video by itself. |
| [RoboMIND](https://x-humanoid-robomind.github.io/) | robot | Multi-embodiment robot demonstrations; controller and action normalization remain necessary. |
| [UMI](https://umi-gripper.github.io/) | interface | Handheld-gripper collection system and releases; instrumented human motion, not ordinary bare-hand video. |
| [iPhUMI](https://github.com/real-stanford/iPhUMI) | interface | Collection/processing interface for instrumented demonstrations; BPP links task-specific datasets and checkpoints. |
| [HumanEgo](https://huggingface.co/datasets/Leo-TX/HumanEgo) | human-video | Human egocentric video source; human footage alone does not provide paired robot action targets. |
| [HumanGen (announced)](https://github.com/robbyant-research/Zero-WAM) | planned | Generated human-video/robot-trajectory pairs described by Zero-WAM; data release is still planned as of 2026-09-03. |

<a id="benchmarks"></a>

## Benchmarks

- [LIBERO / LIBERO-Gen / DrawAnything](https://github.com/real-stanford/behavior_prompting) — BPP provides demonstration-conditioned training and evaluation resources; use its task split, not just the environment name.
- [RoboTwin 2.0](https://robotwin-platform.github.io/) — Bimanual simulation and trajectory generation; reserve unseen tasks and independently sampled demonstrations for ICL.
- [MimicDroid benchmark](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) — Object/environment generalization levels in a RoboCasa-derived benchmark.
- [Zeva Atomic5 and PIM protocols](https://github.com/air-embodied-brain/Zeva) — Separates a frozen no-retry benchmark from fixed-seed cross-attempt case studies.
- [VIMA-Bench](https://vimalabs.github.io/) — Procedurally generated multimodal task specifications and generalization splits.

Minimum evaluation checks: held-out tasks, independent demonstration/execution episodes, swapped or removed `prompt_video` ablations, and matched retry/adaptation budgets. Random frame splits do not demonstrate unseen-task ICL.

<a id="related"></a>

## Related lists

Directly overlapping lists already exist. This list emphasizes manipulation protocols and reproducibility evidence; it does not claim an unoccupied topic. Corrections to existing lists are encouraged.

- [Awesome Embodied In-Context Learning](https://github.com/asimfish/awesome_ICL) — Direct topic overlap; broad bibliography and Chinese research notes.
- [Awesome In-Context Learning in Robot](https://github.com/BraveBoBo/awesome-in-context-learning--in-robot) — Automated digest with dated archives, including Zeva; not a single complete curated list.
- [Awesome Test-Time Robot Learning](https://github.com/Oliverbansk/Awesome-Test-Time-Robot-Learning) — Broader deployment-time adaptation, including ICL, TTT and policy steering.
- [Awesome Robot Learning from Human Videos](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos) — Human-to-robot learning, including offline training methods outside ICL.
- [Awesome WAM](https://github.com/OpenMOSS/Awesome-WAM) — World-action models, datasets and evaluation; overlaps with visual-future-conditioned ICL.
- [Awesome In-Context RL](https://github.com/dunnolab/awesome-in-context-rl) — In-context reinforcement learning and learning from interaction histories.

<a id="contributing"></a>

## Contributing

Edit the relevant README entry directly; no JSON catalog or generator is required. An issue with primary sources is also welcome, and maintainers can help synchronize translations. See [Contributing](CONTRIBUTING.md).

[MIT License](LICENSE). Linked papers, software, datasets and media retain their own licenses and are not redistributed here.
