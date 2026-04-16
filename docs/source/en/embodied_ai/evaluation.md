# Evaluation Protocols for Embodied Agents

## Scope and Motivation

Embodied AI evaluation cannot rely only on training return. Reward functions often include shaping terms, reset and termination rules affect returns, safety filters may hide policy failures, and simulator state may include information unavailable on hardware. Evaluation protocols should separately report task success, robustness, generalization, safety, and system throughput.

## Problem Setting

The object of evaluation is not an isolated policy but a complete system: observation pipeline, low-level controller, safety monitor, and reset procedure. A policy that succeeds from fixed initial states in an undisturbed environment has not demonstrated robustness to object variation, terrain changes, lighting, contact uncertainty, or sensor latency.

## Formalization

An evaluation distribution can be written as:

$$
\xi \sim p_{\mathrm{eval}}(\xi), \quad \tau \sim P(\tau|\pi,\xi),
$$

where $\xi$ contains task parameters, initial state, scene, objects, terrain, and disturbances. Metrics should include success probability $P(\mathrm{success})$, return, completion time, safety violations, energy, and recovery behavior.

## Experimental Protocol

The evaluation set should be explicitly separated from the training distribution. Split dimensions may include goals, scenes, terrain, object instances, initial states, external perturbations, and sensor conditions. Each dimension should be labeled as in-distribution, interpolation, or extrapolation. Statistical reports should include episode count, random seeds, number of environment variants, and confidence intervals or standard errors.

## Failure Modes and Limitations

Evaluation leakage is common. It can occur when the policy uses privileged state, when reset policies remove failure states, when early termination prevents dangerous behavior from affecting later metrics, when success thresholds are tuned after method development, or when human intervention is not logged. Aggregate success rate is also insufficient if it is not accompanied by failure-type analysis.

## Connections to Literature

Embodied evaluation combines reporting norms from reinforcement learning, task success and safety metrics from robotics, and train/test split principles from dataset evaluation. For robot systems, qualitative failure analysis is not a cosmetic appendix; it is evidence for the boundary of the method.

## References

- Henderson et al., "Deep Reinforcement Learning That Matters": reproducibility and statistical reporting in RL.
- Dulac-Arnold et al., "Challenges of Real-World Reinforcement Learning": constraints, delays, and safety in real systems.
- Agarwal et al., "Deep Reinforcement Learning at the Edge of the Statistical Precipice": aggregate metrics and statistical uncertainty.
