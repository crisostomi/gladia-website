---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Implicit-ARAP: Efficient Handle-Guided Neural Field Deformation via Local Patch Meshing'
subtitle: ''
summary: ''
authors:
- baieri
- maggioli
- rodola
- melzi
- Zorah Laehner
tags: []
categories: []
date: '2025-09-19'
lastmod: 2023-10-02T:26:44
featured: false
draft: false
publication_short: "NeurIPS 2025"

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
- '1'
abstract: "Neural fields have emerged as a powerful representation for 3D geometry, enabling compact and continuous modeling of complex shapes. Despite their expressive power, manipulating neural fields in a controlled and accurate manner – particularly under spatial constraints – remains an open challenge, as existing approaches struggle to balance surface quality, robustness, and efficiency. We address this by introducing a novel method for handle-guided neural field deformation, which leverages discrete local surface representations to optimize the As-Rigid-As-Possible deformation energy. To this end, we propose the local patch mesh representation, which discretizes level sets of a neural signed distance field by projecting and deforming flat mesh patches guided solely by the SDF and its gradient. We conduct a comprehensive evaluation showing that our method consistently outperforms baselines in deformation quality, robustness, and computational efficiency. We also present experiments that motivate our choice of discretization over marching cubes. By bridging classical geometry processing and neural representations through local patch meshing, our work enables scalable, high-quality deformation of neural fields and paves the way for extending other geometric tasks to neural domains."
publication: '*Conference on Neural Information Processing Systems (NeurIPS 2025)*'
links:
- name: arXiv
  url : https://arxiv.org/abs/2405.12895
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/daniele-baieri/implicit-arap
---