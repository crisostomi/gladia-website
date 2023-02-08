---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'ZoomOut: Spectral Upsampling for Efficient Shape Correspondence'
subtitle: ''
summary: ''
authors:
- melzi
- Jing Ren
- rodola
- Abhishek Sharma
- Peter Wonka
- Maks Ovsjanikov
tags:
- spectral methods
- shape matching
- functional maps
categories: []
date: '2019-11-01'
lastmod: 2023-02-08T15:02:32+01:00
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
publishDate: '2023-02-08T14:02:31.810661Z'
publication_types:
- '2'
abstract: We present a simple and efficient method for refining maps or correspondences
  by iterative upsampling in the spectral domain that can be implemented in a few
  lines of code. Our main observation is that high quality maps can be obtained even
  if the input correspondences are noisy or are encoded by a small number of coefficients
  in a spectral basis. We show how this approach can be used in conjunction with existing
  initialization techniques across a range of application scenarios, including symmetry
  detection, map refinement across complete shapes, non-rigid partial shape matching
  and function transfer. In each application we demonstrate an improvement with respect
  to both the quality of the results and the computational speed compared to the best
  competing methods, with up to two orders of magnitude speed-up in some applications.
  We also demonstrate that our method is both robust to noisy input and is scalable
  with respect to shape complexity. Finally, we present a theoretical justification
  for our approach, shedding light on structural properties of functional maps.
publication: '*ACM Trans. Graph.*'
doi: 10.1145/3355089.3356524
links:
- name: URL
  url: https://doi.org/10.1145/3355089.3356524
---
