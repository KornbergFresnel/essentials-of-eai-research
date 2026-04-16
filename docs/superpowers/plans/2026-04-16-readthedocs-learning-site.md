# Read the Docs Learning Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a bilingual Sphinx/Read the Docs learning site for reinforcement learning, world models, embodied AI, robot learning practice, and distributed RL systems.

**Architecture:** The site uses Sphinx with the Read the Docs theme and MyST Markdown. A root language selection page links to parallel `zh_CN` and `en` documentation trees with matching slugs and navigation. The first version includes real introductory content, maintenance docs, and local/Read the Docs build configuration.

**Tech Stack:** Python docs tooling, Sphinx, sphinx-rtd-theme, MyST Parser, Markdown, Read the Docs configuration.

---

## File Structure

- Create `.gitignore`: ignore generated docs builds, Python caches, virtual environments, and `.superpowers/`.
- Create `.readthedocs.yaml`: configure Read the Docs to install `requirements.txt` and build `docs/source`.
- Create `requirements.txt`: pin documentation dependencies.
- Create `README.md`: describe project purpose, language structure, and local build workflow.
- Create `CONTRIBUTING.md`: define bilingual maintenance, page template, links, and contribution workflow.
- Create `docs/Makefile`: standard Sphinx local build commands.
- Create `docs/source/conf.py`: Sphinx project metadata, theme, MyST support, source suffixes, static path, and exclude patterns.
- Create `docs/source/index.md`: root language selection page.
- Create `docs/source/zh_CN/index.md`: Chinese home page and toctree.
- Create `docs/source/en/index.md`: English home page and toctree.
- Create matching overview pages in:
  - `docs/source/zh_CN/orientation/index.md`
  - `docs/source/zh_CN/rl_basics/index.md`
  - `docs/source/zh_CN/world_models/index.md`
  - `docs/source/zh_CN/embodied_ai/index.md`
  - `docs/source/zh_CN/robot_learning/index.md`
  - `docs/source/zh_CN/distributed_rl/index.md`
  - `docs/source/zh_CN/research_practice/index.md`
  - `docs/source/en/orientation/index.md`
  - `docs/source/en/rl_basics/index.md`
  - `docs/source/en/world_models/index.md`
  - `docs/source/en/embodied_ai/index.md`
  - `docs/source/en/robot_learning/index.md`
  - `docs/source/en/distributed_rl/index.md`
  - `docs/source/en/research_practice/index.md`
- Create `docs/source/_static/.gitkeep`: keep the static asset directory in git.

## Task 1: Add Repository Hygiene and Documentation Dependencies

**Files:**
- Create: `.gitignore`
- Create: `requirements.txt`
- Create: `.readthedocs.yaml`

- [ ] **Step 1: Write repository hygiene and dependency files**

Create `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Virtual environments
.venv/
venv/
env/

# Sphinx builds
docs/build/
docs/source/_build/

# Local brainstorming/session state
.superpowers/

# OS/editor noise
.DS_Store
```

Create `requirements.txt`:

```text
sphinx==7.4.7
sphinx-rtd-theme==2.0.0
myst-parser==3.0.1
```

Create `.readthedocs.yaml`:

```yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"

sphinx:
  configuration: docs/source/conf.py

python:
  install:
    - requirements: requirements.txt
```

- [ ] **Step 2: Verify files are present**

Run:

```bash
test -f .gitignore && test -f requirements.txt && test -f .readthedocs.yaml
```

Expected: command exits with status `0`.

- [ ] **Step 3: Commit**

```bash
git add .gitignore requirements.txt .readthedocs.yaml
git commit -m "build: add docs dependencies and rtd config"
```

## Task 2: Add Sphinx Build Configuration

**Files:**
- Create: `docs/Makefile`
- Create: `docs/source/conf.py`
- Create: `docs/source/_static/.gitkeep`

- [ ] **Step 1: Add Sphinx build files**

Create `docs/Makefile`:

```makefile
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help clean html linkcheck

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)"

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

linkcheck:
	@$(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
```

Create `docs/source/conf.py`:

```python
from __future__ import annotations

from pathlib import Path

project = "Essentials of Embodied AI Research"
author = "Ming Zhou"
copyright = "2026, Ming Zhou"

root_doc = "index"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = project

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "substitution",
]

myst_heading_anchors = 3

language = "en"
locale_dirs = ["locale/"]
gettext_compact = False

_static_dir = Path(__file__).parent / "_static"
_static_dir.mkdir(exist_ok=True)
```

Create `docs/source/_static/.gitkeep` as an empty file.

- [ ] **Step 2: Verify config imports**

Run:

```bash
python -m py_compile docs/source/conf.py
```

Expected: command exits with status `0`.

- [ ] **Step 3: Commit**

```bash
git add docs/Makefile docs/source/conf.py docs/source/_static/.gitkeep
git commit -m "build: configure sphinx documentation"
```

## Task 3: Add Root and Bilingual Home Pages

