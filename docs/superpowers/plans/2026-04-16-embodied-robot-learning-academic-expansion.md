# Embodied Robot Learning Academic Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the embodied AI and robot learning sections into bilingual academic-style technical documentation.

**Architecture:** Keep the existing Sphinx/MyST documentation structure. Convert `embodied_ai/index.md` and `robot_learning/index.md` into section landing pages, then add matched Chinese and English child pages with identical slugs. Each detailed page should read as concise research documentation: problem setting, formalization or system view, implementation notes, experimental protocol, limitations, and references.

**Tech Stack:** Sphinx, MyST Markdown, Read the Docs theme, bilingual Markdown content.

---

## File Structure

Modify:

- `docs/source/zh_CN/embodied_ai/index.md`
- `docs/source/en/embodied_ai/index.md`
- `docs/source/zh_CN/robot_learning/index.md`
- `docs/source/en/robot_learning/index.md`

Create:

- `docs/source/zh_CN/embodied_ai/embodiment_and_pomdp.md`
- `docs/source/zh_CN/embodied_ai/observation_action_spaces.md`
- `docs/source/zh_CN/embodied_ai/simulation_and_real_robot_constraints.md`
- `docs/source/zh_CN/embodied_ai/evaluation.md`
- `docs/source/en/embodied_ai/embodiment_and_pomdp.md`
- `docs/source/en/embodied_ai/observation_action_spaces.md`
- `docs/source/en/embodied_ai/simulation_and_real_robot_constraints.md`
- `docs/source/en/embodied_ai/evaluation.md`
- `docs/source/zh_CN/robot_learning/locomotion.md`
- `docs/source/zh_CN/robot_learning/loco_manipulation.md`
- `docs/source/zh_CN/robot_learning/teleoperation.md`
- `docs/source/zh_CN/robot_learning/data_collection.md`
- `docs/source/zh_CN/robot_learning/imitation_and_offline_data.md`
- `docs/source/zh_CN/robot_learning/safety_and_resets.md`
- `docs/source/en/robot_learning/locomotion.md`
- `docs/source/en/robot_learning/loco_manipulation.md`
- `docs/source/en/robot_learning/teleoperation.md`
- `docs/source/en/robot_learning/data_collection.md`
- `docs/source/en/robot_learning/imitation_and_offline_data.md`
- `docs/source/en/robot_learning/safety_and_resets.md`

Do not modify `rl_basics`, `world_models`, `distributed_rl`, or `research_practice` in this expansion.

## Task 1: Convert Embodied AI Landing Pages

**Files:**
- Modify: `docs/source/zh_CN/embodied_ai/index.md`
- Modify: `docs/source/en/embodied_ai/index.md`

- [ ] **Step 1: Verify current landing pages still use course-style template**

Run:

```bash
rg -n "Learning Goals|Exercises / Research Questions|Glossary" docs/source/zh_CN/embodied_ai/index.md docs/source/en/embodied_ai/index.md
```

Expected: output includes the current course-style section headings. This is the red check for the style conversion.

- [ ] **Step 2: Replace the Chinese embodied AI landing page**

Write `docs/source/zh_CN/embodied_ai/index.md` with this structure and content:

````markdown
# 具身智能基础

具身智能研究将学习问题放回到身体、传感器、执行器和环境构成的闭环系统中。与只在抽象状态空间中定义的强化学习任务不同，具身任务的状态通常不可完全观测，动作会受到低层控制器和硬件限制约束，评估结果也会受到 reset、接触、延迟和安全策略的影响。

本章把具身智能作为机器人学习和世界模型研究的共同问题设定来处理。重点不在于列举任务，而在于明确建模假设：什么被观测，什么被隐藏，动作如何作用到物理系统，仿真和真实系统之间哪些假设不一致，以及评估协议如何避免把工程细节误判为算法能力。

