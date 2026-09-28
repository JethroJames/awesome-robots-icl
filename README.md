<a id="top"></a>

# In-Context Learning for Robots

**Methods and Applications**

<p>
<a href="https://jethrojames.github.io/awesome-robots-icl/assets/robot-icl-survey.pdf"><img src="https://img.shields.io/badge/PDF-100_pages-222222?style=flat-square" alt="Paper PDF — 100 pages" height="26"></a>
<img src="https://img.shields.io/badge/arXiv-coming_soon-B31B1B?style=flat-square" alt="arXiv — coming soon" height="26">
<a href="https://jethrojames.github.io/awesome-robots-icl/"><img src="https://img.shields.io/badge/Project_Page-Online-222222?style=flat-square" alt="Project Page" height="26"></a>
</p>

**English** · [简体中文](README_zh-CN.md)

**432 papers · Four method families**

## Browse the taxonomy

| Method family | Control mechanism | Papers |
| :--- | :--- | ---: |
| [Context-conditioned policies](#policy) | Action inference | [128](papers/policy.md) |
| [Geometric demonstration transfer](#geometry) | Motion transfer | [28](papers/geometry.md) |
| [World-model-based control](#world) | Future prediction | [27](papers/world.md) |
| [Skill- and agent-based execution](#agent) | Skill & program execution | [92](papers/agent.md) |

[Navigation: four context types](#navigation) | [Physical self-improvement](#improvement)

[Shared correspondence and memory mechanisms](#shared) · [Data and acquisition interfaces](#data) · [Training and improvement](#training) · [Grounding and failure assessment](#grounding) · [Benchmarks and evaluation](#evaluation) · [Foundations and related surveys](#foundations)

Within each subcategory, papers are ordered by **first public release, newest first**; year only when the month is unavailable. Navigation and self-improvement provide complementary views by context type and update target.

---

<a id="policy"></a>

## 01 · Context-conditioned policies

<a id="policy-demo"></a>

### Demonstration-conditioned action generation

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | GLOW: A Generative Learning Framework for General-Purpose Embodied Intelligence <!-- paper:knowin2026glow --> | <a href="https://knowinai.com/tech.html"><img src="https://img.shields.io/badge/Report-52616b.svg?style=flat-square" alt="Report" height="24"></a> | — |
| 2026‑09 | Embodied In-Context Learning for GPT-6 Astra <!-- paper:extra_roboicl --> | <a href="https://mosi-ai.github.io/RoboICL-GPT6-Astra.github.io/"><img src="https://img.shields.io/badge/Report-52616b.svg?style=flat-square" alt="Report" height="24"></a> | [Code](https://github.com/Mosi-AI/RoboICL) |
| 2026‑09 | ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models <!-- paper:yang2026icivla --> | <a href="https://arxiv.org/abs/2609.07581"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | ContextFlow: In-Context Flow Matching for Robot Manipulation <!-- paper:ding2026contextflow --> | <a href="https://arxiv.org/abs/2609.06852"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/dingjiansw101/ContextFlow) |
| 2026‑08 | PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control <!-- paper:choi2026ponderpounce --> | <a href="https://arxiv.org/abs/2608.24115"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/worv-ai/PonderPounce) |
| 2026‑08 | GEN-1.5: Embodied Foundation Models are One-Shot Learners <!-- paper:generalist2026gen15 --> | <a href="https://generalistai.com/blog/gen-1.5"><img src="https://img.shields.io/badge/Report-52616b.svg?style=flat-square" alt="Report" height="24"></a> | — |
| 2026‑08 | Introducing S1: In-Context Learning for Robotics <!-- paper:skild2026s1 --> | <a href="https://www.skild.ai/blogs/s1"><img src="https://img.shields.io/badge/Report-52616b.svg?style=flat-square" alt="Report" height="24"></a> | — |
| 2026‑08 | Task-Prototype Guided Flow Matching for Few-Shot Generalization in Vision-Language Robot Manipulation <!-- paper:arxiv260927780 --> | <a href="https://arxiv.org/abs/2609.27780"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models <!-- paper:xu2026stellavla --> | <a href="https://arxiv.org/abs/2608.11671"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | Behavior Prompting Policy: Demonstrations as Prompts for Manipulation <!-- paper:patel2026bpp --> | <a href="https://arxiv.org/abs/2606.30457"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/real-stanford/behavior_prompting) |
| 2026‑06 | SynthICL: Scalable In-context Imitation Learning with Synthetic Data <!-- paper:qian2026synthicl --> | <a href="https://arxiv.org/abs/2606.08154"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | Instant-Fold: In-Context Imitation Learning for Deformable Object Manipulation <!-- paper:wang2026instantfold --> | <a href="https://arxiv.org/abs/2606.04269"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/kelthuzadyl/Instant-Fold) |
| 2026‑06 | SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos <!-- paper:son2026seetraceact --> | <a href="https://arxiv.org/abs/2606.02745"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics <!-- paper:fateh2026histat --> | <a href="https://arxiv.org/abs/2604.15215"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | ICLR: In-Context Imitation Learning with Visual Reasoning <!-- paper:nguyen2026iclr --> | <a href="https://arxiv.org/abs/2603.07530"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/toannguyen1904/ICLR) |
| 2026‑02 | Mimic Intent, Not Just Trajectories <!-- paper:huang2026mint --> | <a href="https://arxiv.org/abs/2602.08602"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/RenMing-Huang/MINT) |
| 2025‑12 | See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations <!-- paper:chen2025vivla --> | <a href="https://arxiv.org/abs/2512.07582"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑09 | RoboSSM: Scalable In-context Imitation Learning via State-Space Models <!-- paper:extra250919658 --> | <a href="https://arxiv.org/abs/2509.19658"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/youngjuY/RoboSSM) |
| 2025‑09 | MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos <!-- paper:shah2025mimicdroid --> | <a href="https://arxiv.org/abs/2509.09769"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/UT-Austin-RPL/mimicdroid-robocasa) |
| 2025‑08 | RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models <!-- paper:sridhar2025ricl --> | <a href="https://arxiv.org/abs/2508.02062"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/ricl-vla/ricl_openpi) |
| 2025‑05 | Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt <!-- paper:extra250520795 --> | <a href="https://arxiv.org/abs/2505.20795"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑03 | Action Tokenizer Matters in In-Context Imitation Learning <!-- paper:vuong2025actiontokenizer --> | <a href="https://arxiv.org/abs/2503.01206"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/andvg3/LipVQ-VAE) |
| 2024‑09 | One-Shot Imitation under Mismatched Execution <!-- paper:kedia2024rhyme --> | <a href="https://arxiv.org/abs/2409.06615"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/portal-cornell/rhyme) |
| 2024‑08 | In-Context Imitation Learning via Next-Token Prediction <!-- paper:fu2024icrt --> | <a href="https://arxiv.org/abs/2408.15980"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Max-Fu/icrt) |
| 2024‑03 | Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers <!-- paper:jain2024vid2robot --> | <a href="https://arxiv.org/abs/2403.12943"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑10 | VIMA: General Robot Manipulation with Multimodal Prompts <!-- paper:jiang2022vima --> | <a href="https://arxiv.org/abs/2210.03094"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/vimalabs/VIMA) |
| 2022‑02 | BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning <!-- paper:jang2022bcz --> | <a href="https://arxiv.org/abs/2202.02005"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2021‑10 | Towards More Generalizable One-shot Visual Imitation Learning <!-- paper:mandi2021mosaic --> | <a href="https://arxiv.org/abs/2110.13423"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/rll-research/mosaic) |
| 2020‑11 | Transformers for One-Shot Visual Imitation <!-- paper:dasari2020tosil --> | <a href="https://arxiv.org/abs/2011.05970"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/SudeepDasari/one_shot_transformers) |
| 2020‑10 | Path-Following Navigation Network Using Sparse Visual Memory <!-- paper:yoo2020sparsepath --> | <a href="https://doi.org/10.23919/ICCAS50221.2020.9268247"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 2019‑11 | Learning One-Shot Imitation from Humans without Humans <!-- paper:bonardi2019humans --> | <a href="https://arxiv.org/abs/1911.01103"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2018‑12 | Visual Memory for Robust Path Following <!-- paper:kumar2018rpf --> | <a href="https://arxiv.org/abs/1812.00940"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2018‑10 | Task-Embedded Control Networks for Few-Shot Imitation Learning <!-- paper:james2018tec --> | <a href="https://arxiv.org/abs/1810.03237"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2018‑04 | Zero-Shot Visual Imitation <!-- paper:pathak2018zeroshot --> | <a href="https://arxiv.org/abs/1804.08606"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/pathak22/zeroshot-imitation) |
| 2017‑03 | One-Shot Imitation Learning <!-- paper:duan2017oneshot --> | <a href="https://arxiv.org/abs/1703.07326"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="policy-spatial"></a>

### Spatial correspondence and action representations

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑08 | MatchingPolicy: Correspondence-Aware Policy Enables Cross-Object In-Context Learning <!-- paper:she2026matchingpolicy --> | <a href="https://arxiv.org/abs/2608.16715"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances <!-- paper:oh2026vlaff --> | <a href="https://arxiv.org/abs/2608.05215"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | Bimanual Robot Manipulation via Multi-Agent In-Context Learning <!-- paper:palma2026bicicle --> | <a href="https://arxiv.org/abs/2604.20348"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑06 | Robust Instant Policy: Leveraging Student&#x27;s t-Regression Model for Robust In-context Imitation Learning of Robot Manipulation <!-- paper:oh2025rip --> | <a href="https://arxiv.org/abs/2506.15157"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑02 | Point Policy: Unifying Observations and Actions with Key Points for Robot Manipulation <!-- paper:haldar2025pointpolicy --> | <a href="https://arxiv.org/abs/2502.20391"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/siddhanthaldar/Point-Policy) |
| 2025‑01 | SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model <!-- paper:qu2025spatialvla --> | <a href="https://arxiv.org/abs/2501.15830"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/SpatialVLA/SpatialVLA) |
| 2024‑11 | Instant Policy: In-Context Imitation Learning via Graph Diffusion <!-- paper:vosylius2024instantpolicy --> | <a href="https://arxiv.org/abs/2411.12633"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/vv19/instant_policy) |
| 2024‑10 | In-Context Learning Enables Robot Action Prediction in LLMs <!-- paper:yin2024roboprompt --> | <a href="https://arxiv.org/abs/2410.12782"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/davidyyd/roboprompt) |
| 2024‑10 | Keypoint Abstraction using Large Models for Object-Relative Imitation Learning <!-- paper:fang2024kalm --> | <a href="https://arxiv.org/abs/2410.23254"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/FANG-Xiaolin/KALM) |
| 2024‑08 | NOLO: Navigate Only Look Once <!-- paper:zhou2024nolo --> | <a href="https://arxiv.org/abs/2408.01384"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/zhoubohan0/NOLO) |
| 2024‑03 | Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics <!-- paper:dipalo2024keypoint --> | <a href="https://arxiv.org/abs/2403.19578"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="policy-retrieval"></a>

