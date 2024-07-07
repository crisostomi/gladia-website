---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'KiloNeuS: A Versatile Neural Implicit Surface Representation for Real-Time Rendering'
subtitle: ''
summary: A neural implicit representation which couples solving for a well-defined surface
  and real-time rendering capabilities.
authors:
- Stefano Esposito
- baieri
- Stefan Zellmann
- André Hinkenjann
- rodola
tags: 
  - neural geometry
  - nerf
  - rendering
  - real-time
categories: []
date: '2022-01-01'
lastmod: 2023-02-06T11:39:09+01:00
featured: false
draft: false
publication_short: Preprint

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

links:
- name: 'arXiv'
  url: https://arxiv.org/abs/2206.10885
  


# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-06T10:39:08.326476Z'
publication_types:
- '2'
abstract: NeRF-based techniques fit wide and deep multi-layer perceptrons (MLPs) to
  a continuous radiance field that can be rendered from any unseen viewpoint. However,
  the lack of surface and normals definition and high rendering times limit their
  usage in typical computer graphics applications. Such limitations have recently
  been overcome separately, but solving them together remains an open problem. We
  present KiloNeuS, a neural representation reconstructing an implicit surface represented
  as a signed distance function (SDF) from multi-view images and enabling real-time
  rendering by partitioning the space into thousands of tiny MLPs fast to inference.
  As we learn the implicit surface locally using independent models, resulting in
  a globally coherent geometry is non-trivial and needs to be addressed during training.
  We evaluate rendering performance on a GPU-accelerated ray-caster with in-shader
  neural network inference, resulting in an average of 46 FPS at high resolution,
  proving a satisfying tradeoff between storage costs and rendering quality. In fact,
  our evaluation for rendering quality and surface recovery shows that KiloNeuS outperforms
  its single-MLP counterpart. Finally, to exhibit the versatility of KiloNeuS, we
  integrate it into an interactive path-tracer taking full advantage of its surface
  normals. We consider our work a crucial first step toward real-time rendering of
  implicit neural representations under global illumination.
publication: '*arXiv preprint arXiv:2206.10885*'
---
