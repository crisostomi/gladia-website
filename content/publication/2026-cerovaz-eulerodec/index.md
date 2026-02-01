---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'EuleroDec: A Complex-Valued RVQ-VAE for Efficient and Robust Audio Coding'
subtitle: ''
summary: ''
authors:
- cerovaz
- mancusi
- rodola
tags: []
categories: []
date: '2026-1-17'
lastmod: 2023-10-02T:26:44
featured: false
draft: false
publication_short: "ICASSP 2026"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-10-02T:26:44'
publication_types:
- '1'
abstract: "Audio codecs power discrete music generative modelling, music streaming and immersive media by shrinking PCM audio to bandwidth-friendly bit-rates. Recent works have gravitated towards processing in the spectral domain; however, spectrogram-domains typically struggle with phase modeling which is naturally complex-valued. Most frequency-domain neural codecs either disregard phase information or encode it as two separate real-valued channels, limiting spatial fidelity. This entails the need to introduce adversarial discriminators at the expense of convergence speed and training stability to compensate for the inadequate representation power of the audio signal. In this work we introduce an end-to-end complex-valued RVQ-VAE audio codec that preserves magnitude-phase coupling across the entire analysis-quantization-synthesis pipeline and removes adversarial discriminators and diffusion post-filters. Without GANs or diffusion we match or surpass much longer-trained baselines in-domain and reach SOTA out-of-domain performance. Compared to standard baselines that train for hundreds of thousands of steps, our model reducing training budget by an order of magnitude is markedly more compute-efficient while preserving high perceptual quality."
publication: '*Proc. ICASSP*'
links:
- name: arXiv
  url : https://www.arxiv.org/abs/2601.17517
---