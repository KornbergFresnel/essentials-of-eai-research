# Loco-Manipulation

## Scope and Motivation

Loco-manipulation refers to tasks where mobility and manipulation are coupled rather than separable. Base or leg motion changes manipulation reachability, while arms and payloads change center of mass, contact, and stability. The problem is harder than isolated locomotion or fixed-base manipulation because a policy must coordinate navigation, contact, grasping, object state, and whole-body control.

## Problem Setting

Representative tasks include mobile manipulators carrying objects, quadrupeds opening doors, whole-body pick-and-place, and mobile bimanual manipulation. Observations often require robot body state, end-effector pose, object pose, contact or grasp state, local maps, and task progress. Important variables such as grasp force, friction, object mass, and occluded contact state may remain hidden.

## System / Algorithmic View

Systems can be end-to-end, hierarchical, or hybrid planning-control architectures. Hierarchical systems often decompose the task into base navigation, reaching, grasping, transport, and placement. If the decomposition boundary is too rigid, failures appear during contact-rich transitions. Whole-body controllers can handle base, arm, and posture constraints jointly, but the policy interface must specify whether actions are high-level targets, end-effector velocities, or whole-body joint commands.

## Implementation Notes

Documentation should record base and arm control frequencies, coordinate frames, collision checking, grasp representation, object-pose source, and recovery behavior. If a policy uses exact object pose, the source must be clear: perception, markers, simulator state, or offline annotation. For long-horizon tasks, logs should record stage entry time, exit condition, and failure type.

## Experimental Protocol

Evaluation should not only report final success. It should decompose progress into reaching, contact establishment, stable grasp, transport, placement, and recovery. Partial-success metrics help locate whether failure comes from locomotion, perception, grasping, or task planning. Initial object placement, environment layout, payload mass, and obstacles should be separated between training and test distributions.

## Failure Modes and Limitations

Common failures include base-arm interference, payload-induced instability, contact-state misclassification, conflict between path planning and manipulation goals, and long-horizon error accumulation. Idealized simulated grasps and rigid contacts can substantially overestimate hardware performance. If reset requires manual object and robot recovery, experimental throughput becomes a central system bottleneck.

## References

- Fu et al., "Mobile ALOHA": mobile manipulation data collection and imitation system.
- Cheng et al., "Learning Whole-Body Manipulation for Quadrupedal Robots": whole-body manipulation for legged robots.
- Khatib, "A Unified Approach for Motion and Force Control of Robot Manipulators": classical constrained manipulation control.
