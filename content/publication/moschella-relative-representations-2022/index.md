---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Relative representations enable zero-shot latent space communication
subtitle: ''
summary: ''
authors:
- moschella
- maiorca
- fumero
- norelli
- Francesco Locatello
- rodola

tags:
- '"Computer Science - Machine Learning"'
- 'featured'

categories: []
date: '2022-09-30'
lastmod: 2022-09-30T11:32:00+02:00
featured: false
draft: false
publication_short: "ICLR 2023"

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
  url: https://openreview.net/forum?id=SrC-nwieGJ
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/lucmos/relreps
- icon: chalkboard-user
  icon_pack: fas
  name: 'Slides'
  url: https://lucmos.github.io/relreps-presentation/
- icon: award
  icon_pack: fas
  name: 'ICLR 2023 notable top 5%'
  url: https://iclr.cc/virtual/2023/poster/11612

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-04-28T10:30:59.888843Z'
publication_types:
- '1'
abstract: 'Neural networks embed the geometric structure of a data manifold lying in a high-dimensional space into latent representations. Ideally, the distribution of the data points in the latent space should depend only on the task, the data, the loss, and other architecture-specific constraints. However, factors such as the random weights initialization, training hyperparameters, or other sources of randomness in the training phase may induce incoherent latent spaces that hinder any form of reuse. Nevertheless, we empirically observe that, under the same data and modeling choices, distinct latent spaces typically differ by an unknown quasi-isometric transformation: that is, in each space, the distances between the encodings do not change. In this work, we propose to adopt pairwise similarities as an alternative data representation, that can be used to enforce the desired invariance without any additional training. We show how neural architectures can leverage these relative representations to guarantee, in practice, latent isometry invariance, effectively enabling latent space communication: from zero-shot model stitching to latent space comparison between diverse settings. We extensively validate the generalization capability of our approach on different datasets, spanning various modalities (images, text, graphs), tasks (e.g., classification, reconstruction) and architectures (e.g., CNNs, GCNs, transformers).'

publication: '*International Conference on Learning Representations (ICLR 2023)*'
---
