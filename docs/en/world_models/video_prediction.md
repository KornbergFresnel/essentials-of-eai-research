# Video Prediction

Video prediction — forecasting future visual frames from past observations — is a core capability for world models. Accurate video prediction enables planning, anomaly detection, and understanding of physical dynamics.

## Problem Formulation

Given a sequence of past frames (and optionally actions), predict future frames:

$$
\hat{o}_{t+1:t+H} = f_\theta(o_{1:t}, a_{1:t+H-1})
$$

**Action-conditioned**: predicting outcomes of specific actions (for control)
**Action-free**: predicting general future evolution (for understanding)

## Deterministic Models

### Convolutional Sequence Models

Early approaches used convolutional encoder-decoder networks with recurrent dynamics:

- **ConvLSTM** (Shi et al., 2015): Convolutional LSTM for spatiotemporal prediction
- **PredNet** (Lotter et al., 2017): Predictive coding architecture inspired by neuroscience
- **SVG** (Denton & Biber, 2018): Stochastic video generation with learned prior

### Limitations

- **Blurry predictions**: MSE loss + deterministic model → average over possible futures
- **Short horizon**: Quality degrades rapidly beyond a few frames
- **Mode collapse**: Cannot represent multiple possible futures

## Stochastic Models

### VAE-Based

**SV2P** (Babaeizadeh et al., 2018): Stochastic Variational Video Prediction — adds latent random variables per timestep to capture uncertainty:

$$
z_t \sim q(z_t | o_{1:t+1}), \quad \hat{o}_{t+1} = \text{dec}(h_t, z_t)
$$

**FitVid** (Babaeizadeh et al., 2021): Scales up stochastic video prediction with architectural improvements for longer, higher-quality predictions.

### GAN-Based

**DVD-GAN** (Clark et al., 2019): Uses adversarial training for sharper video generation. Discriminator operates on spatial and temporal dimensions separately.

**Pros**: Sharper predictions than VAE models
**Cons**: Training instability, mode dropping

## Transformer-Based Models

Transformers have become dominant in video prediction due to their ability to model long-range dependencies.

### Video GPT and Tokenization

**VideoGPT** (Yan et al., 2021): Tokenizes video frames using VQ-VAE, then models token sequences autoregressively with a GPT-like Transformer.

Pipeline:

1. Encode frames to discrete tokens via VQ-VAE
2. Model the token sequence with a causal Transformer
3. Autoregressively sample future tokens
4. Decode tokens back to frames

### IRIS

**IRIS** (Micheli et al., 2023): An RL agent that uses a Transformer-based world model with discrete tokens.

1. Observations → discrete tokens via VQ-VAE
2. Dynamics modeled as autoregressive next-token prediction over (observation tokens, action tokens, reward tokens)
3. Imagination-based policy training

This bridges video prediction and RL directly.

## Diffusion-Based Models

Diffusion models have recently achieved state-of-the-art in video prediction, producing high-quality, diverse samples.

### How Diffusion Applies to Video

Standard diffusion: learn to denoise $x_t = \sqrt{\alpha_t} x_0 + \sqrt{1-\alpha_t} \epsilon$ back to $x_0$.

For video prediction, $x_0$ is a future frame (or sequence of frames), conditioned on past frames:

$$
p_\theta(o_{t+1:t+H} | o_{1:t}) = \int p_\theta(o_{t+1:t+H}^{(0)} | o_{t+1:t+H}^{(T)}) \, p(o_{t+1:t+H}^{(T)}) \, d o^{(T)}
$$

### Key Models

- **MCVD** (Voleti et al., 2022): Masked Conditional Video Diffusion
- **RVD** (Yang et al., 2023): Scalable video diffusion with recurrent conditioning
- **Sora**: Video generation model from OpenAI based on diffusion transformers (DiT)

### Advantages of Diffusion for Video

- **High quality**: Sharp, detailed predictions
- **Diversity**: Naturally generates diverse futures
- **Controllability**: Can condition on text, actions, layout, etc.
- **Scalability**: DiT architecture scales well with compute

## Action-Conditioned Video Prediction

For control and robotics, we need **action-conditioned** video prediction:

$$
\hat{o}_{t+1} = f_\theta(o_{1:t}, a_t)
$$

Key works:

- **Action-Conditioned Video Prediction** (Oh et al., 2015): Early work on predicting Atari frames conditioned on actions
- **UniPi** (Du et al., 2023): Uses video diffusion as a universal policy interface — plan by generating future video, then extract actions
- **SuSIE** (Black et al., 2023): Uses video prediction for subgoal generation in robot manipulation

## Evaluation Metrics

| Metric | What It Measures | Notes |
|--------|-----------------|-------|
| **MSE / PSNR** | Pixel-level accuracy | Penalizes blurriness less than perceptual methods |
| **SSIM** | Structural similarity | Better than MSE but still pixel-level |
| **LPIPS** | Perceptual similarity | Uses deep features, correlates with human judgment |
| **FVD** | Fréchet Video Distance | Distribution-level metric, the video equivalent of FID |
| **FID per frame** | Per-frame distribution quality | Useful for long-horizon evaluation |

!!! warning "Metric Limitations"
    Pixel-level metrics (MSE, SSIM) can be misleading for stochastic environments — a blurry average over possible futures may score well on MSE but be useless for planning. FVD and LPIPS are generally more informative.

## Connection to World Models

Video prediction models become world models when combined with:

1. **Action conditioning**: predict consequences of actions
2. **Reward prediction**: estimate rewards from predicted futures
3. **Planning algorithms**: use predictions for decision-making

The trend is moving from pure video prediction toward integrated world models that jointly handle perception, prediction, and control.

## Key References

- Shi, X., et al. (2015). "Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting." *NeurIPS*.
- Babaeizadeh, M., et al. (2018). "Stochastic Variational Video Prediction." *ICLR*.
- Yan, W., et al. (2021). "VideoGPT: Video Generation using VQ-VAE and Transformers." *arXiv*.
- Micheli, V., Alonso, E., Fleuret, F. (2023). "Transformers are Sample-Efficient World Learners." *ICLR*.
- Du, Y., et al. (2023). "Learning Universal Policies via Text-Guided Video Generation." *NeurIPS*.