### Action retrieval and refinement

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | Training-free Behavior Cloning <!-- paper:arxiv260930134 --> | <a href="https://arxiv.org/abs/2609.30134"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | TraceFlow: Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces <!-- paper:extra260920646 --> | <a href="https://arxiv.org/abs/2609.20646"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation <!-- paper:arxiv260920648 --> | <a href="https://arxiv.org/abs/2609.20648"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | UniMPA: A Unified Memory-Prediction-Action Model via Action-Grounded Transition Modeling <!-- paper:extra260911875 --> | <a href="https://arxiv.org/abs/2609.11875"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/JiuTian-VL/UniMPA) |
| 2026‑08 | Retrieve in Time, Correct in Frequency <!-- paper:fan2026rtcf --> | <a href="https://arxiv.org/abs/2608.04527"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | SAIL: Test-Time Scaling for In-Context Imitation Learning with VLM <!-- paper:sato2026sail --> | <a href="https://arxiv.org/abs/2603.08269"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑06 | DemoDiffusion: One-Shot Human Imitation using pre-trained Diffusion Policy <!-- paper:park2025demodiffusion --> | <a href="https://arxiv.org/abs/2506.20668"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/demodiffusion/demodiffusion) |
| 2025‑06 | RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models <!-- paper:arxiv250617811 --> | <a href="https://arxiv.org/abs/2506.17811"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑12 | REGENT: A Retrieval-Augmented Generalist Agent That Can Act In-Context in New Environments <!-- paper:sridhar2024regent --> | <a href="https://arxiv.org/abs/2412.04759"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/regent-research/regent) |
| 2021‑12 | The Surprising Effectiveness of Representation Learning for Visual Imitation <!-- paper:pari2021vinn --> | <a href="https://arxiv.org/abs/2112.01511"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/jyopari/VINN) |

<a id="policy-history"></a>

### Interaction history and physical adaptation

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | Self-Adaptive VLA for Robust Robot Deployment <!-- paper:arxiv260930092 --> | <a href="https://arxiv.org/abs/2609.30092"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Zeva-Ego: Egocentric Mid-Training with In-Context Causal Learning for Robot Manipulation <!-- paper:arxiv260924411 --> | <a href="https://arxiv.org/abs/2609.24411"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/air-embodied-brain/Zeva/tree/feature/zeva_ego) |
| 2026‑09 | RopeFormer: Cross-Trial Adaptation from Interaction History for Dynamic Rope Manipulation <!-- paper:arxiv260923432 --> | <a href="https://arxiv.org/abs/2609.23432"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | TEMPO: Learning Temporal Context for Dynamic Robot Manipulation <!-- paper:extra260916864 --> | <a href="https://arxiv.org/abs/2609.16864"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/tempo-robot/TEMPO) |
| 2026‑09 | CR-VLA-Force: Learning Control-aware Compliance VLA Model for Robust Contact-rich Robotic Manipulation <!-- paper:mai2026crvlaforce --> | <a href="https://arxiv.org/abs/2609.05832"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation <!-- paper:chen2026zeva --> | <a href="https://arxiv.org/abs/2608.30880"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/air-embodied-brain/Zeva) |
| 2026‑08 | TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback <!-- paper:arxiv260825798 --> | <a href="https://arxiv.org/abs/2608.25798"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | In-Context World Modeling for Robotic Control <!-- paper:wang2026icwm --> | <a href="https://arxiv.org/abs/2606.26025"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | AdaTracker: Learning Adaptive In-Context Policy for Cross-Embodiment Active Visual Tracking <!-- paper:wu2026adatracker --> | <a href="https://arxiv.org/abs/2604.20305"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | Gated Memory Policy: In-Context Memorization and Adaptation <!-- paper:gao2026gmp --> | <a href="https://arxiv.org/abs/2604.18933"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/real-stanford/gated-memory-policy) |
| 2025‑09 | LocoFormer: Generalist Locomotion via Long-context Adaptation <!-- paper:liu2025locoformer --> | <a href="https://arxiv.org/abs/2509.23745"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑07 | Behavioral Exploration: Learning to Explore via In-Context Adaptation <!-- paper:wagenmaker2025exploration --> | <a href="https://arxiv.org/abs/2507.09041"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑10 | ReLIC: A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI <!-- paper:elawady2024relic --> | <a href="https://arxiv.org/abs/2410.02751"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/aielawady/relic) |
| 2023‑10 | AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents <!-- paper:grigsby2023amago --> | <a href="https://arxiv.org/abs/2310.09971"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/UT-Austin-RPL/amago) |
| 2022‑10 | In-context Reinforcement Learning with Algorithm Distillation <!-- paper:laskin2022ad --> | <a href="https://arxiv.org/abs/2210.14215"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑06 | Prompting Decision Transformer for Few-Shot Policy Generalization <!-- paper:xu2022promptdt --> | <a href="https://arxiv.org/abs/2206.13499"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/mxu34/prompt-dt) |
| 2022‑06 | Robust Task Representations for Offline Meta-Reinforcement Learning via Contrastive Learning <!-- paper:yuan2022corro --> | <a href="https://arxiv.org/abs/2206.10442"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/PKU-AI-Edge/CORRO) |
| 2021‑07 | RMA: Rapid Motor Adaptation for Legged Robots <!-- paper:kumar2021rma --> | <a href="https://arxiv.org/abs/2107.04034"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/antonilo/rl_locomotion) |
| 2020‑11 | Modeling Task Uncertainty for Safe Meta-Imitation Learning <!-- paper:matsushima2020uncertainty --> | <a href="https://doi.org/10.3389/frobt.2020.606361"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 2020‑10 | FOCAL: Efficient Fully-Offline Meta-Reinforcement Learning via Distance Metric Learning and Behavior Regularization <!-- paper:li2020focal --> | <a href="https://arxiv.org/abs/2010.01112"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/LanqingLi1993/FOCAL-ICLR) |
| 2020‑06 | MetaCURE: Meta Reinforcement Learning with Empowerment-Driven Exploration <!-- paper:zhang2020metacure --> | <a href="https://arxiv.org/abs/2006.08170"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2019‑10 | VariBAD: A Very Good Method for Bayes-Adaptive Deep RL via Meta-Learning <!-- paper:zintgraf2019varibad --> | <a href="https://arxiv.org/abs/1910.08348"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/lmzintgraf/varibad) |
| 2019‑06 | Watch, Try, Learn: Meta-Learning from Demonstrations and Reward <!-- paper:zhou2019wtl --> | <a href="https://arxiv.org/abs/1906.03352"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2019‑03 | Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context Variables <!-- paper:rakelly2019pearl --> | <a href="https://arxiv.org/abs/1903.08254"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/katerakelly/oyster) |
| 2017‑07 | A Simple Neural Attentive Meta-Learner <!-- paper:mishra2017snail --> | <a href="https://arxiv.org/abs/1707.03141"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2017‑02 | Preparing for the Unknown: Learning a Universal Policy with Online System Identification <!-- paper:yu2017uposi --> | <a href="https://arxiv.org/abs/1702.02453"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2016‑11 | RL²: Fast Reinforcement Learning via Slow Reinforcement Learning <!-- paper:duan2016rl2 --> | <a href="https://arxiv.org/abs/1611.02779"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="policy-memory"></a>

### Memory and long-context policies

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams <!-- paper:arxiv260928429 --> | <a href="https://arxiv.org/abs/2609.28429"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | MemBodied: Recurrent Associative Memory for Vision-Language-Action Models <!-- paper:arxiv260928256 --> | <a href="https://arxiv.org/abs/2609.28256"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/declare-lab/MemBodied) |
| 2026‑09 | Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision <!-- paper:extra260920820 --> | <a href="https://arxiv.org/abs/2609.20820"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation <!-- paper:arxiv260919796 --> | <a href="https://arxiv.org/abs/2609.19796"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models <!-- paper:yin2026simplememvla --> | <a href="https://arxiv.org/abs/2609.05533"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/wadeKeith/SimpleMemVLA) |
| 2026‑08 | TemporalFlow-VLA: Learning Physically Grounded Execution History for Long-Horizon Robot Manipulation <!-- paper:arxiv260826821 --> | <a href="https://arxiv.org/abs/2608.26821"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control <!-- paper:shah2026halo --> | <a href="https://arxiv.org/abs/2606.25136"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/UT-Austin-RobIn/HALO) |
| 2026‑06 | EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies <!-- paper:yang2026eventvla --> | <a href="https://arxiv.org/abs/2606.20092"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | μVLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models <!-- paper:cherepanov2026muvla --> | <a href="https://arxiv.org/abs/2606.12497"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/CognitiveAISystems/muVLA) |
| 2026‑03 | ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries <!-- paper:li2026rememvla --> | <a href="https://arxiv.org/abs/2603.12942"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | MEM: Multi-Scale Embodied Memory for Vision Language Action Models <!-- paper:torne2026mem --> | <a href="https://arxiv.org/abs/2603.03596"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑10 | MemER: Scaling Up Memory for Robot Control via Experience Retrieval <!-- paper:sridhar2025memer --> | <a href="https://arxiv.org/abs/2510.20328"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/memer-policy/memer) |
| 2025‑08 | MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation <!-- paper:shi2025memoryvla --> | <a href="https://arxiv.org/abs/2508.19236"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/shihao1895/MemoryVLA) |
| 2025‑05 | Learning Long-Context Diffusion Policies via Past-Token Prediction <!-- paper:torne2025ptp --> | <a href="https://arxiv.org/abs/2505.09561"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/long-context-dp/ldp) |

