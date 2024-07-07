---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Unsupervised source separation via Bayesian inference in the latent domain
subtitle: ''
summary: ''
authors:
- mancusi
- postolache
- mariani
- fumero
- santilli
- cosmo
- rodola
tags:
- Signal Processing
- Source Separation
categories: []
date: '2021-01-01'
lastmod: 2023-02-05T10:57:35+01:00
featured: false
draft: false
publication_short: "Preprint"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-05T09:57:34.078006Z'
publication_types:
- '2'
abstract: State of the art audio source separation models rely on supervised data-driven
  approaches, which can be expensive in terms of labeling resources. On the other
  hand, approaches for training these models without any direct supervision are typically
  high-demanding in terms of memory and time requirements, and remain impractical
  to be used at inference time. We aim to tackle these limitations by proposing a
  simple yet effective unsupervised separation algorithm, which operates directly
  on a latent representation of time-domain signals. Our algorithm relies on deep
  Bayesian priors in the form of pre-trained autoregressive networks to model the
  probability distributions of each source. We leverage the low cardinality of the
  discrete latent space, trained with a novel loss term imposing a precise arithmetic
  structure on it, to perform exact Bayesian inference without relying on an approximation
  strategy. We validate our approach on the Slakh dataset arXiv:1909.08494, demonstrating
  results in line with state of the art supervised approaches while requiring fewer
  resources with respect to other unsupervised methods.
publication: '*arXiv preprint arXiv:2110.05313*'
links:
- name: 'arXiv'
  url: https://arxiv.org/abs/2110.05313
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/michelemancusi/LQVAE-separation
---
