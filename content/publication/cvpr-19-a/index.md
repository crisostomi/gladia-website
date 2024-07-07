---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'GFrames: Gradient-based local reference frame for 3D shape matching'
subtitle: ''
summary: ''
authors:
- melzi
- Riccardo Spezialetti
- Federico Tombari
- Michael M. Bronstein
- Luigi Di Stefano
- rodola
tags: []
categories: []
date: '2019-06-01'
lastmod: 2023-02-02T06:55:07+01:00
featured: false
draft: false
publication_short: "CVPR 2019"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://ieeexplore.ieee.org/document/8953995
- name: PDF
  url: https://openaccess.thecvf.com/content_CVPR_2019/papers/Melzi_GFrames_Gradient-Based_Local_Reference_Frame_for_3D_Shape_Matching_CVPR_2019_paper.pdf
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://drive.google.com/file/d/17Th7QFhX2dOobcZM38AIqPaBQYg7nldW/view
    
# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-02T05:55:07.122370Z'
publication_types:
- '1'
abstract: "We introduce GFrames, a novel local reference frame (LRF) construction for 3D meshes and point clouds. GFrames are based on the computation of the intrinsic gradient of a scalar field defined on top of the input shape. The resulting tangent vector field defines a repeatable tangent direction of the local frame at each point; importantly, it directly inherits the properties and invariance classes of the underlying scalar function, making it remarkably robust under strong sampling artifacts, vertex noise, as well as non-rigid deformations. Existing local descriptors can directly benefit from our repeatable frames, as we showcase in a selection of 3D vision and shape analysis applications where we demonstrate state-of-the-art performance in a variety of challenging settings."
publication: "*Proc. Int'l Conference on Computer Vision and Pattern Recognition (CVPR)*"
---
