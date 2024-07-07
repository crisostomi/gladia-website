---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Reduced Representation of Deformation Fields for Effective Non-rigid Shape Matching'
subtitle: ''
summary: ''
authors:
- Riccardo Marin
- rodola
- Maks Ovsjanikov
- Ramana Subramanyam Sundararaman
tags: []
categories: []
date: '2022-01-01'
lastmod: 2023-02-06T12:13:55+01:00
featured: false
draft: false
publication_short: "NeurIPS 2022"

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
publishDate: '2023-02-06T11:13:54.626749Z'
publication_types:
- '2'
abstract: "In this work we present a novel approach for computing correspondences between non-rigid objects, by exploiting a reduced representation of deformation fields. Different from existing works that represent deformation fields by training a general-purpose neural network, we advocate for an approximation based on mesh-free methods. By letting the network learn deformation parameters at a sparse set of positions in space (nodes), we reconstruct the continuous deformation field in a closed-form with guaranteed smoothness. With this reduction in degrees of freedom, we show significant improvement in terms of data-efficiency thus enabling limited supervision. Furthermore, our approximation provides direct access to first-order derivatives of deformation fields, which facilitates enforcing desirable regularization effectively. Our resulting model has high expressive power and is able to capture complex deformations. We illustrate its effectiveness through state-of-the-art results across multiple deformable shape matching benchmarks."
publication: '*Advances in Neural Information Processing Systems*'
links:
- name: 'PDF'
  url: https://proceedings.neurips.cc/paper_files/paper/2022/file/43d1d3bdd92204c96fa4ac3c578f6a33-Paper-Conference.pdf
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://dl.acm.org/doi/10.5555/3600270.3601026
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/Sentient07/DeformationBasis
---
