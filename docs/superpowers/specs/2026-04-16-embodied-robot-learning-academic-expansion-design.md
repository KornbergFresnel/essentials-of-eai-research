# Embodied and Robot Learning Academic Expansion Design

Date: 2026-04-16

## Goal

Expand the embodied AI and robot learning sections from introductory overview pages into academically styled technical documentation. The expansion should focus on embodied problem formulation, robot learning system design, implementation details, and experimental protocol for locomotion, loco-manipulation, teleoperation, data collection, imitation learning, offline data use, safety, and resets.

This is the first detailed content expansion after the bilingual Sphinx/Read the Docs framework was established.

## Style Direction

The content should use an academic and technical documentation style, not a teaching or course-handout style. It should avoid framing pages around learning goals, exercises, or glossary-first pedagogy. Instead, pages should read like concise research notes or technical documentation for a research group.

Where algorithmic or implementation detail is discussed, the organization may follow the spirit of OpenAI Spinning Up: begin with background and problem setting, connect mathematical objects to implementable quantities, identify practical assumptions, and close with references. The expansion should reference Spinning Up as an inspiration for organization and clarity, not copy its content.

Preferred page structure:

```text
# Title

## Scope and Motivation
## Problem Setting
## Formalization
## System / Algorithmic View
## Implementation Notes
## Experimental Protocol
## Failure Modes and Limitations
## Connections to Literature
## References
```

Not every page must include every section, but new detailed pages should generally follow this structure. Existing overview pages should be converted into section landing pages with compact introductions and toctrees.

## Language Strategy

Maintain parallel Chinese and English documentation trees with matching page slugs:

```text
docs/source/zh_CN/embodied_ai/<page>.md
docs/source/en/embodied_ai/<page>.md
docs/source/zh_CN/robot_learning/<page>.md
docs/source/en/robot_learning/<page>.md
```

Chinese pages may be more complete in the first pass. English pages should be formal, readable, and structurally aligned, not placeholders.

## Scope

Expand two existing sections:

- `embodied_ai`
- `robot_learning`

Do not expand RL basics, world models, distributed RL, or research practice in this iteration except for incidental cross-links if needed.

## Embodied AI Section

### Landing Page

Modify:

```text
docs/source/zh_CN/embodied_ai/index.md
docs/source/en/embodied_ai/index.md
```

The landing page should briefly state the role of embodied AI in the overall research path and link to the new detailed pages through a toctree.

### New Pages

Create matching Chinese and English pages:

```text
embodiment_and_pomdp.md
observation_action_spaces.md
simulation_and_real_robot_constraints.md
evaluation.md
```

#### `embodiment_and_pomdp.md`

Purpose: explain why embodied problems are rarely clean fully observable MDPs, and why POMDP-style thinking is often the more robust default.

Required topics:

- Body morphology as part of the problem definition.
- Sensorimotor loop and closed-loop interaction.
- Latent physical state, unobserved contacts, and history dependence.
- Relationship between MDP, POMDP, belief state, recurrent policy, and state estimator.
- Practical consequences for policy inputs, logging, and evaluation.

#### `observation_action_spaces.md`

Purpose: formalize observation and action choices as modeling decisions that shape the learning problem.

Required topics:

- Proprioception, vision, tactile signals, force/torque, language or task specification.
- Privileged state versus deployable observation.
- Observation normalization, frame conventions, timestamps, and synchronization.
- Joint position, joint velocity, torque, end-effector displacement, whole-body command, and action chunk parameterizations.
- Action rate, control frequency, low-level controllers, and action smoothing.

#### `simulation_and_real_robot_constraints.md`

Purpose: describe the assumptions that separate simulated embodied learning from real robot learning.

Required topics:

- Simulator dynamics, contact modeling, actuator models, and observation rendering.
- Real robot latency, calibration, sensing noise, hardware limits, thermal limits, and maintenance.
- Domain randomization and system identification.
- Sim-to-real gap categories: dynamics, perception, actuation, reset, and task distribution.
- Engineering documentation needed for reproducibility.

#### `evaluation.md`

Purpose: define evaluation protocols for embodied agents beyond training return.

Required topics:

