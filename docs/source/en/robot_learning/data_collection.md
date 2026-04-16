# Data Collection

## Scope and Motivation

Robot data collection is an experimental system, not passive logging. The collection strategy determines coverage, failure distribution, action executability, annotation quality, and downstream algorithm validity. A large dataset without schema, synchronization, and versioning is difficult to use for reproducible research.

## Problem Setting

An episode usually contains sensor observations, robot state, human input or policy actions, rewards or task labels, termination conditions, reset information, and metadata. For multi-camera, multi-robot, or human-in-the-loop systems, timestamp synchronization and coordinate-frame records are as important as the data values themselves. Failure samples should be retained because the failure distribution defines the policy boundary.

## System / Algorithmic View

A collection system can be divided into acquisition, validation, annotation, storage, and indexing. Acquisition records synchronized streams. Validation checks dropped frames, action saturation, sensor anomalies, and safety events. Annotation produces success, phase, failure reason, or language instruction labels. Storage preserves raw and processed data. Indexing supports filtering by task, scene, object, and quality.

## Implementation Notes

A minimal episode schema should include:

| Field | Description |
| --- | --- |
| `episode_id` | Globally unique identifier including dataset version and collection batch. |
| `timestamps` | Clock records for sensors, actions, and events. |
| `observations` | Images, proprioception, force, language, or task specification. |
| `actions` | Human input, policy output, and low-level control command. |
| `labels` | Success, phase, failure reason, and quality flag. |
| `reset` | Initial state, reset method, and human intervention. |
| `metadata` | Hardware, software, calibration, scene, operator, and task parameters. |

## Experimental Protocol

Dataset reports should specify task distribution, collection strategy, number of operators, autonomous-to-human ratio, failure-retention rules, quality checks, annotation process, version number, and exclusion criteria. For continuously updated datasets, training and evaluation should cite explicit versions rather than mutable directories.

## Failure Modes and Limitations

Common failures include timestamp drift, camera extrinsic changes, incorrect episode boundaries, filtering out failures, mismatch between success labels and true task completion, missing metadata, and preprocessing scripts overwriting raw data. Insufficient coverage makes offline evaluation optimistic, especially for long-tail initial states and contact failures.

## References

- Brohan et al., RT-1: large-scale robot data and task-conditioned policies.
- Walke et al., "BridgeData V2": multi-task robot dataset construction.
- Open X-Embodiment Collaboration, RT-X: cross-embodiment data integration and policy training.
