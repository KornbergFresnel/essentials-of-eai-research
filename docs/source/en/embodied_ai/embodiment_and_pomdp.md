# Embodiment and POMDP Modeling

## Scope and Motivation

In embodied AI, the environment is not merely an abstract process that returns a compact state vector. It is a closed-loop system formed by morphology, sensors, actuators, controllers, and the external physical world. Body morphology changes the feasible action set and passive dynamics. Sensors determine what can be observed. Actuators and low-level controllers determine how policy outputs become physical interaction.

For this reason, the modeling question is usually not "what is the state $s_t$?" but "given the observation history and the available control interface, can the agent reliably change the world?" Most embodied problems are better treated as partially observable than as clean fully observable MDPs.

## Problem Setting

An embodied agent can be written as:

$$
s_{t+1} \sim P(s_{t+1}|s_t, a_t), \quad
o_t \sim O(o_t|s_t), \quad
a_t \sim \pi(a_t|h_t),
$$

where $s_t$ is the physical and internal robot state, $o_t$ is the sensor observation, and $h_t=(o_0,a_0,\dots,o_t)$ is the interaction history. Contact state, friction, object mass, actuator temperature, camera calibration drift, and human interventions may all affect future transitions without being directly observed.

## Formalization

In a POMDP view, the policy may depend on history or on a belief state:

$$
b_t(s)=P(s_t=s|h_t), \quad a_t \sim \pi(a_t|b_t).
$$

Practical systems rarely maintain an exact belief. Common approximations include state estimators, sliding windows, recurrent policies, latent states in world models, and low-level controllers that absorb part of the dynamics. The important question is whether the policy receives enough information to distinguish hidden variables that matter for action.

## System / Algorithmic View

POMDP modeling affects four interfaces. First, policy inputs should separate deployable observations from privileged state. Second, logs should record observable signals, diagnostic hidden variables when available offline, control commands, and safety events. Third, state estimators or recurrent modules used during training should respect the same information boundary during evaluation. Fourth, evaluation should vary initial states, disturbances, and sensor conditions rather than reporting only training return under simulator state access.

## Implementation Notes

Implementation failures often come from unclear information boundaries. A policy trained with simulator contact labels, exact object pose, or future commands may not be deployable. Conversely, a policy given only a single camera frame and current joint positions may fail because velocity, contact, and external force are unobservable. Documentation should identify the source, frequency, latency, coordinate frame, and deployment availability of every input field.

## Failure Modes and Limitations

The POMDP formalism identifies hidden state, but it does not solve state estimation. Recurrent policies may memorize spurious correlations in the training distribution. State estimators may fail at contact transitions. Belief models may accumulate long-horizon error. In embodied systems, the gap between formal abstraction and hardware reality should be treated as part of the method boundary.

## References

- Kaelbling, Littman, and Cassandra, "Planning and Acting in Partially Observable Stochastic Domains": canonical POMDP survey.
- Sutton and Barto, *Reinforcement Learning: An Introduction*: MDPs, value functions, and policy optimization.
- Pfeifer and Bongard, *How the Body Shapes the Way We Think*: morphology and embodiment as computational structure.