```{toctree}
:maxdepth: 1
:caption: 具身建模与评估

embodiment_and_pomdp
observation_action_spaces
simulation_and_real_robot_constraints
evaluation
```

## Connections

具身智能基础与本资料中的三条主线相连：强化学习提供优化和决策语言，世界模型提供预测和规划接口，机器人学习实践则暴露真实系统中的数据、控制、reset 和安全约束。
````

- [ ] **Step 3: Replace the English embodied AI landing page**

Write `docs/source/en/embodied_ai/index.md` with this structure and content:

````markdown
# Embodied AI Foundations

Embodied AI places learning back inside a closed-loop system composed of a body, sensors, actuators, and an environment. Compared with reinforcement learning tasks defined only over abstract states, embodied tasks are typically partially observable, constrained by low-level control and hardware interfaces, and evaluated under reset, contact, latency, and safety assumptions.

This section treats embodiment as a problem setting shared by robot learning and world model research. The emphasis is not on enumerating tasks, but on making assumptions explicit: what is observed, what remains latent, how actions affect the physical system, which simulator assumptions differ from real hardware, and how evaluation protocols prevent engineering details from being mistaken for algorithmic progress.

```{toctree}
:maxdepth: 1
:caption: Embodied Modeling and Evaluation

embodiment_and_pomdp
observation_action_spaces
simulation_and_real_robot_constraints
evaluation
```

## Connections

Embodied AI foundations connect three threads in this resource: reinforcement learning supplies the optimization language, world models provide prediction and planning interfaces, and robot learning exposes the data, control, reset, and safety constraints of physical systems.
````

- [ ] **Step 4: Verify landing pages now contain toctrees and no course headings**

Run:

```bash
rg -n "toctree|embodiment_and_pomdp|observation_action_spaces|simulation_and_real_robot_constraints|evaluation" docs/source/zh_CN/embodied_ai/index.md docs/source/en/embodied_ai/index.md
```

Expected: output includes all four child slugs in both language files.

Run:

```bash
! rg -n "Learning Goals|Exercises / Research Questions|Glossary" docs/source/zh_CN/embodied_ai/index.md docs/source/en/embodied_ai/index.md
```

Expected: command exits with status `0`, meaning the landing pages no longer use the course-style headings.

- [ ] **Step 5: Commit**

```bash
git add docs/source/zh_CN/embodied_ai/index.md docs/source/en/embodied_ai/index.md
git commit -m "docs: convert embodied ai landing pages"
```

## Task 2: Add Detailed Embodied AI Pages

**Files:**
- Create: `docs/source/zh_CN/embodied_ai/embodiment_and_pomdp.md`
- Create: `docs/source/zh_CN/embodied_ai/observation_action_spaces.md`
- Create: `docs/source/zh_CN/embodied_ai/simulation_and_real_robot_constraints.md`
- Create: `docs/source/zh_CN/embodied_ai/evaluation.md`
- Create: `docs/source/en/embodied_ai/embodiment_and_pomdp.md`
- Create: `docs/source/en/embodied_ai/observation_action_spaces.md`
- Create: `docs/source/en/embodied_ai/simulation_and_real_robot_constraints.md`
- Create: `docs/source/en/embodied_ai/evaluation.md`

- [ ] **Step 1: Verify detailed embodied pages do not exist yet**

Run:

```bash
test ! -f docs/source/zh_CN/embodied_ai/embodiment_and_pomdp.md && test ! -f docs/source/en/embodied_ai/embodiment_and_pomdp.md
```

Expected: command exits with status `0`.

- [ ] **Step 2: Create Chinese embodied pages**

Create the four Chinese pages using academic prose and the required sections below.

`docs/source/zh_CN/embodied_ai/embodiment_and_pomdp.md`:

