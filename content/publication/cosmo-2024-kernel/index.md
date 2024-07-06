---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Graph Kernel Neural Networks'
subtitle: ''
summary: ''
authors:
- cosmo
- Giorgia Minello
- Alessandro Bicciato
- Michael Bronstein
- rodola
- Luca Rossi
- Andrea Torsello
tags:
- 'Graph learning'
categories: []
date: '2024-05-01'
lastmod: 2023-02-05T10:57:53+01:00
featured: false
draft: false
publication_short: "TNNLS"

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
publishDate: '2023-02-05T09:57:52.951304Z'
publication_types:
- '2'
abstract: "The convolution operator at the core of many modern neural architectures can effectively be seen as performing a dot product between an input matrix and a filter. While this is readily applicable to data such as images, which can be represented as regular grids in the Euclidean space, extending the convolution operator to work on graphs proves more challenging, due to their irregular structure. In this article, we propose to use graph kernels, i.e., kernel functions that compute an inner product on graphs, to extend the standard convolution operator to the graph domain. This allows us to define an entirely structural model that does not require computing the embedding of the input graph. Our architecture allows to plug-in any type of graph kernels and has the added benefit of providing some interpretability in terms of the structural masks that are learned during the training process, similar to what happens for convolutional masks in traditional convolutional neural networks (CNNs). We perform an extensive ablation study to investigate the model hyperparameters’ impact and show that our model achieves competitive performance on standard graph classification and regression datasets."
publication: '*IEEE Transactions on Neural Networks and Learning Systems*'
links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://ieeexplore.ieee.org/document/10542111
- name: arXiv
  url: https://arxiv.org/abs/2112.07436
---
