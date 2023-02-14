---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Metric Based Few-Shot Graph Classification
subtitle: ''
summary: ''
authors:
- crisostomi
- Simone Antonelli
- maiorca
- moschella
- marin
- rodola
tags: []
categories: []
date: '2022-12-01'
lastmod: 2023-02-05T16:50:39+01:00
featured: false
draft: false
publication_short: "LoG 2022"

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
publishDate: '2023-02-05T15:50:38.894577Z'
publication_types:
- '1'
abstract: Few-shot graph classification is a novel yet promising emerging research
  field that still lacks the soundness of well-established research domains. Existing
  works often consider different benchmarks and evaluation settings, hindering comparison
  and, therefore, scientific progress. In this work, we start by providing an extensive
  overview of the possible approaches to solving the task, comparing the current state-of-the-art
  and baselines via a unified evaluation framework. Our findings show that while graph-tailored
  approaches have a clear edge on some distributions, easily adapted few-shot learning
  methods generally perform better.  In fact, we show that it is sufficient to equip
  a simple metric learning baseline with a state-of-the-art graph embedder to obtain
  the best overall results. We then show that straightforward additions at the latent
  level lead to substantial improvements by introducing i) a task-conditioned embedding
  space ii) a MixUp-based data augmentation technique. Finally, we release a highly
  reusable codebase to foster research in the field, offering modular and extensible
  implementations of all the relevant techniques.
publication: '*Proceedings of the First Learning on Graphs Conference*'
links:
- name: URL
  url: https://proceedings.mlr.press/v198/crisostomi22a.html
---
