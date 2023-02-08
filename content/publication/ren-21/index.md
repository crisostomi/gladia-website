---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Discrete Optimization for Shape Matching
subtitle: ''
summary: ''
authors:
- Jing Ren
- Simone Melzi
- Peter Wonka
- Maks Ovsjanikov
tags:
- CCS Concepts
- • Computing methodologies → Shape analysis
- • Theory of computation → Computational geometry
categories: []
date: '2021-01-01'
lastmod: 2023-02-08T15:02:28+01:00
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
publishDate: '2023-02-08T14:02:27.682276Z'
publication_types:
- '2'
abstract: Abstract We propose a novel discrete solver for optimizing functional map-based
  energies, including descriptor preservation and promoting structural properties
  such as area-preservation, bijectivity and Laplacian commutativity among others.
  Unlike the commonly-used continuous optimization methods, our approach enforces
  the functional map to be associated with a pointwise correspondence as a hard constraint,
  which provides a stronger link between optimized properties of functional and point-to-point
  maps. Under this hard constraint, our solver obtains functional maps with lower
  energy values compared to the standard continuous strategies. Perhaps more importantly,
  the recovered pointwise maps from our discrete solver preserve the optimized for
  functional properties and are thus of higher overall quality. We demonstrate the
  advantages of our discrete solver on a range of energies and shape categories, compared
  to existing techniques for promoting pointwise maps within the functional map framework.
  Finally, with this solver in hand, we introduce a novel Effective Functional Map
  Refinement (EFMR) method which achieves the state-of-the-art accuracy on the SHREC'19
  benchmark.
publication: '*Computer Graphics Forum*'
doi: https://doi.org/10.1111/cgf.14359
links:
- name: URL
  url: https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14359
---
