---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Domain Elastic Transform: Bayesian Function Registration for High-Dimensional Scientific Data'
subtitle: ''
summary: ''
authors:
- Osamu Hirose
- rodola

tags: []
categories: []
date: '2026-03-22'
lastmod: 2026-04-07T:26:44
featured: false
draft: false
publication_short: "Preprint"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2026-04-07T:00:00'
publication_types:
- '3'
abstract: "Nonrigid registration is conventionally divided into point set registration, which aligns sparse geometries, and image registration, which aligns continuous intensity fields on regular grids. However, this dichotomy creates a critical bottleneck for emerging scientific data, such as spatial transcriptomics, where high-dimensional vector-valued functions, e.g., gene expression, are defined on irregular, sparse manifolds. Consequently, researchers currently face a forced choice: either sacrifice single-cell resolution via voxelization to utilize image-based tools, or ignore the critical functional signal to utilize geometric tools. To resolve this dilemma, we propose Domain Elastic Transform (DET), a grid-free probabilistic framework that unifies geometric and functional alignment. By treating data as functions on irregular domains, DET registers high-dimensional signals directly without binning. We formulate the problem within a rigorous Bayesian framework, modeling domain deformation as an elastic motion guided by a joint spatial-functional likelihood. The method is fully unsupervised and scalable, utilizing feature-sensitive downsampling to handle massive atlases. We demonstrate that DET achieves 92% topological preservation on MERFISH data where state-of-the-art optimal transport methods struggle (less than 5%), and successfully registers whole-embryo Stereo-seq atlases across developmental stages -- a task involving massive scale and complex nonrigid growth. "
publication: '*ArXiv preprint*'
links:
- name: arXiv
  url : https://arxiv.org/abs/2603.21235
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/ohirose/bcpd
---