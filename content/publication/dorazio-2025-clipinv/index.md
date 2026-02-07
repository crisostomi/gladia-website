---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Implicit Inversion turns CLIP into a Decoder"
subtitle: ''
summary: ''
authors:
- Antonio D'Orazio
- Maria Rosaria Briglia
- crisostomi
- Dario Loi
- rodola
- Iacopo Masi
tags: []
categories: []
date: '2025-05-29'
lastmod: 2024-10-11T:26:44
featured: false
draft: false
publication_short: "ICLR 2026"

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
- '3'
abstract: "CLIP is a discriminative model trained to align images and text in a shared embedding space. Due to its multimodal structure, it serves as the backbone of many generative pipelines, where a decoder is trained to map from the shared space back to images. In this work, we show that image synthesis is nevertheless possible using CLIP alone -- without any decoder, training, or fine-tuning. Our approach optimizes a frequency-aware implicit neural representation that encourages coarse-to-fine generation by stratifying frequencies across network layers. To stabilize this inverse mapping, we introduce adversarially robust initialization, a lightweight Orthogonal Procrustes projection to align local text and image embeddings, and a blending loss that anchors outputs to natural image statistics. Without altering CLIP's weights, this framework unlocks capabilities such as text-to-image generation, style transfer, and image reconstruction. These findings suggest that discriminative models may hold untapped generative potential, hidden in plain sight."
publication: '*ICLR 2026*'
links:
- name: 'arXiv'
  url : https://arxiv.org/abs/2505.23161
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/OmnAI-Lab/implicit-inversion
---