- Success rate, return, task completion time, energy, safety violations, and robustness.
- Train/test split for tasks, scenes, terrain, objects, and initial states.
- Evaluation leakage from privileged state, reset policy, or hand-tuned termination.
- Failure taxonomy and qualitative failure analysis.
- Statistical reporting across seeds, episodes, and environment variants.

## Robot Learning Section

### Landing Page

Modify:

```text
docs/source/zh_CN/robot_learning/index.md
docs/source/en/robot_learning/index.md
```

The landing page should frame robot learning as a pipeline that couples task formulation, data generation, learning algorithm, evaluation, resets, and safety constraints. It should link to the new detailed pages through a toctree.

### New Pages

Create matching Chinese and English pages:

```text
locomotion.md
loco_manipulation.md
teleoperation.md
data_collection.md
imitation_and_offline_data.md
safety_and_resets.md
```

#### `locomotion.md`

Purpose: document locomotion as a continuous-control problem shaped by contact, stability, morphology, and evaluation distribution.

Required topics:

- State and observation design for legged or mobile systems.
- Low-level control interfaces and action parameterizations.
- Reward components such as velocity tracking, energy, stability, foot clearance, and smoothness.
- Terrain distributions, perturbations, and command curricula.
- Evaluation under disturbances and out-of-distribution terrain.

#### `loco_manipulation.md`

Purpose: document tasks where motion and manipulation are coupled rather than separable.

Required topics:

- Whole-body coordination and contact-rich dynamics.
- Coupling between base motion, arm motion, grasping, and object dynamics.
- Long-horizon decomposition and hierarchical control.
- Observation requirements for object pose, contact state, and task progress.
- Evaluation for sequential success and partial failure.

#### `teleoperation.md`

Purpose: describe teleoperation as both a data source and an intervention mechanism.

Required topics:

- Teleoperation devices and command spaces.
- Latency, operator feedback, and shared autonomy.
- Alignment between teleoperation action space and learned policy action space.
- Demonstration quality, operator bias, and correction data.
- Logging requirements for interventions and human actions.

#### `data_collection.md`

Purpose: define data collection as an experimental system rather than a passive logging process.

Required topics:

- Episode schema: observations, actions, rewards, success labels, resets, metadata.
- Timestamp synchronization across robot, sensors, operator input, and environment state.
- Dataset coverage, task distribution, and sampling bias.
- Quality control, invalid episode detection, and annotation.
- Dataset versioning and reproducibility.

#### `imitation_and_offline_data.md`

Purpose: connect collected data to imitation learning and offline RL assumptions.

Required topics:

- Behavior cloning and covariate shift.
- DAgger-style correction and interactive data aggregation.
- Offline RL constraints, OOD actions, conservatism, and policy evaluation.
- Dataset bias, multi-modal demonstrations, and action relabeling.
- When imitation learning is preferable to online RL.

#### `safety_and_resets.md`

Purpose: document safety and reset design as first-class components of robot learning experiments.

Required topics:

- Safety monitors, constraints, emergency stops, and workspace limits.
- Reset distribution and reset policy.
- Failure recovery and hardware protection.
- Throughput accounting: wall-clock time, robot uptime, reset time, and human intervention time.
- Safety and reset effects on reported performance.

## References and External Resources

Each new page should include a References section with a small number of useful entries. These may include papers, books, software documentation, benchmarks, and datasets. References should be concise and accompanied by a short phrase indicating why the item is relevant.

The implementation should avoid overclaiming recency. If current project URLs, package names, or benchmark details are included and may have changed, verify them before adding.

## Navigation Requirements

Both Chinese and English landing pages must include toctrees for their new child pages.

The existing top-level Chinese and English home pages already link to `embodied_ai/index` and `robot_learning/index`; no top-level navigation redesign is required.

## Testing and Verification

The implementation should verify:

- Sphinx builds with warnings treated as errors.
- Chinese and English embodied AI toctrees include the same child page slugs.
- Chinese and English robot learning toctrees include the same child page slugs.
- No newly added page is empty or placeholder-only.
- References and external links are valid Markdown links when URLs are included.

## Out of Scope

- Full literature survey coverage.
- Executable notebooks or robot code.
- Custom Sphinx theme changes.
- Expansion of RL basics, world models, distributed RL, or research practice.
- Automated translation infrastructure.
- Claims about the latest benchmark state without verification.