- Title: `# 具身性与 POMDP 建模`
- Required headings: `Scope and Motivation`, `Problem Setting`, `Formalization`, `System / Algorithmic View`, `Implementation Notes`, `Failure Modes and Limitations`, `References`.
- Required content:
  - Define the embodied agent as a closed-loop system with morphology, sensors, actuators, and environment.
  - Contrast MDP state `s_t` with observation `o_t` and history `h_t`.
  - Include equations for `o_t ~ O(.|s_t)`, `a_t ~ pi(.|h_t)`, and belief/state-estimator view.
  - Discuss contact uncertainty, unobserved object properties, actuator delay, and morphology.
  - Explain practical consequences for policy inputs, recurrent policies, state estimation, logging, and evaluation.
  - References should include Kaelbling et al. on POMDPs, Sutton and Barto, and a robotics/embodiment reference.

`docs/source/zh_CN/embodied_ai/observation_action_spaces.md`:

- Title: `# 观测空间与动作空间`
- Required headings: `Scope and Motivation`, `Problem Setting`, `Formalization`, `System / Algorithmic View`, `Implementation Notes`, `Experimental Protocol`, `Failure Modes and Limitations`, `References`.
- Required content:
  - Cover proprioception, RGB/depth vision, tactile/force-torque, language/task specification, and privileged state.
  - Formalize observation as a dictionary or product space and action as command to a low-level controller.
  - Discuss timestamps, synchronization, normalization, coordinate frames, frame stacking, action repeat, action chunks, smoothing, and saturation.
  - Compare joint position, velocity, torque, end-effector delta, whole-body command, and high-level skill actions.
  - Include an experimental protocol for reporting observation/action design.

`docs/source/zh_CN/embodied_ai/simulation_and_real_robot_constraints.md`:

- Title: `# 仿真与真实机器人约束`
- Required headings: `Scope and Motivation`, `Problem Setting`, `System / Algorithmic View`, `Implementation Notes`, `Experimental Protocol`, `Failure Modes and Limitations`, `References`.
- Required content:
  - Cover simulator dynamics, contact model, actuator model, rendering, sensing noise, latency, calibration, thermal and hardware limits.
  - Discuss domain randomization, system identification, and sim-to-real gap categories.
  - Describe reproducibility metadata: simulator version, assets, physics parameters, control frequency, randomization ranges, calibration state, and hardware revision.
  - Include protocol for separating simulation-only assumptions from deployable assumptions.

`docs/source/zh_CN/embodied_ai/evaluation.md`:

- Title: `# 具身智能评估协议`
- Required headings: `Scope and Motivation`, `Problem Setting`, `Formalization`, `Experimental Protocol`, `Failure Modes and Limitations`, `Connections to Literature`, `References`.
- Required content:
  - Cover success rate, return, completion time, energy, safety violations, robustness, and generalization.
  - Define train/test splits over tasks, scenes, terrain, objects, initial states, and perturbations.
  - Discuss evaluation leakage from privileged state, reset policy, early termination, and hand-tuned thresholds.
  - Include statistical reporting across seeds, episodes, and environment variants.
  - Include failure taxonomy: perception, planning, control, contact, reset, safety, distribution shift.

- [ ] **Step 3: Create English embodied pages**

Create the four English pages with the same slugs and parallel structure:

`docs/source/en/embodied_ai/embodiment_and_pomdp.md`

- Title: `# Embodiment and POMDP Modeling`
- Use the same headings and cover the same topics as the Chinese page.
- Include equations using MyST-compatible dollar math.
- References should be English-language entries with short relevance notes.

`docs/source/en/embodied_ai/observation_action_spaces.md`

- Title: `# Observation and Action Spaces`
- Use the same headings and cover the same topics as the Chinese page.
- Keep prose formal and concise; do not use teaching prompts or exercises.

`docs/source/en/embodied_ai/simulation_and_real_robot_constraints.md`

- Title: `# Simulation and Real Robot Constraints`
- Use the same headings and cover the same topics as the Chinese page.

`docs/source/en/embodied_ai/evaluation.md`

