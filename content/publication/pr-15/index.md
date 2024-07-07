---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Fast and Accurate Surface Alignment Through an Isometry-Enforcing Game
subtitle: ''
summary: ''
authors:
- Andrea Albarelli
- rodola
- Andrea Torsello
tags: []
categories: []
date: '2015-07-01'
lastmod: 2023-02-02T06:54:58+01:00
featured: false
draft: false
publication_short: "PR"

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
publishDate: '2023-02-02T05:54:58.046552Z'
publication_types:
- '2'
abstract: "Surface registration is often performed as a two step process. A feature matching scheme is first adopted to find a coarse initial alignment between two meshes. Subsequently, a refinement step, which usually operates in the space of rigid motions, is applied to reach an optimal registration with respect to pointwise distances between overlapping areas. In this paper we propose a novel technique that allows to obtain an accurate surface registration in a single step, without the need for an initial motion estimation. The main idea of our approach is to cast the selection of correspondences between points on the surfaces in a game-theoretic framework, where a natural selection process allows matching points that satisfy a mutual rigidity constraint to thrive, eliminating all the other correspondences. This process yields a very robust inlier selection scheme that does not depend on any particular technique for selecting the initial strategies as it relies only on the global geometric compatibility between correspondences. The practical effectiveness of the approach is confirmed by an extensive set of experiments and comparisons with state-of-the-art techniques."
publication: '*Pattern Recognition (PR)*'
---