<a id="policy-prior"></a>

### Pretrained policies and cross-task competence

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑07 | Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories <!-- paper:xiaomi2026robotics1 --> | <a href="https://arxiv.org/abs/2607.15330"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) |
| 2026‑05 | Wall-OSS-0.5 Technical Report <!-- paper:yu2026walloss05 --> | <a href="https://arxiv.org/abs/2605.30877"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | π₀.₇: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities <!-- paper:arxiv260415483 --> | <a href="https://arxiv.org/abs/2604.15483"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑01 | Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning <!-- paper:huang2026fastthinkact --> | <a href="https://arxiv.org/abs/2601.09708"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑12 | Emergence of Human to Robot Transfer in Vision-Language-Action Models <!-- paper:arxiv251222414 --> | <a href="https://arxiv.org/abs/2512.22414"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑08 | Galaxea Open-World Dataset and G0 Dual-System VLA Model <!-- paper:galaxea2025 --> | <a href="https://arxiv.org/abs/2509.00576"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑03 | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots <!-- paper:nvidia2025gr00t --> | <a href="https://arxiv.org/abs/2503.14734"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/NVIDIA/Isaac-GR00T) |
| 2024‑10 | π₀: A Vision-Language-Action Flow Model for General Robot Control <!-- paper:black2024pi0 --> | <a href="https://arxiv.org/abs/2410.24164"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Physical-Intelligence/openpi) |
| 2024‑10 | RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation <!-- paper:liu2024rdt --> | <a href="https://arxiv.org/abs/2410.07864"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/thu-ml/RoboticsDiffusionTransformer) |
| 2024‑09 | Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers <!-- paper:hpt2024 --> | <a href="https://arxiv.org/abs/2409.20537"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/liruiw/HPT) |
| 2024‑08 | Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation <!-- paper:doshi2024crossformer --> | <a href="https://arxiv.org/abs/2408.11812"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/rail-berkeley/crossformer) |
| 2024‑06 | OpenVLA: An Open-Source Vision-Language-Action Model <!-- paper:kim2024openvla --> | <a href="https://arxiv.org/abs/2406.09246"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/openvla/openvla) |
| 2024‑05 | Octo: An Open-Source Generalist Robot Policy <!-- paper:octo2024 --> | <a href="https://arxiv.org/abs/2405.12213"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/octo-models/octo) |
| 2023‑10 | Open X-Embodiment: Robotic Learning Datasets and RT-X Models <!-- paper:oxe2023 --> | <a href="https://arxiv.org/abs/2310.08864"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/google-deepmind/open_x_embodiment) |
| 2023‑09 | RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking <!-- paper:bharadhwaj2023roboagent --> | <a href="https://arxiv.org/abs/2309.01918"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/robopen/roboagent) |
| 2023‑07 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control <!-- paper:brohan2023rt2 --> | <a href="https://arxiv.org/abs/2307.15818"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑04 | Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware <!-- paper:zhao2023act --> | <a href="https://arxiv.org/abs/2304.13705"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/tonyzhaozh/act) |
| 2022‑12 | RT-1: Robotics Transformer for Real-World Control at Scale <!-- paper:brohan2022rt1 --> | <a href="https://arxiv.org/abs/2212.06817"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/google-research/robotics_transformer) |

<a id="policy-update"></a>

### Parameter adaptation and policy improvement

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface <!-- paper:arxiv260920659 --> | <a href="https://arxiv.org/abs/2609.20659"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On-Policy Corrections <!-- paper:xu2026bimanualscaling --> | <a href="https://arxiv.org/abs/2609.03591"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning <!-- paper:arxiv260821204 --> | <a href="https://arxiv.org/abs/2608.21204"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use <!-- paper:arxiv260805738 --> | <a href="https://arxiv.org/abs/2608.05738"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | RoboTTT: Context Scaling for Robot Policies <!-- paper:jiang2026robottt --> | <a href="https://arxiv.org/abs/2607.15275"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | Robotic Policy Adaptation via Weight-Space Meta-Learning <!-- paper:extra260607217 --> | <a href="https://arxiv.org/abs/2606.07217"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis <!-- paper:arxiv260313528 --> | <a href="https://arxiv.org/abs/2603.13528"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑02 | VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model <!-- paper:arxiv260212063 --> | <a href="https://arxiv.org/abs/2602.12063"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑02 | World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy <!-- paper:arxiv260206508 --> | <a href="https://arxiv.org/abs/2602.06508"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑11 | π*₀.₆: a VLA That Learns From Experience <!-- paper:arxiv251114759 --> | <a href="https://arxiv.org/abs/2511.14759"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑06 | RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation <!-- paper:bousmalis2023robocat --> | <a href="https://arxiv.org/abs/2306.11706"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2018‑02 | One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning <!-- paper:yu2018domainadaptive --> | <a href="https://arxiv.org/abs/1802.01557"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2017‑09 | One-Shot Visual Imitation Learning via Meta-Learning <!-- paper:finn2017mil --> | <a href="https://arxiv.org/abs/1709.04905"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

[↑ Back to top](#top) · [Category page](papers/policy.md)

---

<a id="geometry"></a>

## 02 · Geometric demonstration transfer

<a id="geometry-alignment"></a>

### Visual alignment and reference tracking

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2024‑05 | One-Shot Imitation Learning with Invariance Matching for Robotic Manipulation <!-- paper:zhang2024imop --> | <a href="https://arxiv.org/abs/2405.13178"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑02 | DINOBot: Robot Manipulation via Retrieval and Alignment with Vision Foundation Models <!-- paper:dipalo2023dinobot --> | <a href="https://arxiv.org/abs/2402.13181"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑10 | One-Shot Imitation Learning: A Pose Estimation Perspective <!-- paper:vitiello2023pose --> | <a href="https://arxiv.org/abs/2310.12077"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑08 | RoboTAP: Tracking Arbitrary Points for Few-Shot Visual Imitation <!-- paper:vecerik2023robotap --> | <a href="https://arxiv.org/abs/2308.15975"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/google-deepmind/tapnet) |
| 2022‑04 | Demonstrate Once, Imitate Immediately (DOME): Learning Visual Servoing for One-Shot Imitation Learning <!-- paper:valassakis2022dome --> | <a href="https://arxiv.org/abs/2204.02863"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2021‑05 | Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration <!-- paper:extra210506411 --> | <a href="https://arxiv.org/abs/2105.06411"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2020‑07 | FlowControl: Optical Flow Based Visual Servoing <!-- paper:argus2020flowcontrol --> | <a href="https://arxiv.org/abs/2007.00291"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="geometry-retarget"></a>

### Trajectory reconstruction and retargeting

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | V2-STRep: VLM-Grounded Structured Task Representations for Reusable Robot Skills Acquired from Generated Videos <!-- paper:extra260920582 --> | <a href="https://arxiv.org/abs/2609.20582"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026 | Demonstrate once, execute on many: Kinematic intelligence for cross-robot skill transfer <!-- paper:gupta2026kinematic --> | <a href="https://doi.org/10.1126/scirobotics.aea1995"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 2025‑10 | HRT1: One-Shot Human-to-Robot Trajectory Transfer for Mobile Manipulation <!-- paper:allu2025hrt1 --> | <a href="https://arxiv.org/abs/2510.21026"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/IRVLUTD/HRT1) |
| 2025‑03 | Elastic Motion Policy: An Adaptive Dynamical System for Robust and Efficient One-Shot Imitation Learning <!-- paper:li2025emp --> | <a href="https://arxiv.org/abs/2503.08029"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/penn-figueroa-lab/emp) |
| 2024‑07 | R+X: Retrieval and Execution from Everyday Human Videos <!-- paper:extra240712957 --> | <a href="https://arxiv.org/abs/2407.12957"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/gpapagiannis/r-plus-x-hand2actions) |
| 2024‑05 | ScrewMimic: Bimanual Imitation from Human Videos with Screw Space Projection <!-- paper:bahety2024screwmimic --> | <a href="https://arxiv.org/abs/2405.03666"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/UT-Austin-RobIn/ScrewMimic) |
| 2024‑03 | DITTO: Demonstration Imitation by Trajectory Transformation <!-- paper:heppert2024ditto --> | <a href="https://arxiv.org/abs/2403.15203"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/robot-learning-freiburg/DITTO) |
| 2023‑06 | One-shot Imitation Learning via Interaction Warping <!-- paper:biza2023warping --> | <a href="https://arxiv.org/abs/2306.12392"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="geometry-functional"></a>

### Functional correspondence and object substitution

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑08 | Sparse Meets Dense: Correspondence Guided Robotic Manipulation with Rigid-Deformable Interactions <!-- paper:zhu2026sparsedense --> | <a href="https://arxiv.org/abs/2608.01083"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | SemAnCorr: Semantic Anchored Correspondence for Zero-Shot Manipulation Skill Transfer <!-- paper:dong2026semancorr --> | <a href="https://arxiv.org/abs/2607.28382"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/semancorr/SemAnCorr) |
| 2026‑04 | One-Shot Cross-Geometry Skill Transfer through Part Decomposition <!-- paper:thompson2026parttransfer --> | <a href="https://arxiv.org/abs/2604.15455"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑03 | GIFT: Geometry-Induced Functional Transfer for Category-level Object Manipulation <!-- paper:defarias2025gift --> | <a href="https://arxiv.org/abs/2503.15371"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑02 | FUNCTO: Function-Centric One-Shot Imitation Learning for Tool Manipulation <!-- paper:tang2025functo --> | <a href="https://arxiv.org/abs/2502.11744"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑11 | One-Shot Manipulation Strategy Learning by Making Contact Analogies <!-- paper:liu2024magic --> | <a href="https://arxiv.org/abs/2411.09627"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/nature21/magic) |
| 2022‑11 | SE(3)-Equivariant Relational Rearrangement with Neural Descriptor Fields <!-- paper:simeonov2023rndf --> | <a href="https://arxiv.org/abs/2211.09786"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/anthonysimeonov/relational_ndf) |

<a id="geometry-repertoire"></a>

