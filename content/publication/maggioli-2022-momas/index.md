---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'MoMaS: Mold Manifold Simulation for real-time procedural texturing'
subtitle: ''
summary: 'A generalization of the algorithm for simulating the evolution of slime mold organisms to work on triangular meshes. The algorithm is implemented on GPU to achieve real-time performance.'
authors:
- maggioli
- marin
- melzi
- rodola
tags: ["Procedural Texturing", "Geometry Processing", "GPU Computing"]
categories: []
date: '2022-01-01'
lastmod: 2023-02-08T16:41:56+01:00
featured: false
draft: false
publication_short: "PG 2022"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

links:
- name: PDF
  url: https://boa.unimib.it/retrieve/09f247d5-0a17-4a2d-a0ba-52e0f39efaf5/Maggioli-2022-Computer%20Graphics%20Forum-VoR.pdf

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-08T15:41:55.045832Z'
publication_types:
- '2'
abstract: The slime mold algorithm has recently been under the spotlight thanks to
  its compelling properties studied across many disciplines like biology, computation
  theory, and artificial intelligence. However, existing implementations act only
  on planar surfaces, and no adaptation to arbitrary surfaces is available. Inspired
  by this gap, we propose a novel characterization of the mold algorithm to work on
  arbitrary curved surfaces. Our algorithm is easily parallelizable on GPUs and allows
  to model the evolution of millions of agents in real-time over surface meshes with
  several thousand triangles, while keeping the simplicity proper of the slime paradigm.
  We perform a comprehensive set of experiments, providing insights on stability,
  behavior, and sensibility to various design choices. We characterize a broad collection
  of behaviors with a limited set of controllable and interpretable parameters, enabling
  a novel family of heterogeneous and high-quality procedural textures. The appearance
  and complexity of these patterns are well-suited to diverse materials and scopes,
  and we add another layer of generalization by allowing different mold species to
  compete and interact in parallel.
publication: '*Computer Graphics Forum*'
---
