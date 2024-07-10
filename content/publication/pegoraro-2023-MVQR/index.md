---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Vector Quantile Regression on Manifolds'
subtitle: ''
summary: ''
authors:
- pegoraro
- Sanketh Vedula
- Aviv A. Rosenberg
- tallini
- rodola
- Alex M. Bronstein
tags:
- 'Machine Learning'
- 'Probability and Statistics'
categories: []
date: '2024-01-20'
lastmod: 2024-01-20T10:57:53+01:00
featured: false
draft: false
publication_short: "AISTATS 2024"

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
publishDate: '2024-01-20T09:57:52.951304Z'
abstract: Quantile regression (QR) is a statistical tool for distribution-free estimation of conditional quantiles of a target variable given explanatory features.
  QR is limited by the assumption that the target distribution is univariate and defined on an Euclidean domain.
  Although the notion of quantiles was recently extended to multi-variate distributions,
  QR for multi-variate distributions on manifolds remains underexplored, even though 
  many important applications inherently involve data distributed on, e.g., spheres (climate measurements), tori (dihedral angles in proteins), or Lie groups (attitude in navigation).
  By leveraging optimal transport theory and the notion of $c$-concave functions, we meaningfully define conditional vector quantile functions of high-dimensional variables on manifolds (M-CVQFs).
  Our approach allows for quantile estimation, regression, and computation of conditional confidence sets.
  We demonstrate the approach's efficacy and provide insights regarding the meaning of non-Euclidean quantiles through preliminary synthetic data experiments.
publication: '*AISTATS 2024*'
links:
- name: arXiv
  url: https://arxiv.org/abs/2307.01037
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/Marco-Peg/mvqr
---
