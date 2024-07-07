---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Sampling relevant points for surface registration
subtitle: ''
summary: ''
authors:
- Andrea Torsello
- rodola
- Andrea Albarelli
tags: []
categories: []
date: '2011-05-01'
lastmod: 2023-02-02T06:55:32+01:00
featured: false
draft: false
publication_short: "3DPVT 2011"

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
publishDate: '2023-02-02T05:55:31.201195Z'
publication_types:
- '1'
abstract: "Surface registration is a fundamental step in the reconstruction of three-dimensional objects. This is typically a two-step process where an initial coarse motion estimation is followed by a refinement step that almost invariably is some variant of Iterative Closest Point (ICP), which iteratively minimizes a distance function measured between pairs of selected neighboring points. The selection of relevant points on one surface to match against points on the other surface is an important issue in any efficient implementation of ICP, with strong implications both on the convergence speed and on the quality of the final alignment. This is due to the fact that typically on a surface there are a lot of low-curvature points that scarcely constrain the rigid transformation and an order of magnitude less descriptive points that are more relevant for finding the correct alignment. This results in a tendency of surfaces to overfit noise on low-curvature areas sliding away from the correct alignment. In this paper we propose a novel relevant-point sampling approach for ICP based on the idea that points in an area of great change constrain the transformation more and thus should be sampled with higher frequency. Experimental evaluations confront the alignment accuracy obtained with the proposed approach with those obtained with the commonly adopted uniform sub sampling and normal-space sampling strategies."
publication: "*Proc. Int'l Conference on 3D Imaging, Modeling, Processing, Visualization\
  \ and Transmission (3DIMPVT)*"
  
links:
- name: 'PDF'
  url: https://www.dsi.unive.it/~atorsell/papers/Conferences/3dimpvt2011-sampling.pdf
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://ieeexplore.ieee.org/document/5955373
---