**Files:**
- Create: `docs/source/index.md`
- Create: `docs/source/zh_CN/index.md`
- Create: `docs/source/en/index.md`

- [ ] **Step 1: Add root language selection page**

Create `docs/source/index.md`:

````markdown
# Essentials of Embodied AI Research

This site is a bilingual learning resource for reinforcement learning, world models, embodied AI, robot learning practice, and distributed reinforcement learning systems.

Choose a language:

```{toctree}
:maxdepth: 1
:caption: Languages

中文 <zh_CN/index>
English <en/index>
```
````

- [ ] **Step 2: Add Chinese home page**

Create `docs/source/zh_CN/index.md`:

````markdown
# 具身智能研究基础

这是一份面向低年级博士生的学习资料，围绕强化学习、世界模型、具身智能、机器人学习实践和分布式强化学习系统展开。它的目标不是替代论文阅读，而是给你一条清晰的进入路径：先建立概念坐标，再理解算法和系统，最后形成可复现实验与研究判断。

## 如何使用

- 如果你刚开始做强化学习，先读“使用指南”和“强化学习基础”。
- 如果你已经熟悉基础 RL，可以从“世界模型”和“具身智能基础”开始。
- 如果你的课题靠近机器人实验，优先阅读“机器人学习实践”。
- 如果你需要搭建训练系统或大规模数据采集流程，阅读“分布式强化学习系统”。

```{toctree}
:maxdepth: 2
:caption: 学习路径

orientation/index
rl_basics/index
world_models/index
embodied_ai/index
robot_learning/index
distributed_rl/index
research_practice/index
```

[English version](../en/index.md)
````

- [ ] **Step 3: Add English home page**

Create `docs/source/en/index.md`:

````markdown
# Essentials of Embodied AI Research

This is a learning resource for junior PhD students working toward reinforcement learning, world models, embodied AI, robot learning practice, and distributed reinforcement learning systems. It is designed to help you build conceptual orientation first, then connect algorithms, systems, experiments, and research habits.

## How to Use This Site

- If you are new to reinforcement learning, start with Orientation and RL Basics.
- If you already know basic RL, begin with World Models and Embodied AI Foundations.
- If your project involves robot experiments, focus on Robot Learning Practice.
- If you need to build training or data collection infrastructure, read Distributed RL Systems.

```{toctree}
:maxdepth: 2
:caption: Learning Path

orientation/index
rl_basics/index
world_models/index
embodied_ai/index
robot_learning/index
distributed_rl/index
research_practice/index
```

[中文版](../zh_CN/index.md)
````

- [ ] **Step 4: Build and verify expected warnings**

Run:

```bash
python -m sphinx -b html docs/source docs/build/html -W
```

Expected before topic pages exist: FAIL with warnings/errors for missing toctree documents. This confirms Sphinx sees the root pages and now needs the linked topic files.

- [ ] **Step 5: Commit**

```bash
git add docs/source/index.md docs/source/zh_CN/index.md docs/source/en/index.md
git commit -m "docs: add bilingual documentation entry points"
```

## Task 4: Add Chinese Learning Path Pages

**Files:**
- Create: `docs/source/zh_CN/orientation/index.md`
- Create: `docs/source/zh_CN/rl_basics/index.md`
- Create: `docs/source/zh_CN/world_models/index.md`
- Create: `docs/source/zh_CN/embodied_ai/index.md`
- Create: `docs/source/zh_CN/robot_learning/index.md`
- Create: `docs/source/zh_CN/distributed_rl/index.md`
- Create: `docs/source/zh_CN/research_practice/index.md`

- [ ] **Step 1: Create Chinese orientation page**

Create `docs/source/zh_CN/orientation/index.md`:

```markdown
# 使用指南

## Learning Goals

读完本章后，你应该能够判断自己该从哪一部分开始，知道学习强化学习和具身智能研究需要哪些先修知识，并建立一种可持续更新的研究笔记习惯。

## Prerequisites

建议具备基本概率论、线性代数、优化、深度学习和 Python 实验经验。机器人方向的读者还应熟悉基本动力学、控制和仿真概念。

## Core Concepts

这份资料按照“问题定义 - 算法 - 具身约束 - 系统架构 - 研究实践”的顺序组织。低年级博士不需要一次读完所有内容，但需要知道每一层在研究中的作用。

## Practical Notes

阅读时建议维护三类笔记：概念卡片、论文摘要和实验记录。概念卡片回答“这个对象是什么”；论文摘要回答“这篇工作解决了什么问题”；实验记录回答“我做了什么、结果如何、下一步是什么”。

## Common Pitfalls

- 只看算法公式，不记录实验设置。
- 只调工程参数，不回到问题定义。
- 只复现单个结果，不比较 baseline 和 ablation。

## Recommended Reading

- Sutton and Barto, *Reinforcement Learning: An Introduction*.
- OpenAI Spinning Up for classical deep RL background.

## Exercises / Research Questions

写一页自己的研究地图：你的课题中哪些部分是 RL，哪些部分是世界模型，哪些部分是机器人系统，哪些部分是实验基础设施？

## Glossary

- 轨迹：智能体与环境交互得到的状态、动作、奖励序列。
- 可复现性：他人或未来的你能根据记录重新得到可比较结果的程度。
```

