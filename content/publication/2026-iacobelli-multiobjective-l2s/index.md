---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Multi-objective Evolutionary Merging Enables Efficient Reasoning Models'
subtitle: ''
summary: ''
authors:
- iacobelli
- minut
- mencattini
- crisostomi
- santilli
- Iacopo Masi
- rodola

tags: []
categories: []
date: '2026-04-07'
lastmod: 2026-04-07T:26:44
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
publishDate: '2026-04-07T:00:00'
publication_types:
- '3'
abstract: "Reasoning models have demonstrated remarkable capabilities in solving complex problems by leveraging long chains of thought. However, this more deliberate reasoning comes with substantial computational overhead at inference time. The Long-to-Short (L2S) reasoning problem seeks to maintain high accuracy using fewer tokens, but current training-free model merging approaches rely on scalarized, fixed-hyperparameter arithmetic methods that are highly brittle and force suboptimal compromises. To address this gap, we introduce Evo-L2S, a novel framework that formulates L2S reasoning as a multi-objective optimization challenge. By leveraging evolutionary model merging, Evo-L2S explicitly optimizes the trade-off between accuracy and output length to produce a robust Pareto front of merged models. To make this search computationally tractable for large language models, we propose an entropy-based subset sampling technique that drastically reduces the overhead of fitness estimation. Comprehensive experiments across 1.5B, 7B, and 14B parameter scales on six mathematical reasoning benchmarks demonstrate that Evo-L2S can reduce the length of generated reasoning traces by over 50% while preserving, or even improving, the problem-solving accuracy of the original reasoning models."
publication: '*ArXiv preprint*'
links:
- name: arXiv
  url : https://arxiv.org/abs/2604.06465
---