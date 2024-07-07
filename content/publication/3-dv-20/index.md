---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Instant recovery of shape from spectrum via latent space connections
subtitle: ''
summary: ''
authors:
- marin
- rampini
- Umberto Castellani
- rodola
- Maks Ovsjanikov
- melzi
tags: []
categories: []
date: '2020-11-01'
lastmod: 2023-02-02T06:54:33+01:00
featured: false
draft: false
publication_short: "3DV 2020"

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
publishDate: '2023-02-02T05:54:32.324175Z'
publication_types:
- '1'
abstract: 'We introduce the first learning-based method for recovering shapes from Laplacian spectra. Given an auto-encoder, our model takes the form of a cycle-consistent module to map latent vectors to sequences of eigenvalues. This module provides an efficient and effective linkage between spectrum and geometry of a given shape. Our data-driven approach replaces the need for ad-hoc regularizers required by prior methods, while providing more accurate results at a fraction of the computational cost. Our learning model applies without modifications across different dimensions (2D and 3D shapes alike), representations (meshes, contours and point clouds), as well as across different shape classes, and admits arbitrary resolution of the input spectrum without affecting complexity. The increased flexibility allows us to provide a proxy to differentiable eigendecomposition and to address notoriously difficult tasks in 3D vision and geometry processing within a unified framework, including shape generation from spectrum, mesh super-resolution, shape exploration, style transfer, spectrum estimation from point clouds, segmentation transfer and point-to-point matching.'
publication: "*Proc. Int'l Conference on 3D Vision (3DV)*"

links:
- name: 'PDF'
  url: https://iris.uniroma1.it/retrieve/e3835329-4ec7-15e8-e053-a505fe0a3de9/Marin_Instant%20_2020.pdf
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/riccardomarin/InstantRecoveryFromSpectrum
---