- [ ] **Step 2: Create Chinese RL Basics page with Spinning Up link**

Create `docs/source/zh_CN/rl_basics/index.md`:

```markdown
# 强化学习基础

## Learning Goals

本章帮助你建立强化学习的基本语言：什么是环境、状态、动作、奖励、策略、价值函数和回报，以及这些概念如何连接到机器人和世界模型研究。

## Prerequisites

你应熟悉基本概率、期望、梯度下降和神经网络训练。若对控制理论有基础，会更容易理解连续控制任务。

## Core Concepts

强化学习研究智能体如何通过与环境交互来优化长期目标。标准形式通常用马尔可夫决策过程描述：环境在状态之间转移，智能体根据策略选择动作，并从奖励信号中学习。

在具身智能中，状态通常不能被完整观测。机器人只能看到传感器读数、关节状态、图像或触觉信号，因此很多问题更接近部分可观测马尔可夫决策过程。

## Mathematical Formulation

一个 MDP 可以写作五元组 $(S, A, P, R, \gamma)$。策略 $\pi(a|s)$ 给出在状态 $s$ 下选择动作 $a$ 的概率。目标通常是最大化折扣回报：

$$
J(\pi)=\mathbb{E}_{\tau \sim \pi}\left[\sum_{t=0}^{T}\gamma^t r_t\right].
$$

价值函数 $V^\pi(s)$ 估计从状态 $s$ 出发的期望回报，动作价值函数 $Q^\pi(s,a)$ 估计从状态动作对出发的期望回报。

## Algorithms / System Design

常见算法族包括：

- Policy Gradient：直接优化策略参数，适合连续动作，但方差较高。
- Actor-Critic：同时学习策略和价值函数，用 critic 降低梯度估计方差。
- Q-Learning：学习动作价值函数，常用于离散动作或经过特殊处理的连续控制。
- Model-Based RL：学习或使用环境模型进行规划，和世界模型研究直接相关。

## Practical Notes

实践中的 RL 往往比公式更脆弱。你需要记录随机种子、环境版本、奖励设计、终止条件、归一化方式、评估频率和 checkpoint。单条 learning curve 很少足够支撑结论。

## Common Pitfalls

- 把训练回报当成最终性能，而不做独立评估。
- 调奖励函数后不记录变更，导致实验不可比较。
- 忽略环境 reset、early termination 和 safety constraint 对结果的影响。
- 在机器人任务中默认仿真状态完全可观测，导致方法无法迁移到真实系统。

## Recommended Reading

- [OpenAI Spinning Up](https://spinningup.openai.com/en/latest/)：经典深度强化学习概念、算法和实现参考。建议与本章并行阅读，用它补足 PPO、TRPO、SAC、DDPG 等算法细节。
- Sutton and Barto, *Reinforcement Learning: An Introduction*.
- Lillicrap et al., Continuous control with deep reinforcement learning.
- Haarnoja et al., Soft Actor-Critic.

## Exercises / Research Questions

1. 选一个机器人任务，把它写成 MDP 或 POMDP：观测是什么，动作是什么，奖励如何定义？
2. 比较 policy gradient 和 actor-critic：critic 在实际训练中解决了什么问题，又引入了什么风险？
3. 阅读 Spinning Up 中一个算法页面，写出它的目标函数、主要近似和实现假设。

## Glossary

- MDP：状态完全可观测的强化学习问题形式。
- POMDP：智能体只能获得部分观测的问题形式。
- 策略：从观测或状态到动作分布的映射。
- 回报：沿一条轨迹累积得到的长期奖励。
- World Model：对环境动态、观测或潜在状态演化的预测模型。
```

- [ ] **Step 3: Create remaining Chinese overview pages**

Create `docs/source/zh_CN/world_models/index.md`:

```markdown
# 世界模型

## Learning Goals

本章介绍世界模型为什么重要、它预测什么、如何用于规划和策略学习，以及它在具身任务中经常遇到哪些失败模式。

## Prerequisites

建议先理解 MDP/POMDP、监督学习、序列建模和基本强化学习算法。

## Core Concepts

世界模型是智能体对环境变化规律的内部预测模型。它可以预测下一状态、未来观测、奖励、终止条件，或在潜在空间中预测抽象动态。

## Mathematical Formulation

一个常见形式是学习 $p_\theta(z_{t+1}, r_t | z_t, a_t)$，其中 $z_t$ 是由观测编码得到的潜在状态。策略可以在真实环境中学习，也可以在模型生成的 imagined rollout 中学习。

## Algorithms / System Design

世界模型系统通常包含 encoder、dynamics model、reward model、decoder 或 prediction head，以及使用模型进行 planning 或 policy optimization 的模块。

## Practical Notes

模型预测误差会沿时间累积。短期预测准确不代表长期 rollout 可用。评估时应同时看 one-step prediction、多步 rollout、策略性能和模型失效案例。

## Common Pitfalls

- 只优化像素重建，忽略任务相关信息。
- 在训练分布外 rollout 过长。
- 不区分表示学习失败和控制策略失败。

## Recommended Reading

- Ha and Schmidhuber, World Models.
- Hafner et al., Dreamer 系列工作。
- Sutton, Dyna architecture.

## Exercises / Research Questions

为一个移动机器人任务设计世界模型：哪些变量应进入潜在状态，哪些预测目标对控制最有帮助？

## Glossary

- 潜在状态：从高维观测中压缩出的任务相关表示。
- Imagined rollout：在学习到的模型中展开的虚拟轨迹。
```

