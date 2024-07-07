---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Consistent Partial Matching of Shape Collections via Sparse Modeling
subtitle: ''
summary: ''
authors:
- cosmo
- rodola
- Andrea Albarelli
- Facundo Mémoli
- Daniel Cremers
tags: []
categories: []
date: '2017-01-01'
lastmod: 2023-02-08T19:53:27+01:00
featured: false
draft: false
publication_short: "CGF"

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
publishDate: '2023-02-08T18:53:26.615208Z'
publication_types:
- '2'
abstract: Recent efforts in the area of joint object matching approach the problem
  by taking as input a set of pairwise maps, which are then jointly optimized across
  the whole collection so that certain accuracy and consistency criteria are satisfied.
  One natural requirement is cycle-consistency—namely the fact that map composition
  should give the same result regardless of the path taken in the shape collection.
  In this paper, we introduce a novel approach to obtain consistent matches without
  requiring initial pairwise solutions to be given as input. We do so by optimizing
  a joint measure of metric distortion directly over the space of cycle-consistent
  maps; in order to allow for partially similar and extra-class shapes, we formulate
  the problem as a series of quadratic programs with sparsity-inducing constraints,
  making our technique a natural candidate for analysing collections with a large
  presence of outliers. The particular form of the problem allows us to leverage results
  and tools from the field of evolutionary game theory. This enables a highly efficient
  optimization procedure which assures accurate and provably consistent solutions
  in a matter of minutes in collections with hundreds of shapes.
publication: '*Computer Graphics Forum*'
links:
- name: PDF
  url: https://www.dsi.unive.it/~cosmo/content/SCOPUS_ID:84957991700.pdf
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.12796
---
