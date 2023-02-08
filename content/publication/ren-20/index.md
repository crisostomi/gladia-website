---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'MapTree: Recovering Multiple Solutions in the Space of Maps'
subtitle: ''
summary: ''
authors:
- Jing Ren
- melzi
- Maks Ovsjanikov
- Peter Wonka
tags:
- shape matching
- functional maps
- spectral methods
categories: []
date: '2020-11-01'
lastmod: 2023-02-08T15:02:30+01:00
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
publishDate: '2023-02-08T14:02:29.941635Z'
publication_types:
- '2'
abstract: In this paper we propose an approach for computing multiple high-quality
  near-isometric dense correspondences between a pair of 3D shapes. Our method is
  fully automatic and does not rely on user-provided landmarks or descriptors. This
  allows us to analyze the full space of maps and extract multiple diverse and accurate
  solutions, rather than optimizing for a single optimal correspondence as done in
  most previous approaches. To achieve this, we propose a compact tree structure based
  on the spectral map representation for encoding and enumerating possible rough initializations,
  and a novel efficient approach for refining them to dense pointwise maps. This leads
  to a new method capable of both producing multiple high-quality correspondences
  across shapes and revealing the symmetry structure of a shape without a priori information.
  In addition, we demonstrate through extensive experiments that our method is robust
  and results in more accurate correspondences than state-of-the-art for shape matching
  and symmetry detection.
publication: '*ACM Trans. Graph.*'
doi: 10.1145/3414685.3417800
links:
- name: URL
  url: https://doi.org/10.1145/3414685.3417800
---
