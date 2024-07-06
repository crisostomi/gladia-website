---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Leveraging sparse and shared feature activations for disentangled representation learning
subtitle: ''
summary: ''
authors:
- fumero
- Florian Wenzel
- Luca Zancato
- Alessandro Achille
- rodola
- Stefano Soatto
- Bernhard Scholkopf
- Francesco Locatello

tags:
- representation learning
- disentanglement

categories: []
date: '2023-09-30'
lastmod: 2022-09-30T11:32:00+02:00
featured: false
draft: false
publication_short: "NeurIPS 2023"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
# image:
#   caption: ''
#   focal_point: 'Center'
#   preview_only: false

links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://openreview.net/forum?id=IHR83ufYPy
- name: PDF
  url: https://openreview.net/pdf?id=IHR83ufYPy
- icon: award
  icon_pack: fas
  name: 'NeurIPS 2023 spotlight'
  url: https://nips.cc/virtual/2023/poster/72132

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-04-28T10:30:59.888843Z'
publication_types:
- '1'
abstract: 'Recovering the latent factors of variation of high dimensional data has so far focused on simple synthetic settings. Mostly building on unsupervised and weakly-supervised objectives, prior work missed out on the positive implications for representation learning on real world data. In this work, we propose to leverage knowledge extracted from a diversified set of supervised tasks to learn a common disentangled representation. Assuming each supervised task only depends on an unknown subset of the factors of variation, we disentangle the feature space of a supervised multi-task model, with features activating sparsely across different tasks and information being shared as appropriate. Importantly, we never directly observe the factors of variations but establish that access to multiple tasks is sufficient for identifiability under sufficiency and minimality assumptions. We validate our approach on six real world distribution shift benchmarks, and different data modalities (images, text), demonstrating how disentangled representations can be transferred to real settings.'

publication: '*Conference on Neural Information Processing Systems (NeurIPS 2023)*'
---