Create `docs/source/zh_CN/embodied_ai/index.md`:

```markdown
# 具身智能基础

## Learning Goals

本章把抽象 RL 概念连接到有身体的智能体：传感器、执行器、动力学、环境约束和真实实验成本。

## Prerequisites

建议具备基本机器人学、控制、强化学习和深度学习背景。

## Core Concepts

具身智能研究智能体如何通过身体与环境交互。身体不是算法外部的细节，它决定了动作空间、观测模式、探索风险和任务可行性。

## Mathematical Formulation

具身任务通常更接近 POMDP：智能体得到观测 $o_t$，执行动作 $a_t$，环境状态 $s_t$ 可能包含不可直接测量的接触、物体属性或外部扰动。

## Algorithms / System Design

具身系统需要把 perception、state estimation、policy、low-level control、安全监控和数据记录连接起来。学习算法必须和控制频率、传感器延迟、执行器限制共同设计。

## Practical Notes

仿真任务应记录物理参数、domain randomization、控制频率和 reset 逻辑。真实机器人实验应记录硬件状态、校准流程和失败恢复方案。

## Common Pitfalls

- 把仿真中的 privileged state 当作真实机器人可用输入。
- 忽略控制频率和 latency。
- 只报告成功案例，不分析失败分布。

## Recommended Reading

- Levine et al., learning hand-eye coordination.
- Tobin et al., domain randomization.
- OpenAI et al., dexterous manipulation from pixels.

## Exercises / Research Questions

选择一个具身任务，列出它的观测、动作、动力学约束、安全约束和评估指标。

## Glossary

- Proprioception：机器人自身状态感知，如关节角、速度和力矩。
- Sim-to-real：从仿真训练迁移到真实硬件。
```

Create `docs/source/zh_CN/robot_learning/index.md`:

```markdown
# 机器人学习实践

## Learning Goals

本章关注 locomotion、loco-manipulation、遥操和数据采集这些当前最需要先建立工程直觉的主题。

## Prerequisites

建议先理解强化学习基础、具身任务建模和基本机器人控制。

## Core Concepts

机器人学习不是单纯训练一个 policy。你还需要决定数据如何来、任务如何 reset、失败如何处理、动作由谁执行、评估如何保证公平。

## Algorithms / System Design

- Locomotion：关注稳定性、速度、能耗、地形适应和扰动恢复。
- Loco-manipulation：同时处理移动和操作，难点在接触、长时程目标和全身协调。
- Teleoperation：用人类操作生成演示数据，也可作为安全 fallback。
- Data Collection：设计覆盖任务分布的数据流程，记录 observation、action、reward、success、metadata。

## Practical Notes

数据采集系统应记录时间戳、控制频率、坐标系、相机参数、机器人状态和人工标注。没有 metadata 的机器人数据通常很难复用。

## Common Pitfalls

- 只追求数据量，不控制数据质量和覆盖范围。
- 忽略 reset 成本，使实验吞吐远低于预期。
- 遥操接口和学习 policy 的动作空间不一致。

## Recommended Reading

- Kumar et al., RMA for legged locomotion.
- Brohan et al., RT-1 and RT-2.
- Fu et al., Mobile ALOHA.

## Exercises / Research Questions

设计一个遥操采集协议：每条 episode 需要记录哪些数据，如何标记失败，如何保证后续训练可用？

## Glossary

- Loco-manipulation：移动和操作同时发生的机器人任务。
- Teleoperation：人类远程控制机器人执行任务。
- Dataset metadata：描述数据采集条件、设备、任务和质量的信息。
```

Create `docs/source/zh_CN/distributed_rl/index.md`:

