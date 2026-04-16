# Teleoperation

Teleoperation allows a human operator to remotely control a robot in real-time. In the context of embodied AI, teleoperation serves as a critical tool for **collecting expert demonstrations**, **validating robot capabilities**, and enabling human-in-the-loop autonomy.

## Why Teleoperation Matters for AI

Teleoperation is a bridge between human intelligence and robot learning:

1. **Data collection**: Generate expert demonstrations for imitation learning
2. **Task validation**: Verify that a task is physically feasible before training a policy
3. **Shared autonomy**: Human handles hard parts, autonomy handles routine parts
4. **Safety**: Human oversight during deployment of learned policies

## Types of Teleoperation

### By Input Device

| Device | Degrees of Freedom | Latency | Ease of Use | Use Case |
|--------|-------------------|---------|-------------|----------|
| **Keyboard/Gamepad** | Low (6-8) | Low | Easy | Mobile base, simple tasks |
| **3D SpaceMouse** | 6 DOF | Low | Medium | Arm manipulation |
| **VR Controllers** | 6 DOF per hand + fingers | Medium | High | Bimanual manipulation |
| **Exoskeleton** | Full body | Low | Hard | Humanoid whole-body |
| **Hand tracking** | Per-finger control | Medium | Easy | Dexterous manipulation |
| **Motion capture** | Full body | Low | Hard (setup) | Locomotion + manipulation |

### By Control Mode

**Joint-space teleoperation**: Operator commands map directly to robot joint angles. Simple but unintuitive for complex robots.

**Task-space teleoperation**: Operator commands map to end-effector position/orientation (Cartesian space). More intuitive but requires inverse kinematics.

**Retargeting-based**: Map human body motion to robot body motion, accounting for morphology differences.

## Key Systems

### ALOHA (A Low-cost Open-source Hardware System for Bimanual Teleoperation)

**ALOHA** (Zhao et al., 2023) is an influential low-cost teleoperation system:

- **Hardware**: Leader-follower arm pairs (operator moves leader, follower copies)
- **Cost**: ~$20K total (vs. $100K+ for industrial systems)
- **Capabilities**: Fine-grained bimanual manipulation
- **Data quality**: High-quality demonstrations for imitation learning (ACT policy)

**Mobile ALOHA**: Extends ALOHA with a mobile base for whole-room tasks.

### GELLO

**GELLO** (Wu et al., 2024): A general, low-cost teleoperation device:

- 3D-printed, kinematically matched to the target robot arm
- Low-latency joint-space control
- Can be built for ~$200

### UMI (Universal Manipulation Interface)

**UMI** (Chi et al., 2024): A hand-held gripper with tracking:

- Operator holds and moves a gripper directly
- Tracking via GoPro + SLAM provides 6-DOF pose
- No robot needed during demonstration — data collected in any environment
- Policy trained in simulation, deployed on various robot arms

### VR-Based Systems

VR headsets (Meta Quest, Apple Vision Pro) provide:

- Stereoscopic camera view from robot head
- 6-DOF hand tracking per hand
- Finger tracking for dexterous manipulation
- Immersive experience for the operator

### Exoskeleton-Based Systems

For humanoid robots:

- Full-body motion capture (suit or marker-based)
- Real-time retargeting from human skeleton to robot skeleton
- Handles morphology differences (different limb lengths, DOF)

## Retargeting: Human to Robot

When human and robot have different morphologies, **retargeting** maps human motion to robot motion:

### Position-Based Retargeting

Map human keypoint positions to robot end-effector positions:

$$
p_{\text{robot}}^{\text{ee}} = \text{scale} \cdot (p_{\text{human}}^{\text{hand}} - p_{\text{human}}^{\text{ref}}) + p_{\text{robot}}^{\text{ref}}
$$

Then use inverse kinematics (IK) to solve for robot joint angles.

### Joint-Angle Retargeting

Map human joint angles directly to robot joint angles, with appropriate scaling:

$$
q_{\text{robot}} = A \cdot q_{\text{human}} + b
$$

where $A$ and $b$ account for joint range differences and kinematic mapping.

### Optimization-Based Retargeting

Solve an optimization problem at each frame:

$$
q_t^* = \arg\min_q \sum_i w_i \| \text{FK}_i(q) - p_i^{\text{target}} \|^2 + \lambda \| q - q_{t-1} \|^2
$$

where $\text{FK}_i$ is forward kinematics for keypoint $i$, $p_i^{\text{target}}$ is the desired position, and the second term ensures smoothness.

## Data Quality for Learning

The quality of teleoperation data critically affects downstream policy learning:

### Factors Affecting Data Quality

| Factor | Impact | Mitigation |
|--------|--------|------------|
| **Operator skill** | Large — expert demonstrations are much more useful | Training, practice sessions |
| **Control latency** | Delays cause jerky, suboptimal motions | Low-latency hardware, predictive display |
| **Workspace mismatch** | Human and robot workspaces differ | Careful calibration, scaling |
| **Recording artifacts** | Noise, dropped frames, calibration errors | Post-processing, filtering |

### Best Practices

1. **Consistent setup**: Same camera angles, lighting, object placement
2. **Multiple operators**: Diverse demonstration styles improve generalization
3. **Task decomposition**: Collect demonstrations for subtasks when full tasks are too long
4. **Quality filtering**: Review and discard failed or low-quality demonstrations
5. **Annotation**: Record task success/failure labels, phase boundaries, language descriptions

## Key References

- Zhao, T.Z., et al. (2023). "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware." *RSS*.
- Wu, H., et al. (2024). "GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators." *RSS*.
- Chi, C., et al. (2024). "Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots." *RSS*.
- Cheng, X., et al. (2024). "Open-TeleVision: Teleoperation with Immersive Active Visual Feedback." *arXiv*.
- He, L., et al. (2024). "OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning." *arXiv*.