- Title: `# Evaluation Protocols for Embodied Agents`
- Use the same headings and cover the same topics as the Chinese page.

- [ ] **Step 4: Verify embodied pages are substantive and aligned**

Run:

```bash
for f in docs/source/zh_CN/embodied_ai/{embodiment_and_pomdp,observation_action_spaces,simulation_and_real_robot_constraints,evaluation}.md docs/source/en/embodied_ai/{embodiment_and_pomdp,observation_action_spaces,simulation_and_real_robot_constraints,evaluation}.md; do test -f "$f" || exit 1; wc -w "$f"; done
```

Expected: all files exist. Chinese files may have lower `wc -w` counts because Chinese tokenization differs, but each file should be visibly substantive when inspected.

Run:

```bash
rg -n "^## (Scope and Motivation|Problem Setting|References)" docs/source/zh_CN/embodied_ai/*.md docs/source/en/embodied_ai/*.md
```

Expected: each new detailed page has academic-style section headings and a references section.

Run:

```bash
! rg -n "Learning Goals|Exercises / Research Questions|Glossary|TODO|TBD|placeholder" docs/source/zh_CN/embodied_ai docs/source/en/embodied_ai
```

Expected: command exits with status `0`.

- [ ] **Step 5: Commit**

```bash
git add docs/source/zh_CN/embodied_ai docs/source/en/embodied_ai
git commit -m "docs: add embodied ai technical pages"
```

## Task 3: Convert Robot Learning Landing Pages

**Files:**
- Modify: `docs/source/zh_CN/robot_learning/index.md`
- Modify: `docs/source/en/robot_learning/index.md`

- [ ] **Step 1: Verify current landing pages still use course-style template**

Run:

```bash
rg -n "Learning Goals|Exercises / Research Questions|Glossary" docs/source/zh_CN/robot_learning/index.md docs/source/en/robot_learning/index.md
```

Expected: output includes the current course-style section headings.

- [ ] **Step 2: Replace the Chinese robot learning landing page**

Write `docs/source/zh_CN/robot_learning/index.md` with this structure and content:

````markdown
# 机器人学习实践

机器人学习把策略优化、数据生成、机器人控制、实验评估和安全约束耦合在同一个系统中。一个机器人学习结果通常不只由算法决定，还取决于任务定义、遥操或自动采集流程、动作接口、reset 机制、硬件限制和评估分布。

本章采用实验系统视角组织内容。Locomotion 和 loco-manipulation 代表两类典型具身控制问题；teleoperation 和 data collection 描述数据来源；imitation、offline data、safety 和 resets 则描述训练与评估中最容易被低估的工程变量。

```{toctree}
:maxdepth: 1
:caption: 机器人学习系统

locomotion
loco_manipulation
teleoperation
data_collection
imitation_and_offline_data
safety_and_resets
```

## System View

一个可复现的机器人学习实验至少需要同时说明：任务分布、观测和动作接口、控制频率、数据采集策略、训练算法、评估协议、reset 流程、安全边界和日志 schema。缺少任意一项都可能使结果难以比较或迁移。
````

- [ ] **Step 3: Replace the English robot learning landing page**

Write `docs/source/en/robot_learning/index.md` with this structure and content:

````markdown
# Robot Learning Practice

Robot learning couples policy optimization, data generation, robot control, experimental evaluation, and safety constraints inside a single system. A robot learning result is rarely determined by the algorithm alone; it also depends on task definition, teleoperation or autonomous collection, action interfaces, reset mechanisms, hardware limits, and evaluation distributions.

This section uses an experimental-systems view. Locomotion and loco-manipulation represent two central embodied control settings. Teleoperation and data collection define where data comes from. Imitation, offline data, safety, and resets describe engineering variables that often dominate training and evaluation.

```{toctree}
:maxdepth: 1
:caption: Robot Learning Systems

locomotion
loco_manipulation
teleoperation
data_collection
imitation_and_offline_data
safety_and_resets
```