### Multi-stage transfer and reusable repertoires

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | VLBiMan++: Expanding the Generalization Boundary of Vision-Language Anchored One-Shot Bimanual Manipulation <!-- paper:extra260914310 --> | <a href="https://arxiv.org/abs/2609.14310"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/hnuzhy/BiRoMan) |
| 2026‑09 | Continual Field-Adaptive Models (CFAMs) for Post-Deployment Physical AI <!-- paper:extra260904552 --> | <a href="https://arxiv.org/abs/2609.04552"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑12 | ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation <!-- paper:chen2025manilong --> | <a href="https://arxiv.org/abs/2512.16302"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑11 | Learning a Thousand Tasks in a Day <!-- paper:dreczkowski2025mt3 --> | <a href="https://arxiv.org/abs/2511.10110"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/kamil-dreczkowski/learning_thousand_tasks) |
| 2025‑09 | Annotation-Free One-Shot Imitation Learning for Multi-Step Manipulation Tasks <!-- paper:wichitwechkarn2025annotationfree --> | <a href="https://arxiv.org/abs/2509.24972"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑03 | One-Shot Dual-Arm Imitation Learning <!-- paper:wang2025odil --> | <a href="https://arxiv.org/abs/2503.06831"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/kelthuzadyl/ODIL) |

[↑ Back to top](#top) · [Category page](papers/geometry.md)

---

<a id="world"></a>

## 03 · World-model-based control

<a id="world-futures"></a>

### Demonstration-conditioned future generation

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
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

<a id="world-planning"></a>

### Predictive planning, memory, and recovery

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | DeltaWAM: Delta World Action Models for Bimanual Manipulation <!-- paper:arxiv260928811 --> | <a href="https://arxiv.org/abs/2609.28811"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning <!-- paper:arxiv260919315 --> | <a href="https://arxiv.org/abs/2609.19315"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Causal-History Test-Time Scaling for Failure Recovery in Autoregressive World-Action Models <!-- paper:extra260918016 --> | <a href="https://arxiv.org/abs/2609.18016"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | τ₀-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation <!-- paper:arxiv260816885 --> | <a href="https://arxiv.org/abs/2608.16885"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/sii-research/tau-0-vla) |
| 2026‑08 | Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models <!-- paper:core2026realignment --> | <a href="https://arxiv.org/abs/2608.14822"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models <!-- paper:shi2026memoryvlapp --> | <a href="https://arxiv.org/abs/2606.09827"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/shihao1895/MemoryVLA) |
| 2023‑05 | MetaDiffuser: Diffusion Model as Conditional Planner for Offline Meta-RL <!-- paper:ni2023metadiffuser --> | <a href="https://arxiv.org/abs/2305.19923"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑10 | Decomposed Mutual Information Optimization for Generalized Context in Meta-Reinforcement Learning <!-- paper:mu2022domino --> | <a href="https://arxiv.org/abs/2210.04209"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2018‑10 | Robustness via Retrying: Closed-Loop Robotic Manipulation with Self-Supervised Learning <!-- paper:ebert2018retrying --> | <a href="https://arxiv.org/abs/1810.03043"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/febert/robustness_via_retrying) |
| 2018‑04 | Universal Planning Networks <!-- paper:srinivas2018upn --> | <a href="https://arxiv.org/abs/1804.00645"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="world-update"></a>

### Model adaptation and self-improvement

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | Online Sim-to-Real Adaptation via Closed-Loop System Modeling <!-- paper:arxiv260928878 --> | <a href="https://arxiv.org/abs/2609.28878"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models <!-- paper:arxiv260921740 --> | <a href="https://arxiv.org/abs/2609.21740"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | MetaPusher: Meta Learning and Planning for Nonprehensile Manipulation of Unseen Objects with Rapid Online Adaption <!-- paper:arxiv260921122 --> | <a href="https://arxiv.org/abs/2609.21122"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning <!-- paper:extra260912278 --> | <a href="https://arxiv.org/abs/2609.12278"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Motus2: A Self-Evolving General World Model for Dexterous Manipulation <!-- paper:bi2026motus2 --> | <a href="https://arxiv.org/abs/2608.30237"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time <!-- paper:arxiv260706988 --> | <a href="https://arxiv.org/abs/2607.06988"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑06 | Self-Improving Loops for Visual Robotic Planning <!-- paper:luo2025silvr --> | <a href="https://arxiv.org/abs/2506.06658"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/brown-palm/silvr) |

[↑ Back to top](#top) · [Category page](papers/world.md)

---

<a id="agent"></a>

## 04 · Skill- and agent-based execution

<a id="agent-skills"></a>

### Skill sequences and task structure

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation <!-- paper:arxiv260920791 --> | <a href="https://arxiv.org/abs/2609.20791"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑05 | UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations <!-- paper:kim2025uniskill --> | <a href="https://arxiv.org/abs/2505.08787"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/KimHanjung/UniSkill) |
| 2025 | Enabling Long(er) Horizon Imitation for Manipulation Tasks by Modeling Subgoal Transitions <!-- paper:jain2025transitions --> | <a href="https://proceedings.mlr.press/v305/jain25b.html"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | [Code](https://github.com/shivam89jain/SGPT-long-horizon-imitation) |
| 2024‑05 | Vision-based Manipulation from Single Human Video with Open-World Object Graphs <!-- paper:zhu2024orion --> | <a href="https://arxiv.org/abs/2405.20321"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑07 | XSkill: Cross Embodiment Skill Discovery <!-- paper:xu2023xskill --> | <a href="https://arxiv.org/abs/2307.09955"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/real-stanford/xskill) |
| 2023‑02 | MimicPlay: Long-Horizon Imitation Learning by Watching Human Play <!-- paper:wang2023mimicplay --> | <a href="https://arxiv.org/abs/2302.12422"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/j96w/MimicPlay) |
| 2023‑02 | One-shot Visual Imitation via Attributed Waypoints and Demonstration Augmentation <!-- paper:chang2023awda --> | <a href="https://arxiv.org/abs/2302.04856"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/MatthewChang/osvi-awda) |
| 2018‑03 | Semi-parametric Topological Memory for Navigation <!-- paper:savinov2018sptm --> | <a href="https://arxiv.org/abs/1803.00653"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/nsavinov/SPTM) |
| 2017‑10 | Neural Task Programming: Learning to Generalize Across Hierarchical Tasks <!-- paper:xu2017ntp --> | <a href="https://arxiv.org/abs/1710.01813"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/StanfordVL/ntp) |

<a id="agent-programs"></a>

### Programs, tools, and hierarchical control

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | RAPID: Robot Agentic Programming from Demonstrations <!-- paper:arxiv260930249 --> | <a href="https://arxiv.org/abs/2609.30249"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Coding Agents for Generalized Task and Motion Planning Problems <!-- paper:arxiv260930233 --> | <a href="https://arxiv.org/abs/2609.30233"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/tomsilver/robocode) |
| 2026‑09 | Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation <!-- paper:arxiv260929389 --> | <a href="https://arxiv.org/abs/2609.29389"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics <!-- paper:arxiv260927308 --> | <a href="https://arxiv.org/abs/2609.27308"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/EmbodiedSWE/EmbodiedSWE) |
| 2026‑09 | Generalizing Manipulation Skills with a Local Coding Agent <!-- paper:arxiv260926499 --> | <a href="https://arxiv.org/abs/2609.26499"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Transferring the Intelligence of VLMs to Robotic Control <!-- paper:arxiv260922966 --> | <a href="https://arxiv.org/abs/2609.22966"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Hugo-AGI/RoboDawn) |
| 2026‑09 | VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control <!-- paper:arxiv260919554 --> | <a href="https://arxiv.org/abs/2609.19554"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/zhangzhongbo2213/VABench) |
| 2026‑09 | Navi-Agent: Unlocalized Monocular Navigation Agent <!-- paper:arxiv260920388 --> | <a href="https://arxiv.org/abs/2609.20388"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories <!-- paper:extra260918435 --> | <a href="https://arxiv.org/abs/2609.18435"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/tsudalab/WetRobo) |
| 2026‑09 | In-Context Robot Learning with VLM Agents <!-- paper:cheng2026gptpolicyeval --> | <a href="https://arxiv.org/abs/2609.19138"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/cheng-haha/GPT-Policy) |
| 2026‑09 | Show-Harness: Just a VLM Agent Can Play Robots <!-- paper:chen2026showharness --> | <a href="https://arxiv.org/abs/2609.10522"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/showlab/Show-Harness) |
| 2026‑08 | ETA: A New Agentic Paradigm for Embodied Tasks <!-- paper:chen2026eta --> | <a href="https://arxiv.org/abs/2608.03924"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/OpenMOSS/OpenETA) |
| 2026‑07 | A Few Words Go a Long Way: Language Guided Robot Policy Synthesis <!-- paper:chen2026architect --> | <a href="https://arxiv.org/abs/2607.23784"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/robo-architect/architect-franka) |
| 2026‑07 | Addressing the Orchestration Gap in Generalist Robots via Physical Agency <!-- paper:galanti2026physicalagency --> | <a href="https://arxiv.org/abs/2607.21725"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents <!-- paper:arxiv260708448 --> | <a href="https://arxiv.org/abs/2607.08448"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/RLinf/RPent) |
| 2026‑06 | What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents <!-- paper:hu2026orchestrating --> | <a href="https://arxiv.org/abs/2606.10267"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑05 | When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution <!-- paper:arxiv260514504 --> | <a href="https://arxiv.org/abs/2605.14504"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation <!-- paper:arxiv260322435 --> | <a href="https://arxiv.org/abs/2603.22435"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/capgym/cap-x) |
| 2026‑03 | RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks <!-- paper:cui2026roboclaw --> | <a href="https://arxiv.org/abs/2603.11558"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/RoboClaw-Robotics/RoboClaw) |
| 2026‑02 | Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control <!-- paper:chen2026steerable --> | <a href="https://arxiv.org/abs/2602.13193"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/steerable-policies/steerable-policies-bridge) |
| 2024‑11 | MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation <!-- paper:singh2024malmm --> | <a href="https://arxiv.org/abs/2411.17636"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑11 | Select2Plan: Training-Free ICL-Based Planning Through VQA and Memory Retrieval <!-- paper:buoso2024select2plan --> | <a href="https://arxiv.org/abs/2411.04006"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/lambdavi/S2P) |
| 2024‑06 | Trust the PRoC3S: Solving Long-Horizon Robotics Problems with LLMs and Constraint Satisfaction <!-- paper:curtis2025proc3s --> | <a href="https://arxiv.org/abs/2406.05572"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Learning-and-Intelligent-Systems/proc3s) |
| 2023‑08 | A²Nav: Action-Aware Zero-Shot Robot Navigation by Exploiting Vision-and-Language Ability of Foundation Models <!-- paper:chen2023a2nav --> | <a href="https://arxiv.org/abs/2308.07997"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑07 | VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models <!-- paper:huang2023voxposer --> | <a href="https://arxiv.org/abs/2307.05973"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/huangwl18/VoxPoser) |
| 2023‑06 | SayTap: Language to Quadrupedal Locomotion <!-- paper:tang2023saytap --> | <a href="https://arxiv.org/abs/2306.07580"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑09 | ProgPrompt: Generating Situated Robot Task Plans using Large Language Models <!-- paper:singh2022progprompt --> | <a href="https://arxiv.org/abs/2209.11302"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/NVlabs/progprompt-vh) |
| 2022‑09 | Code as Policies: Language Model Programs for Embodied Control <!-- paper:liang2022codeaspolicies --> | <a href="https://arxiv.org/abs/2209.07753"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/google-research/google-research/tree/master/code_as_policies) |
| 2022‑07 | Inner Monologue: Embodied Reasoning through Planning with Language Models <!-- paper:huang2022monologue --> | <a href="https://arxiv.org/abs/2207.05608"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑07 | LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action <!-- paper:shah2022lmnav --> | <a href="https://arxiv.org/abs/2207.04429"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/blazejosinski/lm_nav) |
| 2022‑04 | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances <!-- paper:ahn2022saycan --> | <a href="https://arxiv.org/abs/2204.01691"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/google-research/google-research/tree/master/saycan) |

