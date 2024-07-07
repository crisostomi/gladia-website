---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Learning shape correspondence with anisotropic convolutional neural networks
subtitle: ''
summary: ''
authors:
- Davide Boscaini
- Jonathan Masci
- rodola
- Michael M. Bronstein
tags: []
categories: []
date: '2016-12-01'
lastmod: 2023-02-02T06:55:14+01:00
featured: false
draft: false
publication_short: "NIPS 2016"

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
publishDate: '2023-02-02T05:55:13.906991Z'
publication_types:
- '1'
abstract: "Establishing correspondence between shapes is a fundamental problem in geometry processing, arising in a wide variety of applications. The problem is especially difficult in the setting of non-isometric deformations, as well as in the presence of topological noise and missing parts, mainly due to the limited capability to model such deformations axiomatically. Several recent works showed that invariance to complex shape transformations can be learned from examples. In this paper, we introduce an intrinsic convolutional neural network architecture based on anisotropic diffusion kernels, which we term Anisotropic Convolutional Neural Network (ACNN). In our construction, we generalize convolutions to non-Euclidean domains by constructing a set of oriented anisotropic diffusion kernels, creating in this way a local intrinsic polar representation of the data (patch), which is then correlated with a filter. Several cascades of such filters, linear, and non-linear operators are stacked to form a deep neural network whose parameters are learned by minimizing a task-specific cost. We use ACNNs to effectively learn intrinsic dense correspondences between deformable shapes in very challenging settings, achieving state-of-the-art results on some of the most difficult recent correspondence benchmarks."
publication: '*Proc. Neural Information Processing Systems (NIPS)*'

links:
- name: 'PDF'
  url: https://papers.nips.cc/paper_files/paper/2016/file/228499b55310264a8ea0e27b6e7c6ab6-Paper.pdf
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://papers.nips.cc/paper_files/paper/2016/hash/228499b55310264a8ea0e27b6e7c6ab6-Abstract.html
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/davideboscaini/acnn
---
