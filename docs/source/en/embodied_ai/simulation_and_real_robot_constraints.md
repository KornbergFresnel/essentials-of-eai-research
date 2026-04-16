# Simulation and Real Robot Constraints

## Scope and Motivation

Simulation provides scalable sampling, controlled perturbations, and low-cost failure. It is not an equivalent substitute for the real system. Hardware introduces latency, calibration drift, wear, thermal limits, sensor noise, human safety constraints, and reset cost. The sim-to-real gap is not only a dynamics mismatch; it also includes task distribution, observation pipelines, actuation, reset procedures, and experiment operations.

## Problem Setting

Simulators often assume repeatable reset, exact state access, ideal synchronization, controlled random seeds, and negligible hardware degradation. Real robots violate these assumptions. Sensor timestamps may be misaligned, actuators have bandwidth limits, contact depends on material and wear, and calibration changes over time. Learning methods that rely on simulator-only assumptions can overestimate deployable performance.

## System / Algorithmic View

The sim-to-real gap can be divided into five categories. Dynamics gaps include mass, friction, joint damping, contact modeling, and compliance. Perception gaps include rendering, lighting, camera noise, and occlusion. Actuation gaps include saturation, control delay, and low-level controller differences. Reset gaps include initial-state distribution and human recovery procedures. Task-distribution gaps include objects, terrain, human interventions, and environmental variation.

Domain randomization increases robustness by expanding the training distribution. System identification reduces measurable systematic error. These are complementary: randomization handles uncertainty that cannot be fully modeled, while identification reduces bias in parameters that can be measured.

## Implementation Notes

Reproducible experiments should record simulator version, robot model, asset files, physics parameters, contact-solver settings, control frequency, randomization ranges, rendering settings, and reset scripts. Real-system experiments should record hardware revision, calibration procedure, controller version, sensor frequency, network latency, maintenance state, and safety limits. Without this information, algorithmic results are difficult to compare across systems.

## Experimental Protocol

Reports should separate simulation-only assumptions from deployable assumptions. Simulation-only assumptions include privileged state, exact reset, zero-delay control, and perfect synchronization. Deployable assumptions include real sensor input, actual control frequency, and safety filters. Transfer experiments should report simulator performance, randomized simulator performance, limited real-world trials, and categorized failure cases.

## Failure Modes and Limitations

Randomization ranges that are too narrow lead to simulator overfitting. Ranges that are too broad can make training unnecessarily difficult and reduce nominal performance. System identification based only on short trajectories may fail to explain contact switches and long-term wear. Reset strategies that work in simulation may dominate wall-clock time on hardware.

## References

- Tobin et al., "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World": perception-focused randomization.
- Peng et al., "Sim-to-Real Transfer of Robotic Control with Dynamics Randomization": dynamics randomization for control.
- Tan et al., "Sim-to-Real: Learning Agile Locomotion for Quadruped Robots": legged locomotion transfer case study.
