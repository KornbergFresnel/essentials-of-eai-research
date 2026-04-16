# Data Collection for Embodied AI

Data is the fuel for learning-based embodied AI. This page covers the strategies, systems, and considerations for collecting robot learning data at scale — including demonstrations, autonomous exploration, and synthetic data generation.

## The Data Challenge

Unlike NLP or computer vision, embodied AI faces a unique data bottleneck:

- **Expensive**: Real robot time costs $10-100 per hour
- **Slow**: Physical interactions take real time (no batch processing)
- **Fragile**: Robots break, wear out, need maintenance
- **Diverse**: Tasks, environments, and objects vary enormously
- **Non-reusable**: Data collected for one task may not help another

## Data Collection Strategies

### 1. Teleoperation (Human Demonstrations)

The most common approach for manipulation tasks. See [Teleoperation](teleoperation.md) for details.

**Strengths**: High quality, task-specific, captures human strategies

**Weaknesses**: Expensive (human time), doesn't scale, limited by operator skill

**Key systems**: ALOHA, UMI, GELLO, VR teleoperation

### 2. Scripted/Programmatic Data

Use pre-programmed or heuristic-based controllers to generate data:

```python
# Example: scripted grasping data collection
for episode in range(num_episodes):
    object_pose = randomize_object_placement()
    grasp_pose = compute_antipodal_grasp(object_pose)
    trajectory = plan_trajectory(current_pose, grasp_pose)
    execute_and_record(trajectory)
```

**Strengths**: Cheap, scalable, no human needed

**Weaknesses**: Limited task complexity, no human intuition, needs engineering per task

### 3. Autonomous Exploration (RL-Based)

Let the robot explore and collect its own data via RL:

- **Online RL**: Robot interacts with the environment, learns from rewards
- **Self-supervised**: Robot sets its own goals and explores (goal-conditioned RL, RND)
- **Play data**: Unstructured exploration where the robot interacts freely

**Strengths**: Scalable, discovers novel strategies, no human labels needed

**Weaknesses**: Slow (real-time exploration), safety concerns, sparse rewards challenging

### 4. Simulation Data

Generate data entirely in simulation:

| Approach | Description | Scale |
|----------|-------------|-------|
| **RL in sim** | Train RL policies in parallel simulation | 10⁸-10¹⁰ steps |
| **Procedural generation** | Randomly generate environments, objects, tasks | Unlimited variation |
| **Digital twins** | Simulate specific real environments | Limited but accurate |
| **Synthetic rendering** | Generate training images with domain randomization | Millions of images |

The sim-to-real gap remains the key challenge.

### 5. Internet-Scale Data

Leverage videos and data from the internet:

- **Robot video datasets**: Aggregated real robot data (Open X-Embodiment)
- **Human video**: Learn manipulation strategies from human demonstration videos
- **Passive video**: Internet videos of tasks (cooking, assembly, etc.)
- **Language-annotated data**: Video-language pairs for grounding

## Scaling Data Collection

### Robot Farms

Running multiple robots simultaneously to scale data collection:

**Google's Robot Farms**: 100+ robot arms collecting manipulation data 24/7

**DROID (Khazatsky et al., 2024)**: Distributed Robot Interaction Dataset

- 76K demonstrations across 564 tasks
- Collected across multiple institutions
- Standardized hardware and data format

### Fleet Learning

Using deployed robots to continuously collect and learn:

1. Deploy partially trained policies on a fleet of robots
2. Collect interaction data during normal operation
3. Aggregate data centrally, retrain models
4. Push updated models to the fleet

### Open X-Embodiment

**Open X-Embodiment (OXE)** is the largest aggregated robot learning dataset:

- 1M+ real robot episodes
- 22 robot embodiments
- 527 skills across 160K+ tasks
- Enables training generalist robot policies (RT-X)

## Data Formats and Standards

### Standard Formats

| Format | Description | Used By |
|--------|-------------|---------|
| **RLDS** | Reinforcement Learning Datasets (TensorFlow) | OXE, RT-X |
| **HDF5** | Hierarchical data format, flexible | RoboMimic |
| **LeRobot** | Hugging Face format for robot data | LeRobot ecosystem |
| **zarr** | Chunked, compressed array storage | Diffusion Policy |

### What to Record

For each demonstration episode, record:

- **Observations**: Camera images (multiple views), proprioception, force/torque
- **Actions**: Joint commands, end-effector poses
- **Metadata**: Task description, success/failure, timestamps, calibration
- **Language**: Natural language description of the task

## Data Augmentation

Augment real data to increase effective dataset size:

### Geometric Augmentation

- Random camera viewpoint perturbation
- Object pose randomization
- Workspace scaling and rotation

### Visual Augmentation

- Color jitter, random erasing
- Background randomization
- Lighting variation

### Trajectory Augmentation

- Add noise to action sequences (for robustness)
- Time-stretch trajectories (speed variation)
- Mirror/reflect trajectories

### Generative Augmentation

- Use diffusion models to generate novel visual scenes
- Use LLMs to generate task descriptions
- Use world models to imagine new scenarios

## From Demonstrations to Policies

Common approaches for learning from collected data:

### Behavior Cloning (BC)

Supervised learning: $\pi_\theta(a|o) = \arg\min_\theta \mathbb{E}_{(o,a) \sim \mathcal{D}} [\mathcal{L}(\pi_\theta(o), a)]$

Simple but suffers from **distribution shift** — small errors compound over time.

### Diffusion Policy

**Diffusion Policy** (Chi et al., 2023): Models the action distribution with a diffusion process:

$$
p_\theta(a_{t:t+H} | o_t) \text{ via iterative denoising}
$$

State-of-the-art for learning from demonstrations, handles multi-modal action distributions.

### Action Chunking with Transformers (ACT)

**ACT** (Zhao et al., 2023): Predicts chunks of future actions using a Transformer:

$$
a_{t:t+k} = \text{Transformer}(o_t, \text{style\_variable})
$$

Temporal ensembling of overlapping action chunks reduces jerky behavior.

### Inverse RL / Reward Learning

Learn a reward function from demonstrations, then optimize with RL:

- Potentially more robust than BC (doesn't suffer from distribution shift)
- More complex pipeline

## Key References

- Brohan, A., et al. (2023). "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control." *CoRL*.
- Chi, C., et al. (2023). "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion." *RSS*.
- Khazatsky, A., et al. (2024). "DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset." *RSS*.
- Open X-Embodiment Collaboration. (2024). "Open X-Embodiment: Robotic Learning Datasets and RT-X Models." *ICRA*.
- Zhao, T.Z., et al. (2023). "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware." *RSS*.