<a id="agent-memory"></a>

### Retained guidance and reusable knowledge

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal <!-- paper:arxiv260929964 --> | <a href="https://arxiv.org/abs/2609.29964"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning <!-- paper:arxiv260929394 --> | <a href="https://arxiv.org/abs/2609.29394"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | ADM-Planner: LLM-Guided Long-Horizon Planning for Mobile Manipulators with Attention-Enhanced Dynamic Memory <!-- paper:arxiv260929212 --> | <a href="https://arxiv.org/abs/2609.29212"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution <!-- paper:arxiv260929204 --> | <a href="https://arxiv.org/abs/2609.29204"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Haaareally/AdaHVLA-Adaptive_Harness_VLA) |
| 2026‑09 | OCC4M: Object-Centric 4D Memory for Spatiotemporal Reasoning in Long-Horizon Manipulation <!-- paper:arxiv260928798 --> | <a href="https://arxiv.org/abs/2609.28798"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs <!-- paper:arxiv260928530 --> | <a href="https://arxiv.org/abs/2609.28530"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Learning and Transferring Closed-Loop Robot Software <!-- paper:arxiv260919906 --> | <a href="https://arxiv.org/abs/2609.19906"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | CoreSense: Traceable Failure Recall and Conflict-Aware Belief Gating for Auditable Robot Decisions <!-- paper:arxiv260919512 --> | <a href="https://arxiv.org/abs/2609.19512"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | MessyMem: Learning-from-Doing Memory for Mobile Manipulation <!-- paper:extra260915976 --> | <a href="https://arxiv.org/abs/2609.15976"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation <!-- paper:extra260911308 --> | <a href="https://arxiv.org/abs/2609.11308"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Safe Task Planning with Long-Term Graph Memory for Embodied Agents <!-- paper:extra260908444 --> | <a href="https://arxiv.org/abs/2609.08444"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/lty759/SafeMem) |
| 2026‑08 | Mimir: A Neuro-Symbolic Memory System with Dynamic Grounding for Embodied Agents in Interactive Environments <!-- paper:arxiv260804933 --> | <a href="https://arxiv.org/abs/2608.04933"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies <!-- paper:arxiv260829537 --> | <a href="https://arxiv.org/abs/2608.29537"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation <!-- paper:liu2026hamvln --> | <a href="https://arxiv.org/abs/2607.29600"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning <!-- paper:huang2026roboharness --> | <a href="https://arxiv.org/abs/2607.18060"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | ASPIRE: Agentic /Skills Discovery for Robotics <!-- paper:lu2026aspire --> | <a href="https://arxiv.org/abs/2607.00272"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/NVlabs/ASPIRE) |
| 2026‑06 | Guava: An Effective and Universal Harness for Embodied Manipulation <!-- paper:liu2026guava --> | <a href="https://arxiv.org/abs/2606.18363"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑05 | EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents <!-- paper:ju2026embodiskill --> | <a href="https://arxiv.org/abs/2605.10332"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval <!-- paper:li2026cmmrvln --> | <a href="https://arxiv.org/abs/2603.07997"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation <!-- paper:xie2026uniskillrepo --> | <a href="https://arxiv.org/abs/2603.02623"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation <!-- paper:kumar2026aor --> | <a href="https://arxiv.org/abs/2603.04466"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑09 | Growing with Your Embodied Agent: A Human-in-the-Loop Lifelong Code Generation Framework for Long-Horizon Manipulation Skills <!-- paper:arxiv250918597 --> | <a href="https://arxiv.org/abs/2509.18597"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑06 | Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models <!-- paper:tziafas2024lrll --> | <a href="https://arxiv.org/abs/2406.18746"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑06 | VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought <!-- paper:sarch2024ical --> | <a href="https://arxiv.org/abs/2406.14596"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Gabesarch/ICAL) |
| 2024‑02 | Learning to Learn Faster from Human Feedback with Language Model Predictive Control <!-- paper:liang2024lmpc --> | <a href="https://arxiv.org/abs/2402.11450"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑11 | Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections <!-- paper:zha2023droc --> | <a href="https://arxiv.org/abs/2311.10678"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Stanford-ILIAD/droc) |

<a id="agent-grounding"></a>

### Grounding, feedback, and failure recovery

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | Body-Grounded Replanning for Physically Adaptive Manipulation <!-- paper:arxiv260930024 --> | <a href="https://arxiv.org/abs/2609.30024"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Training-Free Action Correction for VLA Model Failures via Language Feedback <!-- paper:arxiv260829967 --> | <a href="https://arxiv.org/abs/2608.29967"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/owenk3/correct_vla) |
| 2026‑08 | PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration <!-- paper:physcap2026 --> | <a href="https://arxiv.org/abs/2608.21031"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents <!-- paper:arxiv260817129 --> | <a href="https://arxiv.org/abs/2608.17129"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation <!-- paper:chen2026volo --> | <a href="https://arxiv.org/abs/2606.07723"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/NVlabs/VoLoAgent) |
| 2026‑05 | Affordance Agent Harness: Verification-Gated Skill Orchestration <!-- paper:huang2026affordanceharness --> | <a href="https://arxiv.org/abs/2605.00663"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑05 | Where to Look: Can Foundation Models Reach a Target Viewpoint Through Active Exploration? <!-- paper:arxiv260601247 --> | <a href="https://arxiv.org/abs/2606.01247"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/aim-uofa/TVRBench) |
| 2026‑05 | From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation <!-- paper:arxiv260511951 --> | <a href="https://arxiv.org/abs/2605.11951"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/EDEM-AI/AgentChord) |
| 2025‑08 | In-Context Iterative Policy Improvement for Dynamic Manipulation <!-- paper:merwe2025icpi --> | <a href="https://arxiv.org/abs/2508.15021"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑08 | In-situ Value-aligned Human-Robot Interactions with Physical Constraints <!-- paper:li2025iclhf --> | <a href="https://arxiv.org/abs/2508.07606"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/ICLHF/ICLHF) |
| 2024‑09 | VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments <!-- paper:elnoor2024vlmgronav --> | <a href="https://arxiv.org/abs/2409.20445"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑09 | RACER: Rich Language-Guided Failure Recovery Policies for Imitation Learning <!-- paper:dai2024racer --> | <a href="https://arxiv.org/abs/2409.14674"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/sled-group/RACER) |
| 2024‑02 | Introspective Planning: Aligning Robots&#x27; Uncertainty with Inherent Task Ambiguity <!-- paper:liang2024introplan --> | <a href="https://arxiv.org/abs/2402.06529"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/kevinliang888/IntroPlan) |
| 2023‑07 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners <!-- paper:ren2023knowno --> | <a href="https://arxiv.org/abs/2307.01928"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/google-research/google-research/tree/master/language_model_uncertainty) |
| 2023‑06 | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction <!-- paper:liu2023reflect --> | <a href="https://arxiv.org/abs/2306.15724"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/columbia-ai-robotics/reflect) |

<a id="agent-improvement"></a>

### Agent-directed learning and self-improvement

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | HarnessPAI: An Evolving Harness for Physical AI <!-- paper:arxiv260929166 --> | <a href="https://arxiv.org/abs/2609.29166"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention <!-- paper:arxiv260914633 --> | <a href="https://arxiv.org/abs/2609.14633"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | RoboRSI: Stable, Efficient, and Reusable Robot Self-Evolution in Complex Real-World Environments <!-- paper:noematrix2026roborsi --> | <a href="https://lab.noematrix.ai/blog/2-roborsi/"><img src="https://img.shields.io/badge/Research_Blog-52616b.svg?style=flat-square" alt="Research_Blog" height="24"></a> | [Code](https://github.com/nssmd/RoboRSI) |
| 2026‑08 | SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies <!-- paper:arxiv260831167 --> | <a href="https://arxiv.org/abs/2608.31167"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | EXIMO: VLM Guided Exploration of VLA Policies <!-- paper:arxiv260819891 --> | <a href="https://arxiv.org/abs/2608.19891"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence <!-- paper:arxiv260816590 --> | <a href="https://arxiv.org/abs/2608.16590"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Teach and Grow: An Agent-Centered Architecture for General Robot Learning <!-- paper:arxiv260817209 --> | <a href="https://arxiv.org/abs/2608.17209"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/IRMVLab/TGL) |
| 2026‑08 | Self-Evolving Embodied Agents via Skill-Harness Evolution <!-- paper:wang2026shaper --> | <a href="https://arxiv.org/abs/2608.11350"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | ENPIRE: Agentic Robot Policy Self-Improvement in the Real World <!-- paper:xiao2026enpire --> | <a href="https://arxiv.org/abs/2606.19980"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | Playful Agentic Robot Learning <!-- paper:arxiv260619419 --> | <a href="https://arxiv.org/abs/2606.19419"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Playful-RATs/rats) |
| 2024‑01 | AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents <!-- paper:ahn2024autort --> | <a href="https://arxiv.org/abs/2401.12963"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

