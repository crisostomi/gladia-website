---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Multiview registration via graph diffusion of dual quaternions
subtitle: ''
summary: ''
authors:
- Andrea Torsello
- rodola
- Andrea Albarelli
tags: []
categories: []
date: '2011-06-01'
lastmod: 2023-02-02T06:55:29+01:00
featured: false
draft: false
publication_short: "CVPR 2011"

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
publishDate: '2023-02-02T05:55:28.835070Z'
publication_types:
- '1'
abstract: "Surface registration is a fundamental step in the reconstruction of three-dimensional objects. While there are several fast and reliable methods to align two surfaces, the tools available to align multiple surfaces are relatively limited. In this paper we propose a novel multiview registration algorithm that projects several pairwise alignments onto a common reference frame. The projection is performed by representing the motions as dual quaternions, an algebraic structure that is related to the group of 3D rigid transformations, and by performing a diffusion along the graph of adjacent (i.e., pairwise alignable) views. The approach allows for a completely generic topology with which the pair-wise motions are diffused. An extensive set of experiments shows that the proposed approach is both orders of magnitude faster than the state of the art, and more robust to extreme positional noise and outliers. The dramatic speedup of the approach allows it to be alternated with pairwise alignment resulting in a smoother energy profile, reducing the risk of getting stuck at local minima."
publication: "*Proc. Int'l Conference on Computer Vision and Pattern Recognition (CVPR)*"

links:
- name: 'PDF'
  url: https://www.dsi.unive.it/~atorsell/papers/Conferences/cvpr2011-multiview.pdf
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://ieeexplore.ieee.org/document/5995565
---
