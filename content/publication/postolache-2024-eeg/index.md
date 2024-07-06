---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Naturalistic Music Decoding from EEG Data via Latent Diffusion Models'
subtitle: ''
summary: ''
authors:
- postolache
- Natalia Polouliakh
- Hiroaki Kitano
- Akima Connelly
- rodola
- cosmo
- Taketo Akama
tags: []
categories: []
date: '2024-07-02'
lastmod: 2023-10-02T:26:44
featured: false
draft: false
publication_short: "Preprint"

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
abstract: "In this article, we explore the potential of using latent diffusion models, a family of powerful generative models, for the task of reconstructing naturalistic music from electroencephalogram (EEG) recordings. Unlike simpler music with limited timbres, such as MIDI-generated tunes or monophonic pieces, the focus here is on intricate music featuring a diverse array of instruments, voices, and effects, rich in harmonics and timbre. This study represents an initial foray into achieving general music reconstruction of high-quality using non-invasive EEG data, employing an end-to-end training approach directly on raw data without the need for manual pre-processing and channel selection. We train our models on the public NMED-T dataset and perform quantitative evaluation proposing neural embedding-based metrics. We additionally perform song classification based on the generated tracks. Our work contributes to the ongoing research in neural decoding and brain-computer interfaces, offering insights into the feasibility of using EEG data for complex auditory information reconstruction."
publication: '*arXiv preprint*'
links:
- name: URL
  url : https://arxiv.org/abs/2405.09062
- name: PDF
  url: https://arxiv.org/pdf/2405.09062
---