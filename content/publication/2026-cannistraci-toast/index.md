---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'TOAST: Transformer Optimization using Adaptive and Simple Transformations'
subtitle: ''
summary: ''
authors:
- cannistraci
- Simone Antonelli
- Emanuele Palumbo
- Thomas M. Sutter
- rodola
- Bastian Rieck
- Julia E. Vogt
tags: []
categories: []
date: '2026-04-11'
lastmod: 2024-10-31T:26:44
featured: false
draft: false
publication_short: "TMLR"

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
- '2'
abstract: "Foundation models achieve state-of-the-art performance across different tasks, but their size and computational demands raise concerns about accessibility and sustainability. Existing efficiency methods often require additional retraining or finetuning, limiting their practicality. Recent findings suggest that deep neural networks exhibit internal representation similarities. While such similarities across different models have been exploited for enabling techniques such as model stitching and merging, intra-network redundancy remains underexplored as a source for efficiency gains. In this paper, we introduce Transformer Optimization using Adaptive and Simple Transformations (TOAST), a framework that exploits these redundancies to approximate entire transformer blocks with lightweight closed-form mappings, such as linear transformations or even the identity function, without any additional training. Across state-of-the-art pretrained vision models (e.g., ViT, DINOv2, DeiT) and datasets ranging from MNIST to ImageNet-1k, TOAST reduces parameters and computation while preserving, and in some cases improving, downstream performance. These results show that large portions of transformer depth can be replaced by trivial functions, opening a new perspective on efficient foundation models."
publication: '*Transactions on Machine Learning Research*'
links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://openreview.net/forum?id=fSwMCsBtTG
- name: PDF
  url: https://openreview.net/pdf?id=fSwMCsBtTG
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/icannistraci/toast
---