## System View

A reproducible robot learning experiment should specify the task distribution, observation and action interfaces, control frequency, data collection strategy, training algorithm, evaluation protocol, reset process, safety boundary, and logging schema. Omitting any of these can make results difficult to compare or transfer.
````

- [ ] **Step 4: Verify landing pages now contain toctrees and no course headings**

Run:

```bash
rg -n "toctree|locomotion|loco_manipulation|teleoperation|data_collection|imitation_and_offline_data|safety_and_resets" docs/source/zh_CN/robot_learning/index.md docs/source/en/robot_learning/index.md
```

Expected: output includes all six child slugs in both language files.

Run:

```bash
! rg -n "Learning Goals|Exercises / Research Questions|Glossary" docs/source/zh_CN/robot_learning/index.md docs/source/en/robot_learning/index.md
```

Expected: command exits with status `0`.

- [ ] **Step 5: Commit**

```bash
git add docs/source/zh_CN/robot_learning/index.md docs/source/en/robot_learning/index.md
git commit -m "docs: convert robot learning landing pages"
```

## Task 4: Add Detailed Robot Learning Pages

**Files:**
- Create: `docs/source/zh_CN/robot_learning/locomotion.md`
- Create: `docs/source/zh_CN/robot_learning/loco_manipulation.md`
- Create: `docs/source/zh_CN/robot_learning/teleoperation.md`
- Create: `docs/source/zh_CN/robot_learning/data_collection.md`
- Create: `docs/source/zh_CN/robot_learning/imitation_and_offline_data.md`
- Create: `docs/source/zh_CN/robot_learning/safety_and_resets.md`
- Create: `docs/source/en/robot_learning/locomotion.md`
- Create: `docs/source/en/robot_learning/loco_manipulation.md`
- Create: `docs/source/en/robot_learning/teleoperation.md`
- Create: `docs/source/en/robot_learning/data_collection.md`
- Create: `docs/source/en/robot_learning/imitation_and_offline_data.md`
- Create: `docs/source/en/robot_learning/safety_and_resets.md`

- [ ] **Step 1: Verify detailed robot learning pages do not exist yet**

Run:

```bash
test ! -f docs/source/zh_CN/robot_learning/locomotion.md && test ! -f docs/source/en/robot_learning/locomotion.md
```

Expected: command exits with status `0`.

- [ ] **Step 2: Create Chinese robot learning pages**

Create six Chinese pages using academic prose and the required sections below.

`docs/source/zh_CN/robot_learning/locomotion.md`:

- Title: `# Locomotion`
- Required headings: `Scope and Motivation`, `Problem Setting`, `Formalization`, `System / Algorithmic View`, `Implementation Notes`, `Experimental Protocol`, `Failure Modes and Limitations`, `References`.
- Required content:
  - Continuous-control framing for legged or mobile locomotion.
  - Observation design: base state, joint state, command, terrain signal, history.
  - Action parameterizations: joint targets, torques, residual actions, gait or velocity commands.
  - Reward terms: command tracking, energy, stability, foot clearance, smoothness, contacts.
  - Terrain distributions, perturbations, curricula, and evaluation beyond nominal training terrain.

`docs/source/zh_CN/robot_learning/loco_manipulation.md`:

- Title: `# Loco-Manipulation`
- Required headings: `Scope and Motivation`, `Problem Setting`, `System / Algorithmic View`, `Implementation Notes`, `Experimental Protocol`, `Failure Modes and Limitations`, `References`.
- Required content:
  - Define coupled mobility and manipulation tasks.
  - Discuss base-arm-object coupling, contact-rich dynamics, whole-body coordination, grasp stability, object pose uncertainty.
  - Discuss hierarchical decomposition, task progress representation, and partial observability.
  - Evaluation should include sequential success, partial completion, object state, robot stability, and recovery behavior.

