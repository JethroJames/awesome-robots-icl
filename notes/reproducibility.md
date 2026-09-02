# Reproducibility notes

[Back to the list](../README.md) · [返回中文列表](../README_zh-CN.md)

Snapshot: **2026-09-03**. These are source inspections, not training or robot-execution reproductions. No numerical leaderboard is implied.

## What the released resources actually cover

| Work | Deployment context | Located resources | Important boundary |
| --- | --- | --- | --- |
| [ICRT](https://github.com/Max-Fu/icrt) | Robot observations, proprioception and demonstrated actions | Training/inference code, checkpoint links, ICRT-MT | The README still lists its specific DROID pretraining subset as a release TODO. |
| [BPP](https://github.com/real-stanford/behavior_prompting) | Instrumented human sensorimotor demonstration | Policy code, task-specific data/checkpoint instructions and robot deployment support | Its TODO distinguishes the released manual export/process workflow from unreleased real-time wireless iPhUMI prompting. |
| [RICL](https://github.com/ricl-vla/ricl_openpi) | Retrieved segments of robot demonstrations | Retraining, retrieval, serving, datasets and checkpoint links | The [paper](https://proceedings.mlr.press/v305/sridhar25a.html) uses 10–20 target-task demonstrations; zero-update retrieval and optional target-task fine-tuning are separate modes. |
| [Instant Policy](https://github.com/vv19/instant_policy) | Segmented point clouds, gripper poses and gripper states | Pretrained deployment code and weight-download script | The documented interface is not raw human RGB video; a deployment release is not a full training-data release. |
| [RHyME](https://github.com/portal-cornell/rhyme) | Cross-embodiment demonstration video | Encoder training, automatic pairing, diffusion-policy training and simulation evaluation | The linked [dataset](https://huggingface.co/datasets/prithwishdan/RHyME) is the simulation release; real-human experiments in the paper do not establish release of the corresponding raw videos. |
| [MimicDroid](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) | Human-play examples with retargeted supervision | RoboCasa-derived benchmark and dataset instructions | The [project](https://ut-austin-rpl.github.io/MimicDroid/) labels this link Benchmark. This inspection does not establish a complete policy-training/checkpoint release. |
| [HOST](https://github.com/CGuangyan-BIT/HOST) | Human prompt_video | Alignment, target coupling, policy training, recorded-data evaluation and a weight link | Recorded-data evaluation does not command a live robot. The README does not establish release of the complete training corpus or turnkey real-robot reproduction. |
| [Zero-WAM](https://github.com/robbyant-research/Zero-WAM) | Human prompt_video | Paper, project and release-plan repository | Code, model and HumanGen data remain unchecked release-plan items, expected before 2026-09-15. A planned date is not an available artifact. |
| [Zeva](https://github.com/air-embodied-brain/Zeva) | Action-induced state changes across attempts | Code, weight link, frozen Atomic5 evaluation and fixed-seed PIM examples | The released benchmark checkpoint is success-only and evaluated without cross-attempt self-evolution; fixed-seed examples are not the same as benchmark-wide adaptation reproduction. |

An omitted resource means **not established by this inspection**, not proven nonexistent. For a real reproduction, pin repository commits, model revisions, dataset versions, control settings and evaluation seeds.

## Three distinctions that change data selection

### RH20T is not robot-only

The [official RH20T page](https://rh20t.github.io/) explicitly describes corresponding human demonstration videos and shows a robot episode alongside a matching `..._human/` directory. It is therefore a candidate for human `prompt_video` / robot execution pairing.

This is correspondence between demonstrations of the task, not a guarantee that the two executions have identical frame timing. Robot sensor synchronization and human-to-robot task alignment are different problems. Inspect the selected configuration, recording fields and matching keys before constructing examples.

### H&R action fields need interpretation

The [H&R dataset card](https://huggingface.co/datasets/dannyXSC/HumanAndRobot) distinguishes:

- `/human_camera` and `/robot_camera`;
- robot `/end_position` and `/gripper_state`, which its v0 instructions use as actions;
- the v1 `/action` field, which is **human-hand pose in the robot frame**.

Do not silently substitute an estimated/commanded human-hand pose for a measured robot trajectory. A policy dataset should document whether its target is a controller command, a robot state-derived target or a retargeted human trajectory.

### Human data is not a single modality

Plain human `prompt_video`, RGB-D human demonstrations, handheld-gripper sensorimotor recordings and robot teleoperation demonstrations carry different supervision. In particular, [BPP](https://arxiv.org/abs/2606.30457) uses iPhUMI, and [Instant-Fold](https://instant-fold.github.io/) describes RGB-D cloth tokens. Neither should be presented as evidence that every method works from an arbitrary RGB-only clip.

## Mechanism and claim boundaries

- [RoboTTT](https://arxiv.org/abs/2607.15275) updates fast weights through gradients. Freezing the base backbone does not make the complete system zero-gradient.
- [WAM-TTT](https://arxiv.org/abs/2607.06988) adapts lightweight memory from human-video prediction and uses paired human/robot data in meta-training.
- [Zeva](https://github.com/air-embodied-brain/Zeva) states that neural parameters remain frozen while external BIT/PIM memory changes.
- [GEN-1.5](https://generalistai.com/blog/gen-1.5) separates zero-gradient physical-example conditioning from few-step gradient adaptation. Its main described examples include sensor observations and action trajectories; a separate human-hand demonstration section should not be treated as an identical fully specified interface.
- [Skild S1](https://skild.ai/blogs/s1) describes episodic demonstration-conditioned pretraining at a high level. That is evidence for the training interface, not a disclosure of a reconstructable architecture or parameter count.

## A reproducibility checklist

1. What is the context: human video, robot sensorimotor sequence, structured demonstration or robot interaction memory?
2. What is genuinely unseen: task, object, scene, motion, embodiment or only initial state?
3. Are demonstration and query from different executions, with task-level train/test isolation?
4. Does removing or swapping the demonstration change behavior appropriately?
5. Are model weights, fast weights, auxiliary memory or retrieved examples updated?
6. Are retry counts, demonstrations, adaptation compute and interventions matched?
7. Are released code, checkpoint and data sufficient for the exact claim being evaluated?
8. Are robot RGB/proprioception and target actions temporally and geometrically consistent?

These checks guide reading and reproduction; they are not claims that every listed paper has passed them.
