# Read the Docs Learning Site Design

Date: 2026-04-16

## Goal

Turn this repository into a comprehensive, incrementally maintainable Read the Docs style learning resource for junior PhD students studying reinforcement learning, world models, embodied AI, robot learning practice, and distributed reinforcement learning systems.

The first version should be a working bilingual documentation site with real introductory content, not only an empty scaffold.

## Audience

The primary audience is early-stage PhD students who need a structured path from reinforcement learning fundamentals toward modern embodied intelligence research. They may have basic machine learning background, but should not be assumed to know practical RL experimentation, robot learning workflows, world model literature, or distributed RL system architecture.

## Technical Approach

Use Sphinx as the documentation builder, Read the Docs theme for presentation, and MyST Parser so pages can be written in Markdown. This keeps the project close to the standard Read the Docs/Sphinx ecosystem while making future writing and review easier than reStructuredText-only documentation.

The documentation should include:

- `sphinx_rtd_theme` for Read the Docs style navigation and search.
- `myst_parser` for Markdown source pages.
- `.readthedocs.yaml` for hosted builds.
- `requirements.txt` for reproducible documentation dependencies.
- `docs/Makefile` and `docs/source/conf.py` for local builds.
- `README.md` for project overview and local development.
- `CONTRIBUTING.md` for future updates, bilingual maintenance rules, and page template conventions.

## Language Strategy

Use standard separate language trees:

```text
docs/source/zh_CN/
docs/source/en/
```

The root `docs/source/index.md` is a language selection page. `docs/source/zh_CN/index.md` and `docs/source/en/index.md` are the main entry points for each language.

The two language trees must keep matching directory structures and page slugs. For example:

```text
docs/source/zh_CN/rl_basics/index.md
docs/source/en/rl_basics/index.md
```

Chinese is the primary authoring language for the first version. English pages should be readable first drafts or concise matching versions, not broken placeholders. New pages added later should be added to both language trees at the same time, even if one language starts shorter.

## Information Architecture

The site should be organized as a textbook-like learning path rather than a flat collection of notes.

### Part 0: Orientation

Purpose: explain how to use the resource and what preparation is expected.

Topics:

- Intended audience.
- Suggested learning paths.
- Prerequisites in math, control, deep learning, and robotics.
- How to read papers, reproduce experiments, and maintain research notes.

### Part I: Reinforcement Learning Basics

Purpose: provide the foundation needed for later world model, robot learning, and distributed RL topics.

Topics:

- RL problem formulation: MDPs, POMDPs, trajectories, rewards, returns, policies, value functions.
- Policy gradient, actor-critic, Q-learning, and model-based RL.
- Exploration, credit assignment, and training stability.
- Practical RL experiment design: seeds, logging, evaluation, and reproducibility.
- External learning resources.

The RL Basics navigation must include OpenAI Spinning Up as an external reference:

```text
https://spinningup.openai.com/en/latest/
```

Spinning Up should be presented as a recommended classical RL foundation and algorithm implementation reference. The site should link to it and explain how to use it alongside this resource, but should not copy Spinning Up content.

### Part II: World Models

Purpose: introduce predictive and latent models as tools for planning, policy learning, and embodied intelligence.

Topics:

- Core world model concepts.
- Latent dynamics and sequence modeling.
- Predictive representations.
- Model learning and planning.
- Dreamer-style agents and embodied world models.
- Limitations such as compounding error, partial observability, and sim-to-real gaps.

### Part III: Embodied AI Foundations

Purpose: connect abstract RL notation to embodied agents with sensors, bodies, actuators, and environments.

Topics:

- Embodiment and task formulation.
- Observation and action spaces.
- Proprioception, vision, tactile sensing, and multimodal signals.
- Simulation and real robot constraints.
- Benchmarks and evaluation.

### Part IV: Robot Learning Practice

Purpose: cover the practical embodied topics requested for the first version.

Topics:

- Locomotion.
- Loco-manipulation.
- Teleoperation.
- Data collection.
- Imitation learning and offline datasets.
- Safety, reset, and evaluation protocols.

### Part V: Distributed RL Systems

Purpose: explain how large-scale RL training systems are structured and debugged.

Topics:

- Rollout workers, learners, replay buffers, and parameter servers.
- Synchronous and asynchronous training.
- Distributed data collection.
- Experiment orchestration.
- Fault tolerance and reproducibility.

### Part VI: Research Practice

Purpose: provide durable habits and reusable templates for graduate research.

Topics:

- Reading lists.
- Paper summary templates.
- Implementation checklists.
- Experiment reports.
- Suggested projects.

## Page Template

Each major chapter page should follow a consistent structure:

```text
# Chapter Title

## Learning Goals
## Prerequisites
## Core Concepts
## Mathematical Formulation
## Algorithms / System Design
## Practical Notes
## Common Pitfalls
## Recommended Reading
## Exercises / Research Questions
## Glossary
```

Short overview pages may omit sections that do not apply, but the first version should use this template for core topic pages wherever it improves consistency.

## First-Version Content Scope

The initial implementation should include enough real content to make the site useful immediately:

- Root language selection page.
- Chinese and English home pages.
- Overview pages for all six major parts.
- A substantive RL Basics page that includes the Spinning Up external reference.
- Introductory pages for world models, embodied AI, robot learning practice, distributed RL systems, and research practice.
- Contribution and maintenance documentation.

The first version does not need to be a complete textbook. It should establish the site structure, writing conventions, bilingual maintenance model, and a set of coherent starter pages that can be expanded incrementally.

## Navigation Requirements

The navigation should make the learning path obvious:

1. Start with orientation and prerequisites.
2. Move through RL foundations.
3. Introduce world models.
4. Connect to embodied intelligence.
5. Cover locomotion, loco-manipulation, teleoperation, and data collection.
6. Explain distributed RL architecture.
7. End with research practice resources.

Within RL Basics, the navigation should expose both internal foundations and the external Spinning Up reference.

## Visual and Presentation Requirements

The site should feel like a serious research learning resource, not a marketing page. The home pages should prioritize immediate entry into the learning path, similar in spirit to OpenAI Spinning Up's documentation-first presentation.

Use the default Read the Docs theme styling unless there is a clear reason to customize it. Avoid decorative design work in the first version; invest effort in clear structure, readable pages, and maintainable navigation.

## Update and Contribution Rules

`CONTRIBUTING.md` should define:

- How to build the docs locally.
- How to add a new page.
- The requirement to add matching Chinese and English pages.
- The standard page template.
- Citation and external link expectations.
- How to keep reading lists current.

## Testing and Verification

The implementation should verify:

- Sphinx can build HTML locally without broken internal references.
- The root language selection page links to both language sites.
- Chinese and English navigation trees build successfully.
- The RL Basics pages include the Spinning Up external link.
- README instructions are accurate.

If dependency installation is unavailable in the environment, the final report should clearly state which verification commands could not be run and why.

## Out of Scope for First Version

- Full textbook-length coverage of every chapter.
- Automated machine translation workflow.
- Custom Sphinx theme development.
- Hosted Read the Docs project setup outside this repository.
- Interactive notebooks or executable RL code examples.
- CI beyond the Read the Docs configuration and local build instructions.