`docs/source/zh_CN/robot_learning/teleoperation.md`:

- Title: `# Teleoperation`
- Required headings: `Scope and Motivation`, `Problem Setting`, `System / Algorithmic View`, `Implementation Notes`, `Experimental Protocol`, `Failure Modes and Limitations`, `References`.
- Required content:
  - Teleoperation as demonstration source and online intervention mechanism.
  - Device and command-space choices: joystick, VR, keyboard, motion capture, leader-follower, shared autonomy.
  - Latency, operator feedback, action-space alignment, human bias, intervention logs.
  - Protocol for logging human actions, robot actions, autonomy mode, operator ID/session, and intervention reason.

`docs/source/zh_CN/robot_learning/data_collection.md`:

- Title: `# Data Collection`
- Required headings: `Scope and Motivation`, `Problem Setting`, `System / Algorithmic View`, `Implementation Notes`, `Experimental Protocol`, `Failure Modes and Limitations`, `References`.
- Required content:
  - Data collection as an experimental system.
  - Episode schema including observations, actions, rewards, success labels, terminal condition, reset information, metadata.
  - Timestamp synchronization across robot state, sensors, operator input, and environment state.
  - Coverage, sampling bias, quality control, invalid episode detection, annotation, versioning.
  - Include an example schema table in Markdown.

`docs/source/zh_CN/robot_learning/imitation_and_offline_data.md`:

- Title: `# Imitation Learning and Offline Data`
- Required headings: `Scope and Motivation`, `Problem Setting`, `Formalization`, `System / Algorithmic View`, `Implementation Notes`, `Experimental Protocol`, `Failure Modes and Limitations`, `References`.
- Required content:
  - Behavior cloning objective and covariate shift.
  - DAgger-style correction and interactive data aggregation.
  - Offline RL constraints, OOD actions, conservative objectives, off-policy evaluation.
  - Dataset bias, multimodal demonstrations, action relabeling, and when imitation is preferable to online RL.

`docs/source/zh_CN/robot_learning/safety_and_resets.md`:

- Title: `# Safety and Resets`
- Required headings: `Scope and Motivation`, `Problem Setting`, `System / Algorithmic View`, `Implementation Notes`, `Experimental Protocol`, `Failure Modes and Limitations`, `References`.
- Required content:
  - Safety monitors, constraints, emergency stops, workspace limits, velocity/force/torque caps.
  - Reset distribution, reset policy, failure recovery, and hardware protection.
  - Throughput accounting: wall-clock time, robot uptime, reset time, human intervention time.
  - Discuss how safety and reset design can change reported performance.

- [ ] **Step 3: Create English robot learning pages**

Create six English pages with the same slugs, parallel structure, and formal technical prose:

- `docs/source/en/robot_learning/locomotion.md`: title `# Locomotion`
- `docs/source/en/robot_learning/loco_manipulation.md`: title `# Loco-Manipulation`
- `docs/source/en/robot_learning/teleoperation.md`: title `# Teleoperation`
- `docs/source/en/robot_learning/data_collection.md`: title `# Data Collection`
- `docs/source/en/robot_learning/imitation_and_offline_data.md`: title `# Imitation Learning and Offline Data`
- `docs/source/en/robot_learning/safety_and_resets.md`: title `# Safety and Resets`

Each English page must cover the same required topics as the matching Chinese page. Do not leave English pages as summaries only.

- [ ] **Step 4: Verify robot learning pages are substantive and aligned**

Run:

```bash
for f in docs/source/zh_CN/robot_learning/{locomotion,loco_manipulation,teleoperation,data_collection,imitation_and_offline_data,safety_and_resets}.md docs/source/en/robot_learning/{locomotion,loco_manipulation,teleoperation,data_collection,imitation_and_offline_data,safety_and_resets}.md; do test -f "$f" || exit 1; wc -w "$f"; done
```