[↑ Back to top](#top) · [Category page](papers/agent.md)

---

<a id="navigation"></a>

## 05 · Navigation: four context types

<a id="navigation-routes"></a>

### Route demonstrations

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2020‑10 | Path-Following Navigation Network Using Sparse Visual Memory <!-- paper:yoo2020sparsepath --> | <a href="https://doi.org/10.23919/ICCAS50221.2020.9268247"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 2018‑12 | Visual Memory for Robust Path Following <!-- paper:kumar2018rpf --> | <a href="https://arxiv.org/abs/1812.00940"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2018‑04 | Zero-Shot Visual Imitation <!-- paper:pathak2018zeroshot --> | <a href="https://arxiv.org/abs/1804.08606"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/pathak22/zeroshot-imitation) |

<a id="navigation-environment"></a>

### Environment observations

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | NavProbe: Evidence-Grounded Reasoning with Active Memory Retrieval for Zero-Shot Navigation <!-- paper:arxiv260927526 --> | <a href="https://arxiv.org/abs/2609.27526"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | SparseNav: Instruction-conditioned Sparse Semantic Perception for Training-Free Vision-Language Navigation <!-- paper:arxiv260926408 --> | <a href="https://arxiv.org/abs/2609.26408"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑10 | ReLIC: A Recipe for 64k Steps of In-Context Reinforcement Learning for Embodied AI <!-- paper:elawady2024relic --> | <a href="https://arxiv.org/abs/2410.02751"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/aielawady/relic) |
| 2024‑08 | NOLO: Navigate Only Look Once <!-- paper:zhou2024nolo --> | <a href="https://arxiv.org/abs/2408.01384"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/zhoubohan0/NOLO) |
| 2018‑03 | Semi-parametric Topological Memory for Navigation <!-- paper:savinov2018sptm --> | <a href="https://arxiv.org/abs/1803.00653"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/nsavinov/SPTM) |

<a id="navigation-examples"></a>

### Instruction and decision examples

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2024‑11 | Select2Plan: Training-Free ICL-Based Planning Through VQA and Memory Retrieval <!-- paper:buoso2024select2plan --> | <a href="https://arxiv.org/abs/2411.04006"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/lambdavi/S2P) |
| 2023‑08 | A²Nav: Action-Aware Zero-Shot Robot Navigation by Exploiting Vision-and-Language Ability of Foundation Models <!-- paper:chen2023a2nav --> | <a href="https://arxiv.org/abs/2308.07997"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑07 | LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action <!-- paper:shah2022lmnav --> | <a href="https://arxiv.org/abs/2207.04429"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/blazejosinski/lm_nav) |

<a id="navigation-feedback"></a>

### Outcome feedback

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | Talk2Escape: Conversational Grounding for Vision-and-Language Navigation <!-- paper:arxiv260928296 --> | <a href="https://arxiv.org/abs/2609.28296"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation <!-- paper:liu2026hamvln --> | <a href="https://arxiv.org/abs/2607.29600"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval <!-- paper:li2026cmmrvln --> | <a href="https://arxiv.org/abs/2603.07997"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑09 | VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments <!-- paper:elnoor2024vlmgronav --> | <a href="https://arxiv.org/abs/2409.20445"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

[↑ Back to top](#top) · [Category page](papers/navigation.md)

---

<a id="improvement"></a>

## 06 · Physical self-improvement

<a id="improvement-context"></a>

### Interaction context

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | Zeva-Ego: Egocentric Mid-Training with In-Context Causal Learning for Robot Manipulation <!-- paper:arxiv260924411 --> | <a href="https://arxiv.org/abs/2609.24411"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/air-embodied-brain/Zeva/tree/feature/zeva_ego) |
| 2026‑09 | RopeFormer: Cross-Trial Adaptation from Interaction History for Dynamic Rope Manipulation <!-- paper:arxiv260923432 --> | <a href="https://arxiv.org/abs/2609.23432"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="improvement-artifacts"></a>

### Executable artifacts

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | RoboRSI: Stable, Efficient, and Reusable Robot Self-Evolution in Complex Real-World Environments <!-- paper:noematrix2026roborsi --> | <a href="https://lab.noematrix.ai/blog/2-roborsi/"><img src="https://img.shields.io/badge/Research_Blog-52616b.svg?style=flat-square" alt="Research_Blog" height="24"></a> | [Code](https://github.com/nssmd/RoboRSI) |
| 2026‑06 | ENPIRE: Agentic Robot Policy Self-Improvement in the Real World <!-- paper:xiao2026enpire --> | <a href="https://arxiv.org/abs/2606.19980"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="improvement-parameters"></a>

### Neural components

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | MetaPusher: Meta Learning and Planning for Nonprehensile Manipulation of Unseen Objects with Rapid Online Adaption <!-- paper:arxiv260921122 --> | <a href="https://arxiv.org/abs/2609.21122"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention <!-- paper:arxiv260914633 --> | <a href="https://arxiv.org/abs/2609.14633"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="improvement-acquisition"></a>

### Acquisition procedures

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2024‑06 | DrEureka: Language Model Guided Sim-To-Real Transfer <!-- paper:ma2024dreureka --> | <a href="https://arxiv.org/abs/2406.01967"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/eureka-research/DrEureka) |
| 2024‑02 | Learning to Learn Faster from Human Feedback with Language Model Predictive Control <!-- paper:liang2024lmpc --> | <a href="https://arxiv.org/abs/2402.11450"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑10 | Eureka: Human-Level Reward Design via Coding Large Language Models <!-- paper:ma2023eureka --> | <a href="https://arxiv.org/abs/2310.12931"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/eureka-research/Eureka) |

[↑ Back to top](#top) · [Category page](papers/improvement.md)

---

<a id="shared"></a>

## 07 · Shared correspondence and memory mechanisms

<a id="shared-correspondence"></a>

### Cross-embodiment representations

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2024‑06 | RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics <!-- paper:yuan2024robopoint --> | <a href="https://arxiv.org/abs/2406.10721"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/wentaoyuan/RoboPoint) |
| 2021‑06 | XIRL: Cross-embodiment Inverse Reinforcement Learning <!-- paper:zakka2021xirl --> | <a href="https://arxiv.org/abs/2106.03911"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/google-research/google-research/tree/master/xirl) |
| 2017‑04 | Time-Contrastive Networks: Self-Supervised Learning from Video <!-- paper:sermanet2017tcn --> | <a href="https://arxiv.org/abs/1704.06888"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="shared-memory"></a>

### Persistent scene and world representations

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | HitMem: Hierarchical Temporal 3D Memory with Multi-Modal Context-Aware Retrieval for Dynamic Environments <!-- paper:arxiv260900950 --> | <a href="https://arxiv.org/abs/2609.00950"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments <!-- paper:arxiv260900619 --> | <a href="https://arxiv.org/abs/2609.00619"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding <!-- paper:arxiv260819059 --> | <a href="https://arxiv.org/abs/2608.19059"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation <!-- paper:arxiv260618960 --> | <a href="https://arxiv.org/abs/2606.18960"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑01 | Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments <!-- paper:arxiv260101075 --> | <a href="https://arxiv.org/abs/2601.01075"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/hlillemark/flowm) |

[↑ Back to top](#top) · [Category page](papers/shared.md)

---

<a id="data"></a>

## 08 · Data and acquisition interfaces

<a id="data-robot"></a>

### Robot demonstrations and teleoperation

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | AGIBOT WORLD 2026 Theme 3: Reinforcement Learning <!-- paper:agibot2026corrections --> | <a href="https://agibot.com/article/231/detail/95.html"><img src="https://img.shields.io/badge/Report-52616b.svg?style=flat-square" alt="Report" height="24"></a> | — |
| 2026 | AgiBot World 2026 <!-- paper:agibot2026release --> | <a href="https://huggingface.co/datasets/agibot-world/AgiBotWorld2026"><img src="https://img.shields.io/badge/Dataset-52616b.svg?style=flat-square" alt="Dataset" height="24"></a> | — |
| 2025‑12 | RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dataset for Generalizable Embodied Intelligence <!-- paper:robomind2025v2 --> | <a href="https://arxiv.org/abs/2512.24653"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑11 | RoboCOIN: An Open-Sourced Bimanual Robotic Data Collection for Integrated Manipulation <!-- paper:robocoin2025 --> | <a href="https://arxiv.org/abs/2511.17441"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑03 | AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems <!-- paper:agibot2025 --> | <a href="https://arxiv.org/abs/2503.06669"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/OpenDriveLab/AgiBot-World) |
| 2024‑12 | RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation <!-- paper:robomind2024 --> | <a href="https://arxiv.org/abs/2412.13877"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑03 | DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset <!-- paper:khazatsky2024droid --> | <a href="https://arxiv.org/abs/2403.12945"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/droid-dataset/droid) |
| 2023‑08 | BridgeData V2: A Dataset for Robot Learning at Scale <!-- paper:walke2023bridge --> | <a href="https://arxiv.org/abs/2308.12952"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/rail-berkeley/bridge_data_v2) |
| 2023‑07 | RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot <!-- paper:fang2023rh20t --> | <a href="https://arxiv.org/abs/2307.00595"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/rh20t/rh20t_api) |
| 2021‑09 | Bridge Data: Boosting Generalization of Robotic Skills with Cross-Domain Datasets <!-- paper:bridge2021 --> | <a href="https://arxiv.org/abs/2109.13396"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="data-umi"></a>