```markdown
# 分布式强化学习系统

## Learning Goals

本章解释大规模强化学习系统如何把采样、学习、回放、评估和实验管理连接起来。

## Prerequisites

建议先理解基本 RL 训练循环、深度学习训练和常见并行计算概念。

## Core Concepts

分布式 RL 的核心矛盾是数据由环境交互产生，而学习又会不断改变策略。系统需要在吞吐、样本效率、策略新鲜度和稳定性之间取舍。

## Algorithms / System Design

典型组件包括 rollout worker、learner、replay buffer、parameter server、evaluator 和 experiment manager。同步系统更容易分析，异步系统吞吐更高但更难调试 stale policy。

## Practical Notes

系统日志应同时记录环境步数、梯度步数、样本延迟、队列长度、worker 崩溃、评估指标和 checkpoint。只看 reward curve 无法定位系统瓶颈。

## Common Pitfalls

- 混淆 sample throughput 和 learning progress。
- 不记录 policy version，导致数据来源不可追踪。
- evaluator 使用训练环境状态或不固定评估协议。

## Recommended Reading

- Espeholt et al., IMPALA.
- Horgan et al., Ape-X.
- Ray RLlib documentation for system patterns.
- CleanRL for single-file algorithm baselines.

## Exercises / Research Questions

画出一个 distributed actor-learner 系统，并标注每条数据流的延迟、失败模式和日志指标。

## Glossary

- Rollout worker：负责和环境交互、生成轨迹的进程。
- Learner：负责根据数据更新模型参数的进程。
- Replay buffer：存储经验数据供 off-policy 学习使用的组件。
```

Create `docs/source/zh_CN/research_practice/index.md`:

```markdown
# 研究实践

## Learning Goals

本章提供论文阅读、实验记录、实现检查和课题推进的基本工作流。

## Prerequisites

你应已经有一个大致研究方向，或至少知道自己关注算法、机器人任务、数据还是系统。

## Core Concepts

研究实践的目标是让判断可追踪。每个结论都应能回到论文证据、实验记录、代码版本和评估协议。

## Practical Notes

建议为每篇论文记录四件事：问题、方法、关键假设、可复现实验。建议为每个实验记录配置、代码提交、数据版本、随机种子、指标和失败观察。

## Common Pitfalls

- 读论文只摘结论，不记录假设。
- 复现实验不固定版本。
- 把实现 bug 误判为算法问题。

## Recommended Reading

- Papers With Code for baseline and benchmark tracking.
- The ML reproducibility checklist.
- Lab-specific paper reading templates.

## Exercises / Research Questions

选一篇与你课题相关的论文，写一页复现计划：最小可复现实验是什么，需要哪些数据、代码和算力？

## Glossary

- Ablation：移除或改变系统组件来判断其贡献的实验。
- Baseline：用于比较新方法是否真正有效的参考方法。
```

- [ ] **Step 4: Verify Chinese page paths**

Run:

```bash
test -f docs/source/zh_CN/orientation/index.md && test -f docs/source/zh_CN/rl_basics/index.md && test -f docs/source/zh_CN/world_models/index.md && test -f docs/source/zh_CN/embodied_ai/index.md && test -f docs/source/zh_CN/robot_learning/index.md && test -f docs/source/zh_CN/distributed_rl/index.md && test -f docs/source/zh_CN/research_practice/index.md
```

Expected: command exits with status `0`.

- [ ] **Step 5: Commit**

```bash
git add docs/source/zh_CN
git commit -m "docs: add chinese learning path pages"
```

## Task 5: Add English Learning Path Pages

**Files:**
- Create: `docs/source/en/orientation/index.md`
- Create: `docs/source/en/rl_basics/index.md`
- Create: `docs/source/en/world_models/index.md`
- Create: `docs/source/en/embodied_ai/index.md`
- Create: `docs/source/en/robot_learning/index.md`
- Create: `docs/source/en/distributed_rl/index.md`
- Create: `docs/source/en/research_practice/index.md`

- [ ] **Step 1: Create English orientation page**

Create `docs/source/en/orientation/index.md`:

```markdown
# Orientation

## Learning Goals

After this chapter, you should know where to start, what prerequisites matter, and how to maintain research notes that remain useful as your project changes.

## Prerequisites

You should have basic probability, linear algebra, optimization, deep learning, and Python experiment experience. Robotics readers should also understand basic dynamics, control, and simulation concepts.

## Core Concepts

This resource is organized as a path from problem formulation to algorithms, embodied constraints, system architecture, and research practice. You do not need to read everything at once, but you should understand what each layer contributes to a research project.

## Practical Notes

Maintain three kinds of notes: concept cards, paper summaries, and experiment records. Concept cards explain what an object is. Paper summaries explain what a work contributes. Experiment records explain what you ran, what happened, and what should happen next.

## Common Pitfalls

- Reading algorithm equations without tracking experimental assumptions.
- Tuning engineering details without revisiting the problem definition.
- Reproducing one result without baselines or ablations.

## Recommended Reading

- Sutton and Barto, *Reinforcement Learning: An Introduction*.
- OpenAI Spinning Up for classical deep RL background.

## Exercises / Research Questions

Write a one-page map of your research problem: which parts are reinforcement learning, which parts are world modeling, which parts are robotics, and which parts are experimental infrastructure?

## Glossary

- Trajectory: a sequence of states, actions, and rewards from agent-environment interaction.
- Reproducibility: the degree to which future readers can obtain comparable results from your records.
```

- [ ] **Step 2: Create English RL Basics page with Spinning Up link**

Create `docs/source/en/rl_basics/index.md`:

```markdown
# Reinforcement Learning Basics

## Learning Goals

This chapter establishes the basic language of reinforcement learning: environment, state, action, reward, policy, value function, return, and how these ideas connect to robotics and world model research.

## Prerequisites

You should understand probability, expectation, gradient descent, and neural network training. Control background helps when reading continuous control tasks.

## Core Concepts

Reinforcement learning studies how an agent learns to optimize long-term objectives through interaction with an environment. The standard formalism is the Markov decision process: the environment transitions between states, the agent selects actions through a policy, and learning is driven by rewards.

In embodied intelligence, the full state is usually not observable. A robot receives sensor readings, joint states, images, or tactile signals, so many problems are better treated as partially observable Markov decision processes.

## Mathematical Formulation

An MDP can be written as $(S, A, P, R, \gamma)$. A policy $\pi(a|s)$ defines a distribution over actions in state $s$. The objective is often to maximize discounted return:

$$
J(\pi)=\mathbb{E}_{\tau \sim \pi}\left[\sum_{t=0}^{T}\gamma^t r_t\right].
$$

The value function $V^\pi(s)$ estimates expected return from state $s$, while the action-value function $Q^\pi(s,a)$ estimates expected return from a state-action pair.

## Algorithms / System Design

Common algorithm families include:

- Policy Gradient: directly optimizes policy parameters and is useful for continuous action spaces, but often has high variance.
- Actor-Critic: learns both a policy and a value estimator, using the critic to reduce gradient variance.
- Q-Learning: learns action values and is common for discrete actions or specially handled continuous control.
- Model-Based RL: learns or uses an environment model for planning and connects directly to world model research.

## Practical Notes

Practical RL is more fragile than its notation suggests. Record random seeds, environment versions, reward definitions, termination rules, normalization, evaluation frequency, and checkpoints. One learning curve is rarely enough evidence.

## Common Pitfalls

- Treating training return as final performance without independent evaluation.
- Changing rewards without recording the change.
- Ignoring reset logic, early termination, and safety constraints.
- Assuming privileged simulator state will be available on a real robot.

## Recommended Reading

- [OpenAI Spinning Up](https://spinningup.openai.com/en/latest/): a classical deep RL reference for concepts, algorithms, and implementation details. Read it alongside this chapter for PPO, TRPO, SAC, DDPG, and related algorithms.
- Sutton and Barto, *Reinforcement Learning: An Introduction*.
- Lillicrap et al., Continuous control with deep reinforcement learning.
- Haarnoja et al., Soft Actor-Critic.

## Exercises / Research Questions

1. Choose a robot task and formulate it as an MDP or POMDP: what are the observations, actions, and rewards?
2. Compare policy gradient and actor-critic methods: what problem does the critic solve, and what risks does it introduce?
3. Read one algorithm page in Spinning Up and write down its objective, approximations, and implementation assumptions.

## Glossary

- MDP: a fully observable reinforcement learning problem formalism.
- POMDP: a problem formalism where the agent only receives partial observations.
- Policy: a mapping from observations or states to an action distribution.
- Return: long-term accumulated reward along a trajectory.
- World Model: a predictive model of environment dynamics, observations, or latent state evolution.
```

- [ ] **Step 3: Create remaining English overview pages**

Create `docs/source/en/world_models/index.md`:

```markdown
# World Models

## Learning Goals

This chapter explains why world models matter, what they predict, how they support planning and policy learning, and where they often fail in embodied tasks.

## Prerequisites

You should understand MDPs, POMDPs, supervised learning, sequence modeling, and basic reinforcement learning.

## Core Concepts

A world model is an agent's internal predictive model of how the environment changes. It may predict next states, future observations, rewards, termination, or abstract dynamics in a latent space.

## Mathematical Formulation

A common objective is to learn $p_\theta(z_{t+1}, r_t | z_t, a_t)$, where $z_t$ is a latent state encoded from observations. A policy can learn in the real environment or inside imagined rollouts generated by the model.

## Algorithms / System Design

World model systems often include an encoder, dynamics model, reward model, decoder or prediction head, and a module for planning or policy optimization.

## Practical Notes

Prediction errors compound over time. Accurate one-step prediction does not guarantee useful long rollouts. Evaluate one-step prediction, multi-step rollout quality, policy performance, and model failure cases.

## Common Pitfalls

- Optimizing pixel reconstruction while ignoring task-relevant information.
- Rolling out too far outside the training distribution.
- Confusing representation failure with control policy failure.

## Recommended Reading

- Ha and Schmidhuber, World Models.
- Hafner et al., Dreamer series.
- Sutton, Dyna architecture.

## Exercises / Research Questions

Design a world model for a mobile robot task: which variables should enter the latent state, and which prediction targets are most useful for control?

## Glossary

- Latent state: a task-relevant representation compressed from high-dimensional observations.
- Imagined rollout: a virtual trajectory unrolled inside a learned model.
```

Create `docs/source/en/embodied_ai/index.md`:

```markdown
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
```

Create `docs/source/en/robot_learning/index.md`:

