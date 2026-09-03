# Data and releases

[English list](../README.md) · [中文列表](../README_zh-CN.md) · Updated 2026-09-03

## Data formats

- **[RH20T](https://rh20t.github.io/)** includes corresponding human demonstrations in `..._human/` folders. The human and robot executions correspond at task level; their frames are not synchronized.
- **[H&R](https://huggingface.co/datasets/dannyXSC/HumanAndRobot)** provides `/human_camera` and `/robot_camera`. Its v0 instructions use robot `/end_position` and `/gripper_state` as action targets; v1 `/action` instead records human-hand pose in the robot frame.
- **[BPP](https://arxiv.org/abs/2606.30457)** uses instrumented iPhUMI demonstrations. **[Instant-Fold](https://instant-fold.github.io/)** uses RGB-D cloth representations. Their demonstration inputs contain more than an ordinary human RGB video.

## Releases

| Work | Available resources | Notes |
| --- | --- | --- |
| [ICRT](https://github.com/Max-Fu/icrt) | Training/inference code, weights, ICRT-MT | The specific DROID pretraining subset is listed as forthcoming. |
| [BPP](https://github.com/real-stanford/behavior_prompting) | Policy code, task data/weights, deployment support | Manual export and processing are released; real-time wireless iPhUMI prompting remains planned. |
| [RICL](https://github.com/ricl-vla/ricl_openpi) | Training, retrieval, serving, data and weight links | The [paper](https://proceedings.mlr.press/v305/sridhar25a.html) uses 10–20 target-task demos and describes both retrieval-only and fine-tuning variants. |
| [Instant Policy](https://github.com/vv19/instant_policy) | Deployment code and weight-download script | Input: segmented point clouds, gripper poses and gripper states. |
| [RHyME](https://github.com/portal-cornell/rhyme) | Encoder/policy training, pairing code, simulation evaluation | The linked [dataset](https://huggingface.co/datasets/prithwishdan/RHyME) is the simulation release. |
| [MimicDroid](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) | Benchmark and dataset instructions | The [project](https://ut-austin-rpl.github.io/MimicDroid/) labels this repository as the benchmark. |
| [HOST](https://github.com/CGuangyan-BIT/HOST) | Training, recorded-data evaluation and a weight link | Recorded-data evaluation does not control a live robot. |
| [Zero-WAM](https://github.com/robbyant-research/Zero-WAM) | Paper, project and release plan | Code, weights and HumanGen data are planned before 2026-09-15. |
| [Zeva](https://github.com/air-embodied-brain/Zeva) | Code, weights, Atomic5 evaluation and PIM examples | The benchmark checkpoint uses no cross-attempt adaptation; PIM examples are separate. |

## Company descriptions

- **[GEN-1.5](https://generalistai.com/blog/gen-1.5)** describes sensor observations and action trajectories as physical examples, alongside a separate human-hand demonstration section. It reports both zero-gradient ICL and gradient adaptation.
- **[Skild S1](https://skild.ai/blogs/s1)** describes episodic demonstration-conditioned pretraining. The blog does not specify a complete architecture or parameter count.
