# Embodied AI Foundations

## Learning Goals

This chapter connects abstract RL concepts to agents with bodies, sensors, actuators, dynamics, environmental constraints, and real experimental costs.

## Prerequisites

You should have basic background in robotics, control, reinforcement learning, and deep learning.

## Core Concepts

Embodied AI studies how agents interact with the world through a body. The body is not an implementation detail outside the algorithm; it determines action spaces, observation modes, exploration risk, and task feasibility.

## Mathematical Formulation

Embodied tasks are usually closer to POMDPs: the agent receives observation $o_t$, takes action $a_t$, and the true state $s_t$ may contain unmeasured contacts, object properties, or external disturbances.

## Algorithms / System Design

Embodied systems connect perception, state estimation, policy, low-level control, safety monitoring, and data logging. Learning algorithms must be designed together with control frequency, sensor latency, and actuator limits.

## Practical Notes

Simulation tasks should record physical parameters, domain randomization, control frequency, and reset logic. Real robot experiments should record hardware state, calibration, and failure recovery procedures.

## Common Pitfalls

- Treating privileged simulator state as an input available on real robots.
- Ignoring control frequency and latency.
- Reporting only successful cases without failure analysis.

## Recommended Reading

- Levine et al., learning hand-eye coordination.
- Tobin et al., domain randomization.
- OpenAI et al., dexterous manipulation from pixels.

## Exercises / Research Questions

Choose an embodied task and list its observations, actions, dynamics constraints, safety constraints, and evaluation metrics.

## Glossary

- Proprioception: self-sensing such as joint positions, velocities, and torques.
- Sim-to-real: transferring a policy or model from simulation to real hardware.
