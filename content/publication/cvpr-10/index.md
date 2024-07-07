---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'A game-theoretic approach to fine surface registration without initial motion estimation'
subtitle: ''
summary: ''
authors:
- Andrea Albarelli
- rodola
- Andrea Torsello
tags: []
categories: []
date: '2010-06-01'
lastmod: 2023-02-02T06:55:36+01:00
featured: false
draft: false
publication_short: "CVPR 2010"

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
publishDate: '2023-02-02T05:55:36.160993Z'
publication_types:
- '1'
abstract: "Surface registration is a fundamental step in the reconstruction of three-dimensional objects. This is typically a two step process where an initial coarse motion estimation is followed by a refinement. Most coarse registration algorithms exploit some local point descriptor that is intrinsic to the shape and does not depend on the relative position of the surfaces. By contrast, refinement techniques iteratively minimize a distance function measured between pairs of selected neighboring points and are thus strongly dependent on initial alignment. In this paper we propose a novel technique that allows to obtain a fine surface registration in a single step, without the need of an initial motion estimation. The main idea of our approach is to cast the selection of correspondences between points on the surfaces in a game-theoretic framework, where a natural selection process allows mating points that satisfy a mutual rigidity constraint to thrive, eliminating all the other correspondences. This process yields a very robust inlier selection scheme that does not depend on any particular technique for selecting the initial strategies as it relies only on the global geometric compatibility between correspondences. The practical effectiveness of the proposed approach is confirmed by an extensive set of experiments and comparisons with state-of-the-art techniques."
publication: "*Proc. Int'l Conference on Computer Vision and Pattern Recognition (CVPR)*"

links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://ieeexplore.ieee.org/document/5540183
- name: 'PDF'
  url: https://www.dsi.unive.it/~atorsell/papers/Conferences/cvpr2010.pdf
---
