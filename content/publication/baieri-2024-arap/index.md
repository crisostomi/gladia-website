---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Implicit-ARAP: Efficient Handle-Guided Deformation of High-Resolution Meshes and Neural Fields via Local Patch Meshing'
subtitle: ''
summary: ''
authors:
- baieri
- maggioli
- Zorah Laehner
- melzi
- rodola
tags: []
categories: []
date: '2024-05-21'
lastmod: 2023-10-02T:26:44
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
publishDate: '2023-10-02T:26:44'
publication_types:
- '3'
abstract: "In this work, we present the local patch mesh representation for neural signed distance fields. This technique allows to discretize local regions of the level sets of an input SDF by projecting and deforming flat patch meshes onto the level set surface, using exclusively the SDF information and its gradient. Our analysis reveals this method to be more accurate than the standard marching cubes algorithm for approximating the implicit surface. Then, we apply this representation in the setting of handle-guided deformation: we introduce two distinct pipelines, which make use of 3D neural fields to compute As-Rigid-As-Possible deformations of both high-resolution meshes and neural fields under a given set of constraints. We run a comprehensive evaluation of our method and various baselines for neural field and mesh deformation which show both pipelines achieve impressive efficiency and notable improvements in terms of quality of results and robustness. With our novel pipeline, we introduce a scalable approach to solve a well-established geometry processing problem on high-resolution meshes, and pave the way for extending other geometric tasks to the domain of implicit surfaces via local patch meshing."
publication: '*arXiv preprint*'
links:
- name: arXiv
  url : https://arxiv.org/abs/2405.12895
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/daniele-baieri/implicit-arap
---