```markdown
# Robot Learning Practice

## Learning Goals

This chapter focuses on locomotion, loco-manipulation, teleoperation, and data collection: topics where early engineering intuition matters.

## Prerequisites

You should understand reinforcement learning basics, embodied task formulation, and basic robot control.

## Core Concepts

Robot learning is not just training a policy. You must decide where data comes from, how tasks reset, how failures are handled, who executes actions, and how evaluation remains fair.

## Algorithms / System Design

- Locomotion: focuses on stability, speed, energy use, terrain adaptation, and disturbance recovery.
- Loco-manipulation: combines movement and manipulation, with challenges in contact, long-horizon goals, and whole-body coordination.
- Teleoperation: uses human control to produce demonstrations and can provide a safety fallback.
- Data Collection: designs coverage over the task distribution and records observations, actions, rewards, success labels, and metadata.

## Practical Notes

Data collection systems should record timestamps, control frequency, coordinate frames, camera parameters, robot state, and human annotations. Robot datasets without metadata are hard to reuse.

## Common Pitfalls

- Optimizing only data volume while ignoring data quality and coverage.
- Ignoring reset cost, which can dominate experiment throughput.
- Using a teleoperation action space that does not match the learned policy action space.

## Recommended Reading

- Kumar et al., RMA for legged locomotion.
- Brohan et al., RT-1 and RT-2.
- Fu et al., Mobile ALOHA.

## Exercises / Research Questions

Design a teleoperation collection protocol: what should each episode record, how should failures be labeled, and how will you ensure the data remains trainable?

## Glossary

- Loco-manipulation: robot tasks where movement and manipulation happen together.
- Teleoperation: remote human control of a robot.
- Dataset metadata: information describing collection conditions, hardware, tasks, and data quality.
```

Create `docs/source/en/distributed_rl/index.md`:

```markdown
# Distributed RL Systems

## Learning Goals

This chapter explains how large-scale reinforcement learning systems connect sampling, learning, replay, evaluation, and experiment management.

## Prerequisites

You should understand the basic RL training loop, deep learning training, and common parallel computing concepts.

## Core Concepts

The central tension in distributed RL is that data comes from environment interaction while learning continuously changes the policy. Systems must trade off throughput, sample efficiency, policy freshness, and stability.

## Algorithms / System Design

Typical components include rollout workers, learners, replay buffers, parameter servers, evaluators, and experiment managers. Synchronous systems are easier to reason about. Asynchronous systems can provide higher throughput but make stale policies harder to debug.

## Practical Notes

System logs should track environment steps, gradient steps, sample latency, queue length, worker crashes, evaluation metrics, and checkpoints. Reward curves alone cannot diagnose system bottlenecks.

## Common Pitfalls

- Confusing sample throughput with learning progress.
- Failing to record policy versions, making data provenance untraceable.
- Letting evaluators use training-only state or unstable evaluation protocols.

## Recommended Reading

- Espeholt et al., IMPALA.
- Horgan et al., Ape-X.
- Ray RLlib documentation for system patterns.
- CleanRL for single-file algorithm baselines.

## Exercises / Research Questions

Draw a distributed actor-learner system and annotate latency, failure modes, and logging metrics for each data flow.

## Glossary

- Rollout worker: a process that interacts with environments and generates trajectories.
- Learner: a process that updates model parameters from data.
- Replay buffer: a component that stores experience for off-policy learning.
```

Create `docs/source/en/research_practice/index.md`:

```markdown
# Research Practice

## Learning Goals

This chapter gives basic workflows for reading papers, recording experiments, checking implementations, and moving a research project forward.

## Prerequisites

You should have a rough research direction, or at least know whether your work is closer to algorithms, robot tasks, data, or systems.

## Core Concepts

Research practice should make judgment traceable. Each conclusion should connect back to paper evidence, experiment records, code versions, and evaluation protocols.

## Practical Notes

For each paper, record the problem, method, key assumptions, and reproducible experiments. For each experiment, record configuration, commit hash, data version, random seeds, metrics, and failure observations.

## Common Pitfalls

- Reading papers by copying conclusions without assumptions.
- Reproducing experiments without fixed versions.
- Mistaking implementation bugs for algorithmic failures.

## Recommended Reading

- Papers With Code for baseline and benchmark tracking.
- The ML reproducibility checklist.
- Lab-specific paper reading templates.

## Exercises / Research Questions

Choose a paper related to your project and write a one-page reproduction plan: what is the smallest reproducible experiment, and what data, code, and compute does it require?

## Glossary

- Ablation: an experiment that removes or changes a component to estimate its contribution.
- Baseline: a reference method used to judge whether a new method is effective.
```

- [ ] **Step 4: Verify English page paths**

Run:

```bash
test -f docs/source/en/orientation/index.md && test -f docs/source/en/rl_basics/index.md && test -f docs/source/en/world_models/index.md && test -f docs/source/en/embodied_ai/index.md && test -f docs/source/en/robot_learning/index.md && test -f docs/source/en/distributed_rl/index.md && test -f docs/source/en/research_practice/index.md
```