### Handheld and universal manipulation interfaces

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑07 | HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone <!-- paper:simpleai2026hifiumi --> | <a href="https://arxiv.org/abs/2607.25895"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale <!-- paper:ohkawa2026yubi --> | <a href="https://arxiv.org/abs/2606.10244"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/airoa-org/yubi-sw) |
| 2026‑04 | OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction <!-- paper:luo2026omniumi --> | <a href="https://arxiv.org/abs/2604.10647"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑09 | FastUMI: A Scalable and Hardware-Independent Universal Manipulation Interface with Dataset <!-- paper:zhaxizhuoma2024fastumi --> | <a href="https://arxiv.org/abs/2409.19499"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑07 | UMI on Legs: Making Manipulation Policies Mobile with Manipulation-Centric Whole-body Controllers <!-- paper:ha2024umilegs --> | <a href="https://arxiv.org/abs/2407.10353"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/real-stanford/umi-on-legs) |
| 2024‑02 | Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots <!-- paper:chi2024umi --> | <a href="https://arxiv.org/abs/2402.10329"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/real-stanford/universal_manipulation_interface) |

<a id="data-human"></a>

### Human video and egocentric data

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑07 | ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine <!-- paper:cao2026acedata --> | <a href="https://arxiv.org/abs/2607.28625"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning <!-- paper:aoe2026openaoe --> | <a href="https://arxiv.org/abs/2607.14183"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑06 | ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining <!-- paper:li2026aceego --> | <a href="https://arxiv.org/abs/2606.17200"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World <!-- paper:punamiya2026egoverse --> | <a href="https://arxiv.org/abs/2604.07607"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/GaTech-RL2/EgoVerse) |
| 2026‑02 | EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data <!-- paper:egoscale2026 --> | <a href="https://arxiv.org/abs/2602.16710"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑05 | EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video <!-- paper:egodex2025 --> | <a href="https://arxiv.org/abs/2505.11709"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/apple/ml-egodex) |
| 2024‑11 | HOT3D: Hand and Object Tracking in 3D from Egocentric Multi-View Videos <!-- paper:hot3d2025 --> | <a href="https://arxiv.org/abs/2411.19167"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑11 | Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives <!-- paper:grauman2023egoexo4d --> | <a href="https://arxiv.org/abs/2311.18259"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑09 | HoloAssist: an Egocentric Human Interaction Dataset for Interactive AI Assistants in the Real World <!-- paper:holoassist2023 --> | <a href="https://arxiv.org/abs/2309.17024"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Ember-HoloAssist/holoassist-release) |
| 2022‑03 | Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities <!-- paper:assembly1012022 --> | <a href="https://arxiv.org/abs/2203.14712"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/assembly-101/assembly101-temporal-action-segmentation) |
| 2022‑03 | HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction <!-- paper:hoi4d2022 --> | <a href="https://arxiv.org/abs/2203.01577"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2021‑10 | Ego4D: Around the World in 3,000 Hours of Egocentric Video <!-- paper:grauman2021ego4d --> | <a href="https://arxiv.org/abs/2110.07058"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/EGO4D/episodic-memory) |
| 2020‑06 | Rescaling Egocentric Vision <!-- paper:damen2020epic100 --> | <a href="https://arxiv.org/abs/2006.13256"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2017‑06 | The &quot;something something&quot; video database for learning and evaluating visual common sense <!-- paper:goyal2017something --> | <a href="https://arxiv.org/abs/1706.04261"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="data-synthesis"></a>

### Simulation and demonstration synthesis

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | KnowDemo: Knowledge-Guided Robot Demonstration Generation from Human Videos <!-- paper:arxiv260921229 --> | <a href="https://arxiv.org/abs/2609.21229"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | HuRo: Robotizing Human Videos for Scalable VLA Pretraining <!-- paper:extra260910706 --> | <a href="https://arxiv.org/abs/2609.10706"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/3587jjh/HuRo) |
| 2026‑09 | RoboTok: An Internet-Scale Data Engine for Human Demonstration Retrieval and Dexterous Manipulation Learning <!-- paper:qian2026robotok --> | <a href="https://arxiv.org/abs/2609.03199"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation <!-- paper:lin2026simdex --> | <a href="https://arxiv.org/abs/2608.04196"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data <!-- paper:wang2026ego2robot --> | <a href="https://arxiv.org/abs/2608.02580"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑05 | SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning <!-- paper:arxiv260509423 --> | <a href="https://arxiv.org/abs/2605.09423"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots <!-- paper:arxiv260304356 --> | <a href="https://arxiv.org/abs/2603.04356"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑12 | One-Shot Real-World Demonstration Synthesis for Scalable Bimanual Manipulation <!-- paper:zhou2026bidemosyn --> | <a href="https://arxiv.org/abs/2512.09297"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/hnuzhy/BiRoMan) |
| 2025‑04 | Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation <!-- paper:robosplat2025 --> | <a href="https://arxiv.org/abs/2504.13175"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/InternRobotics/RoboSplat) |
| 2025‑01 | You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations <!-- paper:zhou2025yoto --> | <a href="https://arxiv.org/abs/2501.14208"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/hnuzhy/YOTO) |
| 2024‑06 | RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots <!-- paper:robocasa2024 --> | <a href="https://arxiv.org/abs/2406.02523"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/robocasa/robocasa) |
| 2024‑05 | OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code <!-- paper:faldor2024omniepic --> | <a href="https://arxiv.org/abs/2405.15568"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑03 | EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents <!-- paper:zala2024envgen --> | <a href="https://arxiv.org/abs/2403.12014"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/aszala/envgen) |
| 2023‑10 | MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations <!-- paper:mandlekar2023mimicgen --> | <a href="https://arxiv.org/abs/2310.17596"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/NVlabs/mimicgen_environments) |

[↑ Back to top](#top) · [Category page](papers/data.md)

---

<a id="training"></a>

## 09 · Training and improvement

<a id="training-scaling"></a>

### Training coverage and scaling

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | Public Summary of Training Content for GPT-6 Astra <!-- paper:openai2026astratraining --> | <a href="https://cdn.openai.com/pdf/gpt-6-astra-eu-ai-act-public-summary-of-training-content.pdf"><img src="https://img.shields.io/badge/Report-52616b.svg?style=flat-square" alt="Report" height="24"></a> | — |
| 2025‑07 | Is Diversity All You Need for Scalable Robotic Manipulation? <!-- paper:arxiv250706219 --> | <a href="https://arxiv.org/abs/2507.06219"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/OpenDriveLab/AgiBot-World) |
| 2022‑10 | Scaling Instruction-Finetuned Language Models <!-- paper:chung2022flan --> | <a href="https://arxiv.org/abs/2210.11416"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2021‑04 | MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale <!-- paper:mtopt2021 --> | <a href="https://arxiv.org/abs/2104.08212"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="training-adaptation"></a>

### Learning from observation and embodiment transfer

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑07 | A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation <!-- paper:feng2026regrind --> | <a href="https://arxiv.org/abs/2607.11874"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/yunhaif/regrind) |
| 2022‑06 | Human-to-Robot Imitation in the Wild <!-- paper:bahl2022whirl --> | <a href="https://arxiv.org/abs/2207.09450"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑02 | REvolveR: Continuous Evolutionary Models for Robot-to-robot Policy Transfer <!-- paper:liu2022revolver --> | <a href="https://arxiv.org/abs/2202.05244"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/xingyul/revolver) |
| 2018‑05 | Behavioral Cloning from Observation <!-- paper:torabi2018bco --> | <a href="https://arxiv.org/abs/1805.01954"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="training-interactive"></a>

### Interactive supervision and predictive training

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑05 | PhyWorld: Physics-Faithful World Model for Video Generation <!-- paper:arxiv260519242 --> | <a href="https://arxiv.org/abs/2605.19242"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training <!-- paper:arxiv260421741 --> | <a href="https://arxiv.org/abs/2604.21741"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry <!-- paper:arxiv260401985 --> | <a href="https://arxiv.org/abs/2604.01985"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/world-action-verifier/wav_robot) |
| 2024‑07 | Video In-context Learning: Autoregressive Transformers are Zero-Shot Video Imitators <!-- paper:extra240707356 --> | <a href="https://arxiv.org/abs/2407.07356"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2021‑09 | ThriftyDAgger: Budget-Aware Novelty and Risk Gating for Interactive Imitation Learning <!-- paper:hoque2021thrifty --> | <a href="https://arxiv.org/abs/2109.08273"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2017‑03 | DART: Noise Injection for Robust Imitation Learning <!-- paper:laskey2017dart --> | <a href="https://arxiv.org/abs/1703.09327"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2010‑11 | A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning <!-- paper:ross2011dagger --> | <a href="https://arxiv.org/abs/1011.0686"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="training-improvement"></a>

### Autonomous learning and self-improvement

[Compare context, programs, neural components, and acquisition procedures →](papers/improvement.md)

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2025‑09 | Self-Improving Embodied Foundation Models <!-- paper:ghasemipour2025selfimproving --> | <a href="https://arxiv.org/abs/2509.15155"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑06 | DrEureka: Language Model Guided Sim-To-Real Transfer <!-- paper:ma2024dreureka --> | <a href="https://arxiv.org/abs/2406.01967"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/eureka-research/DrEureka) |
| 2023‑10 | Eureka: Human-Level Reward Design via Coding Large Language Models <!-- paper:ma2023eureka --> | <a href="https://arxiv.org/abs/2310.12931"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/eureka-research/Eureka) |
| 2023‑03 | Self-Improving Robots: End-to-End Autonomous Visuomotor Reinforcement Learning <!-- paper:sharma2023medal --> | <a href="https://arxiv.org/abs/2303.01488"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/rehaanahmad2013/self-improving-robots) |

[↑ Back to top](#top) · [Category page](papers/training.md)

---

<a id="grounding"></a>

## 10 · Grounding and failure assessment

<a id="grounding-assessment"></a>

### Progress, uncertainty, and failure detection

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑06 | Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents <!-- paper:arxiv260623085 --> | <a href="https://arxiv.org/abs/2606.23085"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑03 | Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies <!-- paper:xu2025faildetect --> | <a href="https://arxiv.org/abs/2503.08558"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑11 | Vision Language Models are In-Context Value Learners <!-- paper:arxiv241104549 --> | <a href="https://arxiv.org/abs/2411.04549"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑10 | Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress <!-- paper:agia2024sentinel --> | <a href="https://arxiv.org/abs/2410.04640"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2024‑10 | AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation <!-- paper:duan2024aha --> | <a href="https://arxiv.org/abs/2410.00371"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/NVlabs/AHA) |
| 2012‑03 | Designing Robot Learners that Ask Good Questions <!-- paper:cakmak2012questions --> | <a href="https://homes.cs.washington.edu/~mcakmak/pdfs/2012/cakmak2012hri.pdf"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |

[↑ Back to top](#top) · [Category page](papers/grounding.md)

---

<a id="evaluation"></a>

## 11 · Benchmarks and evaluation

<a id="evaluation-transfer"></a>

### Demonstration use and task transfer

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
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

<a id="evaluation-memory"></a>

### Memory and physical adaptation

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | Memory That Changes Action Is Not Memory That Guides It: Counterfactual Auditing of History-Conditioned Robot Policies <!-- paper:arxiv260927247 --> | <a href="https://arxiv.org/abs/2609.27247"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | MEMOBench: A Process Level Memory Benchmark for Robotic Manipulation <!-- paper:sun2026memobench --> | <a href="https://arxiv.org/abs/2609.07047"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Collab-Gen/MEMOBench) |
| 2026‑08 | PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments <!-- paper:arxiv260814441 --> | <a href="https://arxiv.org/abs/2608.14441"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/thunlp/PACE-Bench) |
| 2026‑06 | WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents <!-- paper:arxiv260618847 --> | <a href="https://arxiv.org/abs/2606.18847"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑03 | RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies <!-- paper:dai2026robomme --> | <a href="https://arxiv.org/abs/2603.04639"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/RoboMME/robomme_benchmark) |
| 2025‑02 | Memory, Benchmark &amp; Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning <!-- paper:cherepanov2025mikasa --> | <a href="https://arxiv.org/abs/2502.10550"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/CognitiveAISystems/MIKASA-Robo) |

<a id="evaluation-execution"></a>

### Physical execution and predictive evaluation

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
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

[↑ Back to top](#top) · [Category page](papers/evaluation.md)

---

<a id="foundations"></a>

## 12 · Foundations and related surveys

<a id="foundations-control"></a>

### Robot control and learning foundations

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2018‑06 | QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation <!-- paper:kalashnikov2018qtopt --> | <a href="https://arxiv.org/abs/1806.10293"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2015‑04 | End-to-End Training of Deep Visuomotor Policies <!-- paper:levine2015visuomotor --> | <a href="https://arxiv.org/abs/1504.00702"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2014 | Towards a Unified Behavior Trees Framework for Robot Control <!-- paper:marzinotto2014bt --> | <a href="https://www.csc.kth.se/~ccs/Publications/icra14b.html"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 2011 | Hierarchical Task and Motion Planning in the Now <!-- paper:kaelbling2011hpn --> | <a href="https://people.csail.mit.edu/tlp/pdf/2011/hpnICRA11Final.pdf"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 2006 | Visual Servo Control, Part I: Basic Approaches <!-- paper:chaumette2006visualservo --> | <a href="https://web.mit.edu/amcp/OldFiles/drg/Chaumette_Part_I.pdf"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 1987 | A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation <!-- paper:khatib1987operational --> | <a href="https://khatib.stanford.edu/publications/pdfs/Khatib_1987_RA.pdf"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 1985 | A Robust Layered Control System for a Mobile Robot <!-- paper:brooks1985subsumption --> | <a href="https://people.csail.mit.edu/brooks/papers/AIM-864.pdf"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 1971 | STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving <!-- paper:fikes1971strips --> | <a href="https://www.sciencedirect.com/science/article/pii/0004370271900105"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |

<a id="foundations-icl"></a>

### In-context learning mechanisms

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2024‑02 | Parallel Structures in Pre-training Data Yield In-Context Learning <!-- paper:chen2024parallel --> | <a href="https://arxiv.org/abs/2402.12530"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑12 | The mechanistic basis of data dependence and abrupt learning in an in-context classification task <!-- paper:reddy2023abrupt --> | <a href="https://arxiv.org/abs/2312.03002"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑10 | Position: Do Pretrained Transformers Learn In-Context by Gradient Descent? <!-- paper:shen2023gradient --> | <a href="https://arxiv.org/abs/2310.08540"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2023‑06 | Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression <!-- paper:raventos2023diversity --> | <a href="https://arxiv.org/abs/2306.15063"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/mansheej/icl-task-diversity) |
| 2023‑04 | Are Emergent Abilities of Large Language Models a Mirage? <!-- paper:schaeffer2023mirage --> | <a href="https://arxiv.org/abs/2304.15004"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑12 | Transformers Learn In-Context by Gradient Descent <!-- paper:vonoswald2022gradient --> | <a href="https://arxiv.org/abs/2212.07677"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/google-research/self-organising-systems/tree/master/transformers_learn_icl_by_gd) |
| 2022‑08 | What Can Transformers Learn In-Context? A Case Study of Simple Function Classes <!-- paper:garg2022functions --> | <a href="https://arxiv.org/abs/2208.01066"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/dtsip/in-context-learning) |
| 2022‑04 | Data Distributional Properties Drive Emergent In-Context Learning in Transformers <!-- paper:chan2022distribution --> | <a href="https://arxiv.org/abs/2205.05055"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/deepmind/emergent_in_context_learning) |
| 2022‑02 | Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? <!-- paper:min2022demonstrations --> | <a href="https://arxiv.org/abs/2202.12837"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Alrope123/rethinking-demonstrations) |
| 2021‑11 | An Explanation of In-context Learning as Implicit Bayesian Inference <!-- paper:xie2021bayesian --> | <a href="https://arxiv.org/abs/2111.02080"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2021‑10 | MetaICL: Learning to Learn In Context <!-- paper:min2022metaicl --> | <a href="https://arxiv.org/abs/2110.15943"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/facebookresearch/MetaICL) |
| 2020‑05 | Language Models are Few-Shot Learners <!-- paper:brown2020fewshot --> | <a href="https://arxiv.org/abs/2005.14165"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2019‑05 | Causal Confusion in Imitation Learning <!-- paper:dehaan2019causal --> | <a href="https://arxiv.org/abs/1905.11979"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2017‑06 | Attention Is All You Need <!-- paper:vaswani2017attention --> | <a href="https://arxiv.org/abs/1706.03762"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |

<a id="foundations-surveys"></a>

### Surveys and research directions

| Date | Title | Paper | Code |
| :---: | :--- | :---: | :---: |
| 2026‑09 | In-Context Learning from Demonstrations for Robotic Manipulation: A Survey <!-- paper:li2026demonstrationiclsurvey --> | <a href="https://www.preprints.org/manuscript/202609.0780"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 2026‑09 | World-Action Models for Robot Learning and Control: A Survey <!-- paper:lu2026wamsurvey --> | <a href="https://arxiv.org/abs/2609.16074"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | Deploying Foundation Models for Embodied Navigation <!-- paper:arxiv260925666 --> | <a href="https://arxiv.org/abs/2609.25666"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑09 | The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement <!-- paper:duan2026rsisurvey --> | <a href="https://arxiv.org/abs/2609.11873"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills <!-- paper:jena2026weightsskills --> | <a href="https://arxiv.org/abs/2608.01851"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑08 | The Embodiment Gap in Robot Foundation Models <!-- paper:domae2026embodimentgap --> | <a href="https://arxiv.org/abs/2608.18433"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑07 | Data Pyramid for Embodied Manipulation: A Survey <!-- paper:arxiv260724744 --> | <a href="https://arxiv.org/abs/2607.24744"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Jasper-aaa/Awesome-Embodied-Data-Pyramid) |
| 2026‑07 | In-Context Reinforcement Learning under Non-Stationarity: A Survey <!-- paper:run2026nonstationary --> | <a href="https://arxiv.org/abs/2607.11906"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑05 | World Action Models: The Next Frontier in Embodied AI <!-- paper:survey2026wam --> | <a href="https://arxiv.org/abs/2605.12090"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | World Model for Robot Learning: A Comprehensive Survey <!-- paper:hou2026worldmodel --> | <a href="https://arxiv.org/abs/2605.00080"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2026‑04 | Robot Learning from Human Videos: A Survey <!-- paper:ma2026humanvideosurvey --> | <a href="https://arxiv.org/abs/2604.27621"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos) |
| 2026‑04 | Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines <!-- paper:wang2026vladata --> | <a href="https://arxiv.org/abs/2604.23001"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑12 | Memory in the Age of AI Agents <!-- paper:hu2025agentmemory --> | <a href="https://arxiv.org/abs/2512.13564"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑10 | A Comprehensive Survey on World Models for Embodied AI <!-- paper:li2025embodiedwm --> | <a href="https://arxiv.org/abs/2510.16732"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | [Code](https://github.com/Li-Zn-H/AwesomeWorldModels) |
| 2025‑08 | Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey <!-- paper:shao2025vlasurvey --> | <a href="https://arxiv.org/abs/2508.13073"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2025‑02 | A Survey of In-Context Reinforcement Learning <!-- paper:moeini2025icrlsurvey --> | <a href="https://arxiv.org/abs/2502.07978"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2022‑12 | A Survey on In-context Learning <!-- paper:dong2024iclsurvey --> | <a href="https://arxiv.org/abs/2301.00234"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2020‑05 | Recent Advances in Robot Learning from Demonstration <!-- paper:ravichandar2020survey --> | <a href="https://www.annualreviews.org/content/journals/10.1146/annurev-control-100819-063206"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |
| 2020‑04 | Meta-Learning in Neural Networks: A Survey <!-- paper:hospedales2022metalearning --> | <a href="https://arxiv.org/abs/2004.05439"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2019‑06 | Continual Learning for Robotics: Definition, Framework, Learning Strategies, Opportunities and Challenges <!-- paper:lesort2019continual --> | <a href="https://arxiv.org/abs/1907.00182"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat-square" alt="arXiv" height="24"></a> | — |
| 2008‑11 | A Survey of Robot Learning from Demonstration <!-- paper:argall2009survey --> | <a href="https://publications.ri.cmu.edu/a-survey-of-robot-learning-from-demonstration"><img src="https://img.shields.io/badge/Paper-52616b.svg?style=flat-square" alt="Paper" height="24"></a> | — |

[↑ Back to top](#top) · [Category page](papers/foundations.md)
