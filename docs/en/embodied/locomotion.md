# Locomotion Control

Learning locomotion — the ability to walk, run, climb, and navigate diverse terrain — is one of the most active and successful areas of embodied AI. RL-based locomotion has achieved remarkable results in the past few years, with policies that transfer from simulation to real quadruped and humanoid robots.

## Problem Formulation

The locomotion control problem:

- **State**: Robot proprioception (joint positions $q$, joint velocities $\dot{q}$, base orientation, base angular velocity, gravity vector) + optional exteroception (heightmap, depth image)
- **Action**: Joint position targets $a_t \in \mathbb{R}^n$ (sent to PD controllers)
- **Reward**: Combination of velocity tracking, energy efficiency, and regularization

### Typical Reward Function

$$
r_t = \underbrace{r_{\text{tracking}}}_{\text{follow commands}} + \underbrace{r_{\text{style}}}_{\text{natural motion}} - \underbrace{c_{\text{energy}}}_{\text{efficiency}} - \underbrace{c_{\text{smooth}}}_{\text{smoothness}}
$$

Common reward terms:

| Term | Formula | Purpose |
|------|---------|---------|
| Linear velocity tracking | $\exp(-\|v_{xy} - v_{xy}^{\text{cmd}}\|^2 / \sigma)$ | Follow velocity commands |
| Angular velocity tracking | $\exp(-\|\omega_z - \omega_z^{\text{cmd}}\|^2 / \sigma)$ | Follow yaw rate commands |
| Base height | $-(z_{\text{base}} - z_{\text{target}})^2$ | Maintain desired height |
| Orientation | $-\|\text{gravity\_projected}_{xy}\|^2$ | Stay upright |
| Action rate | $-\|\dot{a}_t\|^2$ | Smooth actions |
| Torque penalty | $-\|\tau_t\|^2$ | Energy efficiency |
| Feet air time | Bonus for swing phase duration | Encourage gait patterns |

## Key Approaches

### Teacher-Student Framework

A widely used paradigm where:

1. **Teacher policy** is trained with privileged information (exact terrain heightmap, contact forces, friction coefficients)
2. **Student policy** is trained to imitate the teacher using only onboard sensor observations

This decouples the RL training (with easy-to-learn privileged state) from the deployment constraint (limited onboard sensors).

```mermaid
graph LR
    T[Teacher Policy<br/>Privileged Obs] -->|Distillation| S[Student Policy<br/>Onboard Obs Only]
    SIM[Simulation<br/>Privileged Info] --> T
    S --> REAL[Real Robot]
```

### Curriculum Learning

Gradually increase task difficulty during training:

- **Terrain curriculum**: Start on flat ground → gentle slopes → stairs → rough terrain → stepping stones
- **Command curriculum**: Start with slow speeds → increase to full range
- **Disturbance curriculum**: Start with no pushes → increase external forces

### Reward Shaping via Reference Motion

Use motion capture or hand-designed reference trajectories to guide learning:

$$
r_{\text{imitation}} = \exp\left(-\alpha \sum_j \| q_j - q_j^{\text{ref}} \|^2 \right)
$$

This helps the policy discover natural gaits (trot, bound, gallop) rather than unnatural but reward-maximizing behaviors.

## Landmark Results

### Quadruped Locomotion

**Learning Agile and Dynamic Motor Skills for Legged Robots** (Hwangbo et al., 2019):

- Actuator network to model real motor dynamics
- Trained ANYmal to walk, recover from falls
- One of the earliest successful sim-to-real RL locomotion results

**Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild** (Miki et al., 2022):

- Teacher-student with proprioception + exteroception
- ANYmal navigating forest trails, snow, stairs
- Belief-based estimation of terrain

**Extreme Parkour with Legged Robots** (Cheng et al., 2024):

- Quadruped performing jumps, flips, climbing
- Trained with massive domain randomization
- Agility approaching biological capability

### Humanoid Locomotion

**Sim-to-Real Learning of All Common Bipedal Gaits** (Siekmann et al., 2021):

- Walking, running, skipping, hopping on Cassie robot
- RL + reference motion + reward shaping

**Learning Humanoid Locomotion with Transformers** (Radosavovic et al., 2024):

- Causal Transformer policy with observation history
- Robust walking on diverse terrain for humanoid robot
- Demonstrates importance of history for handling latency and unobserved state

**Humanoid Locomotion as Next Token Prediction** (Liao et al., 2024):

- Sensorimotor trajectory prediction with autoregressive model
- Framing locomotion as sequence modeling problem

## Technical Deep-Dives

### Observation History and Latency Handling

Real robots have sensor delay (~20-50ms) and actuator delay (~10-30ms). Solutions:

- **Stacked observations**: Concatenate last $k$ observations as input
- **RNN/Transformer**: Process observation sequences with recurrent or attention-based architectures
- **Explicit delay modeling**: Include simulated delay during training

### Sim-to-Real Transfer Techniques

| Technique | Description |
|-----------|-------------|
| **Domain randomization** | Randomize physics, visual, and morphology parameters |
| **System identification** | Estimate real robot parameters, match simulation |
| **Actuator network** | Learn a neural model of real actuator dynamics |
| **Observation noise** | Add noise to simulate real sensor imperfections |
| **Action delay** | Simulate communication and computation latency |

### Terrain-Adaptive Locomotion

For traversing diverse terrain:

1. **Heightmap-based**: Use a terrain heightmap (from depth camera or LiDAR) as additional input
2. **Implicit adaptation**: Use observation history — the policy implicitly infers terrain properties from recent dynamics
3. **Explicit estimation**: Train an estimator network to predict terrain properties (friction, slope) from observation history

## Common Training Configurations

For a typical quadruped locomotion task:

| Parameter | Typical Value |
|-----------|--------------|
| Algorithm | PPO |
| Parallel environments | 4096 - 8192 |
| Simulation platform | Isaac Gym / Isaac Lab |
| Episode length | 20-30 seconds |
| Control frequency | 50-100 Hz |
| Training time | 1-4 hours (single GPU) |
| Total environment steps | 10⁸ - 10⁹ |
| Policy network | MLP (128, 64, 32) or small Transformer |
| Action space | Joint position targets (12D for quadruped) |

## Key References

- Hwangbo, J., et al. (2019). "Learning Agile and Dynamic Motor Skills for Legged Robots." *Science Robotics*.
- Lee, J., et al. (2020). "Learning Quadrupedal Locomotion over Challenging Terrain." *Science Robotics*.
- Miki, T., et al. (2022). "Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild." *Science Robotics*.
- Cheng, X., et al. (2024). "Extreme Parkour with Legged Robots." *ICRA*.
- Radosavovic, I., et al. (2024). "Learning Humanoid Locomotion with Transformers." *arXiv:2303.03381*.
- Kumar, A., et al. (2021). "RMA: Rapid Motor Adaptation for Legged Robots." *RSS*.
