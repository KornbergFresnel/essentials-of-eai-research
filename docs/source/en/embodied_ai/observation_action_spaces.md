# Observation and Action Spaces

## Scope and Motivation

Observation and action spaces are modeling decisions, not merely data formats. They determine what information a policy can use, which latent variables must be inferred, how outputs are interpreted by the control stack, and whether results can transfer to hardware. The same learning algorithm may define substantially different problems under different interfaces.

## Problem Setting

Embodied observations are usually multimodal. Proprioception provides joint positions, velocities, torques, and base state. Vision provides RGB, depth, point clouds, or semantic features. Tactile and force-torque sensors expose contact. Language or task specifications define goals. Simulators may additionally provide privileged state such as exact object pose, contact labels, or terrain height maps. A deployable policy should state which signals come from real sensors and which are used only by a critic, teacher, or diagnostic tool.

## Formalization

An observation may be represented as a product space or dictionary:

$$
o_t=\{q_t,\dot q_t,I_t,f_t,g_t,m_t\},
$$

where $q_t,\dot q_t$ describe robot state, $I_t$ is visual input, $f_t$ is force or tactile input, $g_t$ is a task goal, and $m_t$ stores mode or metadata. Actions are commands to a low-level controller rather than direct physical interventions:

$$
u_t=C(a_t,x_t), \quad s_{t+1}\sim P(s_t,u_t),
$$

where $C$ may be a PD controller, inverse kinematics module, whole-body controller, or safety filter.

## System / Algorithmic View

Common action parameterizations include joint position targets, joint velocities, torques, end-effector deltas, whole-body velocity commands, action chunks, and high-level skill commands. Position targets are stable but may restrict dynamic behavior. Torque control is expressive but sensitive to model error and safety limits. End-effector actions simplify manipulation but hide redundancy and collision constraints. Action chunks lower decision frequency while changing the feedback structure.

## Implementation Notes

Implementation should record timestamps, coordinate frames, normalization statistics, frame stacking, action repeat, control frequency, action clipping, and smoothing. Synchronization is critical: camera images, robot state, and teleoperation input often have different latency. Simply concatenating them can introduce hidden temporal bias. Action units and semantics should also be explicit, such as whether an end-effector delta is expressed in the world, base, or camera frame.

## Experimental Protocol

Reports should specify policy-visible observations, critic or teacher-only state, sensor frequency, policy frequency, low-level control frequency, action limits, action smoothing, coordinate definitions, and normalization. Algorithm comparisons should keep the observation and action interface fixed; otherwise the experiment changes the problem as well as the algorithm.

## Failure Modes and Limitations

Common failures include privileged information leakage, coordinate-frame mistakes, action saturation, and frequency mismatch. Another frequent gap is training on clean synchronized observations while deploying with dropped frames, latency, and calibration drift. If the learned policy action space differs from the data collection interface, behavior cloning can learn commands that are not executable under deployment conditions.

## References

- Levine et al., "End-to-End Training of Deep Visuomotor Policies": early deep visuomotor policy learning.
- Peng et al., "Sim-to-Real Transfer of Robotic Control with Dynamics Randomization": action interfaces and dynamics randomization.
- Brohan et al., RT-1: large-scale robot data with structured observations, actions, and task specifications.