Expected: command exits with status `0`.

- [ ] **Step 5: Commit**

```bash
git add docs/source/en
git commit -m "docs: add english learning path pages"
```

## Task 6: Add Contributor and Reader Documentation

**Files:**
- Create: `README.md`
- Create: `CONTRIBUTING.md`

- [ ] **Step 1: Create README**

Create `README.md`:

````markdown
# Essentials of Embodied AI Research

This repository hosts a bilingual Read the Docs style learning resource for junior PhD students studying reinforcement learning, world models, embodied AI, robot learning practice, and distributed reinforcement learning systems.

## Documentation Structure

- `docs/source/index.md`: language selection page.
- `docs/source/zh_CN/`: Chinese documentation tree.
- `docs/source/en/`: English documentation tree.
- `docs/source/conf.py`: Sphinx configuration.

The Chinese and English trees should keep matching directory structures and page slugs.

## Local Build

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

Build the HTML documentation:

```bash
make -C docs html
```

Open `docs/build/html/index.html` in a browser.

## Learning Path

Start with Orientation and RL Basics, then move through World Models, Embodied AI Foundations, Robot Learning Practice, Distributed RL Systems, and Research Practice.

The RL Basics section links to [OpenAI Spinning Up](https://spinningup.openai.com/en/latest/) as an external reference for classical deep RL concepts and implementations.

## License

This project is released under the MIT License.
````

- [ ] **Step 2: Create CONTRIBUTING**

Create `CONTRIBUTING.md`:

````markdown
# Contributing

## Local Build

Install dependencies and build the documentation:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make -C docs html
```

Treat Sphinx warnings as issues to fix before submitting changes.

## Bilingual Structure

Every new page should be added to both language trees:

```text
docs/source/zh_CN/<section>/<page>.md
docs/source/en/<section>/<page>.md
```

Keep directory names and page slugs aligned. Chinese can be the primary writing language, but English pages should remain readable and should not be empty.

## Standard Page Template

Use this structure for major topic pages:

```markdown
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

Short overview pages may omit sections that do not apply.

## External Links and Citations

- Link to stable project pages, papers, or documentation whenever possible.
- Explain why a resource is useful instead of listing links without context.
- Do not copy substantial text from external resources.
- Keep OpenAI Spinning Up linked from RL Basics as a classical RL reference.

## Updating Reading Lists

When adding a paper or resource, prefer entries that are useful for a junior PhD student: clear problem statement, reusable method, strong baseline, benchmark value, or important negative lesson.
````

- [ ] **Step 3: Verify reader docs mention required topics**

Run:

```bash
rg -n "Spinning Up|zh_CN|en|make -C docs html" README.md CONTRIBUTING.md
```

Expected: output includes Spinning Up, bilingual paths, and local build command references.

- [ ] **Step 4: Commit**

```bash
git add README.md CONTRIBUTING.md
git commit -m "docs: add reader and contributor guides"
```

## Task 7: Build, Fix Warnings, and Verify Required Links

**Files:**
- Modify only files created in Tasks 1-6 if verification exposes broken links, invalid MyST syntax, or navigation mistakes.

- [ ] **Step 1: Install dependencies if needed**

Run:

```bash
python -m pip install -r requirements.txt
```

Expected: Sphinx, sphinx-rtd-theme, and myst-parser install successfully. If network access is blocked, rerun with escalated approval when working in Codex.

- [ ] **Step 2: Build docs with warnings as errors**

Run:

```bash
python -m sphinx -b html docs/source docs/build/html -W
```

Expected: build succeeds with no warnings.

- [ ] **Step 3: Verify root and language output files exist**

Run:

```bash
test -f docs/build/html/index.html && test -f docs/build/html/zh_CN/index.html && test -f docs/build/html/en/index.html
```

Expected: command exits with status `0`.

- [ ] **Step 4: Verify Spinning Up external link is present in both language pages**

Run:

```bash
rg -n "https://spinningup.openai.com/en/latest/" docs/source/zh_CN/rl_basics/index.md docs/source/en/rl_basics/index.md README.md CONTRIBUTING.md
```

Expected: output includes both RL Basics pages and supporting docs.

- [ ] **Step 5: Verify bilingual slug alignment**

Run:

```bash
find docs/source/zh_CN docs/source/en -path '*/index.md' | sort
```

Expected: matching section paths exist under `zh_CN` and `en`: `orientation`, `rl_basics`, `world_models`, `embodied_ai`, `robot_learning`, `distributed_rl`, and `research_practice`.

- [ ] **Step 6: Check git status**

Run:

```bash
git status --short
```

Expected: only intentional generated files are untracked or ignored. `.superpowers/` should be ignored after Task 1.

- [ ] **Step 7: Commit verification fixes**

If Step 2-6 required edits, commit them:

```bash
git add .gitignore .readthedocs.yaml requirements.txt README.md CONTRIBUTING.md docs
git commit -m "docs: verify bilingual sphinx site"
```

If no edits were required, do not create an empty commit.
