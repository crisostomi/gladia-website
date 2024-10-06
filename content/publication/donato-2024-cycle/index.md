---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'C2M3: Cycle-Consistent Multi-Model Merging'
subtitle: ''
summary: ''
authors:
- crisostomi
- fumero
- baieri
- Florian Bernard
- rodola
tags: []
categories: []
date: '2024-09-25'
lastmod: 2023-10-02T:26:44
featured: false
draft: false
publication_short: "NeurIPS 2024"

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
abstract: "In this paper, we present a novel data-free method for merging neural networks in weight space. Differently from most existing works, our method optimizes for the permutations of network neurons globally across all layers. This allows us to enforce cycle consistency of the permutations when merging N >= 3 models, allowing circular compositions of permutations to be computed without accumulating error along the path. We qualitatively and quantitatively motivate the need for such a constraint, showing its benefits when merging sets of models in scenarios spanning varying architectures and datasets. We finally show that, when coupled with activation renormalization, our approach yields the best results in the task."

links:
- name: arXiv
  url : https://arxiv.org/abs/2405.17897
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/crisostomi/cycle-consistent-model-merging

publication: '*Thirty-eighth Conference on Neural Information Processing Systems (NeurIPS 2024)*'
---