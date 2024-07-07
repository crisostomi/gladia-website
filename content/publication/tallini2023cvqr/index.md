---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Continuous Vector Quantile Regression'
subtitle: ''
summary: ''
authors:
- Sanketh Vedula
- tallini
- Aviv A. Rosenberg
- pegoraro
- rodola
- Yaniv Romano
- Alexander Bronstein
tags: []
categories: []
date: '28-07-2023'
lastmod: 
featured: false
draft: false
publication_short: "ICML 2023 Workshop Frontiers4LCD"

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
publishDate: '2023-07-28T15:50:39.853135Z'
publication_types:
- '3'
abstract: Vector quantile regression (VQR) estimates the conditional vector quantile function (CVQF), a fundamental quantity which fully represents the conditional distribution of Y|X. VQR is formulated as an optimal transport (OT) problem between a uniform r.v. U and the target r.v. Y|X , the solution of which is a unique transport map, co-monotonic with U. Recently NL-VQR has been proposed to estimate support non-linear CVQFs, together with fast solvers which enabled the use of this tool in practical applications. Despite its utility, the scalability and estimation quality of NL-VQR is limited due to a discretization of the OT problem onto a grid of quantile levels. We propose a novel continuous formulation and parametrization of VQR using partial input-convex neural networks (PICNNs). Our approach allows for accurate, scalable, differentiable and invertible estimation of non-linear CVQFs. We further demonstrate, theoretically and experimentally, how continuous CVQFs can be used for general statistical inference tasks such as estimation of likelihoods, CDFs, confidence sets, coverage, sampling, and more. This work is an important step towards unlocking the full potential of VQR.
publication: '*ICML 2023 Workshop on New Frontiers in Learning, Control, and Dynamical Systems*'
links:
- name: 'PDF'
  url: https://openreview.net/pdf?id=DUZbGAXcyL
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://openreview.net/forum?id=DUZbGAXcyL
---
