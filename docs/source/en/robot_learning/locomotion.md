# Locomotion

## Scope and Motivation

Locomotion is a canonical continuous-control problem in robot learning. A policy must maintain stable motion under contact switching, underactuated dynamics, terrain perturbations, and actuator limits. Compared with static manipulation, locomotion failures are often system-level: a single contact error can become a fall within hundreds of milliseconds. Evaluation must therefore cover command distributions, terrain distributions, and external disturbances.

## Problem Setting

A locomotion task typically provides a velocity command, heading command, or trajectory target, while the policy outputs low-level control commands. Observations may include base orientation, angular velocity, joint positions, joint velocities, previous actions, contact estimates, and local terrain information. On hardware, base linear velocity and foot contact may not be reliable measurements, so state estimation quality directly affects policy behavior.

## Formalization

A command-conditioned locomotion policy can be written as:

$$
a_t \sim \pi(a_t|o_t,c_t), \quad c_t \sim p(c),
$$

where $c_t$ is a velocity, turning, or posture command. Rewards often combine tracking, energy, stability, smoothness, and contact terms:

$$
r_t = r_{\mathrm{track}} - \lambda_E E_t - \lambda_\Delta \|a_t-a_{t-1}\|^2 + r_{\mathrm{contact}}.
$$

These terms are not neutral; they define preferred gait, speed range, and energy behavior.

## System / Algorithmic View

Common action interfaces include joint position targets, joint torques, residual actions, and high-level gait or velocity commands. Position targets with a PD controller are usually more stable. Torque control is more expressive but more sensitive to model error and safety constraints. Many systems use teacher-student learning, privileged critics, or terrain encoders: training can use terrain and dynamics parameters, while deployment approximates them with history or perception.

## Implementation Notes

Reports should specify control frequency, policy frequency, PD gains, action clipping, command sampling distribution, terrain curriculum, termination conditions, and reset logic. Foot contacts, base velocity, and terrain height maps should be marked as non-deployable if they come from simulator privileged state. Hardware experiments should also record motor temperature, joint limits, emergency stops, and fall detection.

## Experimental Protocol

Evaluation should include nominal command tracking, extrapolation beyond the training command range, terrain variation, pushes, and long-horizon stability. Metrics include tracking error, fall rate, cost of transport or energy per distance, foot slip, recovery time, and safety events. Mean return alone can hide high-risk failures, especially on hardware.

## Failure Modes and Limitations

Common failures include reward hacking, overfitting to flat terrain, action jitter, motor overheating, contact-estimation error, and narrow reset distributions. Stable simulated gaits may rely on unrealistic friction or zero-delay control. Strong domain randomization can improve robustness but may reduce speed or energy efficiency.

## References

- Kumar et al., "RMA: Rapid Motor Adaptation for Legged Robots": adaptive locomotion system.
- Tan et al., "Sim-to-Real: Learning Agile Locomotion for Quadruped Robots": quadruped sim-to-real case study.
- Peng et al., "Learning Agile Robotic Locomotion Skills by Imitating Animals": gait learning and motion style reference.