Expected: all files exist and are visibly substantive.

Run:

```bash
rg -n "^## (Scope and Motivation|Problem Setting|References)" docs/source/zh_CN/robot_learning/*.md docs/source/en/robot_learning/*.md
```

Expected: each new detailed page has academic-style section headings and a references section.

Run:

```bash
! rg -n "Learning Goals|Exercises / Research Questions|Glossary|TODO|TBD|placeholder" docs/source/zh_CN/robot_learning docs/source/en/robot_learning
```

Expected: command exits with status `0`.

- [ ] **Step 5: Commit**

```bash
git add docs/source/zh_CN/robot_learning docs/source/en/robot_learning
git commit -m "docs: add robot learning technical pages"
```

## Task 5: Final Verification and Content Review

**Files:**
- Modify only files created or changed in Tasks 1-4 if verification exposes broken links, invalid MyST syntax, mismatched navigation, or style regressions.

- [ ] **Step 1: Verify Sphinx build**

Run:

```bash
.venv/bin/python -m sphinx -b html docs/source docs/build/html -W
```

Expected: build succeeds with no warnings.

- [ ] **Step 2: Verify Makefile build path**

Run:

```bash
PATH=/home/ethan/Project/essentials-of-eai-research/.venv/bin:$PATH make -C docs html
```

Expected: build succeeds.

- [ ] **Step 3: Verify bilingual embodied slugs match**

Run:

```bash
for slug in embodiment_and_pomdp observation_action_spaces simulation_and_real_robot_constraints evaluation; do test -f "docs/source/zh_CN/embodied_ai/$slug.md" && test -f "docs/source/en/embodied_ai/$slug.md" || exit 1; done
```

Expected: command exits with status `0`.

- [ ] **Step 4: Verify bilingual robot learning slugs match**

Run:

```bash
for slug in locomotion loco_manipulation teleoperation data_collection imitation_and_offline_data safety_and_resets; do test -f "docs/source/zh_CN/robot_learning/$slug.md" && test -f "docs/source/en/robot_learning/$slug.md" || exit 1; done
```

Expected: command exits with status `0`.

- [ ] **Step 5: Verify no newly expanded pages retain teaching template headings**

Run:

```bash
! rg -n "Learning Goals|Exercises / Research Questions|Glossary" docs/source/zh_CN/embodied_ai docs/source/en/embodied_ai docs/source/zh_CN/robot_learning docs/source/en/robot_learning
```

Expected: command exits with status `0`.

- [ ] **Step 6: Verify toctree entries**

Run:

```bash
rg -n "embodiment_and_pomdp|observation_action_spaces|simulation_and_real_robot_constraints|evaluation" docs/source/zh_CN/embodied_ai/index.md docs/source/en/embodied_ai/index.md
rg -n "locomotion|loco_manipulation|teleoperation|data_collection|imitation_and_offline_data|safety_and_resets" docs/source/zh_CN/robot_learning/index.md docs/source/en/robot_learning/index.md
```

Expected: both commands show all required child page slugs in both languages.

- [ ] **Step 7: Inspect references and external links**

Run:

```bash
rg -n "https?://" docs/source/zh_CN/embodied_ai docs/source/en/embodied_ai docs/source/zh_CN/robot_learning docs/source/en/robot_learning
```

Expected: any URLs present are intentional Markdown links or bare references to stable papers/docs. If a current project URL is included, verify it before committing.

- [ ] **Step 8: Check git status**

Run:

```bash
git status --short
```

Expected: only intentional source edits are present before the final verification commit.

- [ ] **Step 9: Commit verification fixes**

If Step 1-8 required edits, commit them:

```bash
git add docs/source/zh_CN/embodied_ai docs/source/en/embodied_ai docs/source/zh_CN/robot_learning docs/source/en/robot_learning
git commit -m "docs: verify embodied robot learning expansion"
```

If no edits were required, do not create an empty commit.
