---
# Documentation: https://wowchemy.com/docs/managing-content/

title: A Game-theoretical Approach for Joint Matching of Multiple Feature throughout
  Unordered Images
subtitle: ''
summary: ''
authors:
- cosmo
- Andrea Albarelli
- Filippo Bergamasco
- Andrea Torsello
- rodola
- Daniel Cremers
tags: []
categories: []
date: '2016-12-01'
lastmod: 2023-02-02T06:55:17+01:00
featured: false
draft: false
publication_short: ""

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
publishDate: '2023-02-02T05:55:17.064539Z'
publication_types:
- '1'
abstract: 'Feature matching is a key step in most Computer Vision tasks involving several views of the same subject. In fact, it plays a crucial role for a successful reconstruction of 3D information of the corresponding material points. Typical approaches to construct stable feature tracks throughout a sequence of images operate via a two-step process: First, feature matches are extracted among all pairs of points of view; these matches are then given in input to a regularizer that provides a final, globally consistent solution. In this paper, we formulate this matching problem as a simultaneous optimization over the entire image collection, without requiring previously computed pairwise matches to be given as input. As our formulation operates directly in the space of feature across multiple images, the final matches are consistent by construction. Our matching problem has a natural interpretation as a non-cooperative game, which allows us to leverage tools and results from Game Theory. We performed a specially crafted set of experiments demonstrating that our approach compares favorably with the state of the art, while retaining a high computational efficiency.'
publication: "*Proc. Int'l Conference on Pattern Recognition (ICPR)*"
---
links:
- name: 'PDF'
  url: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7900212

