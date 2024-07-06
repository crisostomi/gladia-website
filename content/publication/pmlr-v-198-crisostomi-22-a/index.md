---

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

tags:
    - graph representation learning
    - few-shot learning

categories: []
date: '2022-12-01'
lastmod: 2023-02-05T16:50:39+01:00
featured: false
draft: false

image:
  caption: ''
  focal_point: ''
  preview_only: false

projects: []
publishDate: '2023-02-05T15:50:38.894577Z'
publication_types:
- '1'

abstract: Few-shot graph classification is a novel yet promising emerging research field that still lacks the soundness of well-established research domains. Existing works often consider different benchmarks and evaluation settings, hindering comparison and, therefore, scientific progress. In this work, we start by providing an extensive overview of the possible approaches to solving the task, comparing the current state-of-the-art and baselines via a unified evaluation framework. Our findings show that while graph-tailored approaches have a clear edge on some distributions, easily adapted few-shot learning methods generally perform better.  In fact, we show that it is sufficient to equip a simple metric learning baseline with a state-of-the-art graph embedder to obtain the best overall results. We then show that straightforward additions at the latent level lead to substantial improvements by introducing i) a task-conditioned embedding space ii) a MixUp-based data augmentation technique. Finally, we release a highly reusable codebase to foster research in the field, offering modular and extensible implementations of all the relevant techniques.

publication: 'Proceedings of the First Learning on Graphs Conference'
publication_short: "LoG 2022"

links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://proceedings.mlr.press/v198/crisostomi22a.html
- name: PDF
  url: https://proceedings.mlr.press/v198/crisostomi22a/crisostomi22a.pdf
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/crisostomi/metric-few-shot-graph
---
