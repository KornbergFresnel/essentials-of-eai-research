# 视频预测

视频预测——根据过去的观测预测未来的视觉帧——是世界模型的核心能力之一。准确的视频预测能够支撑规划、异常检测以及对物理动力学的理解。

## 问题定义

给定过去的帧序列（以及可选的动作），预测未来的帧：

$$
\hat{o}_{t+1:t+H} = f_\theta(o_{1:t}, a_{1:t+H-1})
$$

**有动作条件**：预测特定动作的结果（用于控制）

**无动作条件**：预测一般性的未来演化（用于理解）

## 确定性模型

### 卷积序列模型

早期方法使用卷积编码器-解码器网络结合循环动力学：

- **ConvLSTM**（Shi et al., 2015）：用于时空预测的卷积 LSTM
- **PredNet**（Lotter et al., 2017）：受神经科学启发的预测编码架构
- **SVG**（Denton & Biber, 2018）：带学习先验的随机视频生成

### 局限性

- **模糊预测**：MSE 损失 + 确定性模型 → 对所有可能未来的平均
- **短预测时域**：质量在超过几帧后迅速退化
- **模式坍塌**：无法表示多种可能的未来

## 随机性模型

### 基于 VAE 的模型

**SV2P**（Babaeizadeh et al., 2018）：随机变分视频预测——在每个时间步添加潜在随机变量以捕捉不确定性：

$$
z_t \sim q(z_t | o_{1:t+1}), \quad \hat{o}_{t+1} = \text{dec}(h_t, z_t)
$$

**FitVid**（Babaeizadeh et al., 2021）：通过架构改进扩展随机视频预测的规模，实现更长时域、更高质量的预测。

### 基于 GAN 的模型

**DVD-GAN**（Clark et al., 2019）：使用对抗训练生成更清晰的视频。判别器分别在空间和时间维度上进行操作。

**优点**：比 VAE 模型预测更清晰

**缺点**：训练不稳定，可能出现模式丢失

## 基于 Transformer 的模型

Transformer 凭借其建模长距离依赖的能力，已成为视频预测领域的主导架构。

### VideoGPT 与标记化

**VideoGPT**（Yan et al., 2021）：先用 VQ-VAE 将视频帧转化为离散 token，然后用类 GPT 的 Transformer 对 token 序列进行自回归建模。

处理流程：

1. 通过 VQ-VAE 将帧编码为离散 token
2. 用因果 Transformer 对 token 序列建模
3. 自回归地采样未来 token
4. 将 token 解码回视频帧

### IRIS

**IRIS**（Micheli et al., 2023）：一个使用基于 Transformer 的世界模型和离散 token 的 RL 智能体。

1. 观测 → 通过 VQ-VAE 转化为离散 token
2. 动力学建模为对（观测 token、动作 token、奖励 token）序列的自回归下一 token 预测
3. 基于想象力的策略训练

这直接架起了视频预测与 RL 之间的桥梁。

## 基于扩散模型的方法

扩散模型近年来在视频预测领域取得了最先进的成果，能够生成高质量、多样化的样本。

### 扩散模型如何应用于视频

标准扩散过程：学习将 $x_t = \sqrt{\alpha_t} x_0 + \sqrt{1-\alpha_t} \epsilon$ 去噪回 $x_0$。

对于视频预测，$x_0$ 是未来帧（或帧序列），以过去的帧为条件：

$$
p_\theta(o_{t+1:t+H} | o_{1:t}) = \int p_\theta(o_{t+1:t+H}^{(0)} | o_{t+1:t+H}^{(T)}) \, p(o_{t+1:t+H}^{(T)}) \, d o^{(T)}
$$

### 代表性模型

- **MCVD**（Voleti et al., 2022）：遮蔽条件视频扩散
- **RVD**（Yang et al., 2023）：基于循环条件的可扩展视频扩散
- **Sora**：OpenAI 基于扩散 Transformer（DiT）的视频生成模型

### 扩散模型用于视频的优势

- **高质量**：清晰、细节丰富的预测
- **多样性**：天然生成多样化的未来
- **可控性**：可以文本、动作、布局等为条件
- **可扩展性**：DiT 架构随计算资源的增加而有效扩展

## 动作条件视频预测

在控制和机器人领域，我们需要**以动作为条件**的视频预测：

$$
\hat{o}_{t+1} = f_\theta(o_{1:t}, a_t)
$$

代表性工作：

- **Action-Conditioned Video Prediction**（Oh et al., 2015）：以动作为条件预测 Atari 帧的早期工作
- **UniPi**（Du et al., 2023）：将视频扩散模型作为通用策略接口——通过生成未来视频进行规划，然后提取动作
- **SuSIE**（Black et al., 2023）：利用视频预测进行机器人操作中的子目标生成

## 评估指标

| 指标 | 衡量内容 | 备注 |
|------|---------|------|
| **MSE / PSNR** | 像素级精度 | 对模糊的惩罚不如感知方法严格 |
| **SSIM** | 结构相似性 | 优于 MSE 但仍在像素级别 |
| **LPIPS** | 感知相似性 | 使用深度特征，与人类判断相关性更高 |
| **FVD** | Frechet 视频距离 | 分布级别的指标，视频版的 FID |
| **FID（逐帧）** | 逐帧的分布质量 | 适用于长时域评估 |

!!! warning "指标的局限性"
    在随机环境下，像素级指标（MSE、SSIM）可能具有误导性——对所有可能未来的模糊平均在 MSE 上可能得分不错，但对规划毫无用处。FVD 和 LPIPS 通常更具参考价值。

## 与世界模型的联系

视频预测模型在结合以下要素后即成为世界模型：

1. **动作条件**：预测动作的后果
2. **奖励预测**：从预测的未来中估计奖励
3. **规划算法**：利用预测进行决策

当前的趋势是从纯粹的视频预测走向集成式世界模型——统一处理感知、预测和控制。

## 核心参考文献

- Shi, X., et al. (2015). "Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting." *NeurIPS*.
- Babaeizadeh, M., et al. (2018). "Stochastic Variational Video Prediction." *ICLR*.
- Yan, W., et al. (2021). "VideoGPT: Video Generation using VQ-VAE and Transformers." *arXiv*.
- Micheli, V., Alonso, E., Fleuret, F. (2023). "Transformers are Sample-Efficient World Learners." *ICLR*.
- Du, Y., et al. (2023). "Learning Universal Policies via Text-Guided Video Generation." *NeurIPS*.
