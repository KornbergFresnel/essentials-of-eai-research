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
