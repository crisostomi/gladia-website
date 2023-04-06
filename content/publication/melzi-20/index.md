---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Intrinsic/extrinsic embedding for functional remeshing of 3D shapes
subtitle: ''
summary: ''
authors:
- melzi
- marin
- Pietro Musoni
- Filippo Bardon
- Marco Tarini
- Umberto Castellani
tags:
- Shape analysis
- Geometry processing
- Functional maps
- Surface remeshing
- Shape modeling
categories: []
date: '2020-01-01'
lastmod: 2023-02-08T15:02:31+01:00
featured: false
draft: false
publication_short: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

links:
  - name: URL
    url: https://reader.elsevier.com/reader/sd/pii/S0097849320300194?token=A4863AC87E8DEE6D9DB93E0D0A82B9E73546D60608F9626ED4979759D5E53CB52B9F4C53C71C59F147B6E7A87E5DAD37&originRegion=eu-west-1&originCreation=20230406125403
  - name: GitHub
    url: https://github.com/PietroMsn/CMH
    
# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-08T14:02:30.728206Z'
publication_types:
- '2'
abstract: '3D acquisition pipeline delivers 3D digital models accurately representing
  real-world objects, improving the geometric accuracy and realism of virtual reconstructions.
  However, even after intensive clean-up, the captured models fall short of many of
  the requirements imposed by the downstream application, such as video-games, virtual
  reality, digital movies, etc. Often, the captured 3D model can only serve as a starting
  point for a cascade of subsequent phases, by either digital artists or geometry
  processing algorithms, such as a complete remeshing (or retopology), surface parameterization,
  and skinning for animation. In contrast, we propose a novel remeshing-by-matching
  approach, where we automatically combine the accurate 3D geometry of the captured
  model with the tessellation of a target pre-existing template which already satisfies
  all the professional requirements. At the core of this process, there is a matching
  strategy based on the functional mapping framework. To this end, we introduce a
  new set of basis functions designed for this context: termed Coordinates Manifold
  Harmonics (CMH). We evaluate this strategy (quantitatively and qualitatively) over
  models of different classes, obtaining a favourable comparison with existing methods.'
publication: '*Computers & Graphics*'
doi: https://doi.org/10.1016/j.cag.2020.02.002
links:
- name: URL
  url: https://www.sciencedirect.com/science/article/pii/S0097849320300194
---
