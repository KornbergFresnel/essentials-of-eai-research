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
