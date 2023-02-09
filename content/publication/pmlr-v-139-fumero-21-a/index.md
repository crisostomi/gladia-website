---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Learning disentangled representations via product manifold projection
subtitle: ''
summary: ''
authors:
- fumero
- cosmo
- melzi
- rodola
tags: []
categories: []
date: '2021-07-01'
lastmod: 2023-02-08T15:00:22+01:00
featured: false
draft: false

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
publishDate: '2023-02-08T14:02:06.250215Z'
publication_types:
- '1'
abstract: We propose a novel approach to disentangle the generative factors of variation
  underlying a given set of observations. Our method builds upon the idea that the
  (unknown) low-dimensional manifold underlying the data space can be explicitly modeled
  as a product of submanifolds. This definition of disentanglement gives rise to a
  novel weakly-supervised algorithm for recovering the unknown explanatory factors
  behind the data. At training time, our algorithm only requires pairs of non i.i.d.
  data samples whose elements share at least one, possibly multidimensional, generative
  factor of variation. We require no knowledge on the nature of these transformations,
  and do not make any limiting assumption on the properties of each subspace. Our
  approach is easy to implement, and can be successfully applied to different kinds
  of data (from images to 3D surfaces) undergoing arbitrary transformations. In addition
  to standard synthetic benchmarks, we showcase our method in challenging real-world
  applications, where we compare favorably with the state of the art.
publication: '*Proceedings of the 38th International Conference on Machine Learning*'
links:
- name: URL
  url: https://proceedings.mlr.press/v139/fumero21a.html
---
