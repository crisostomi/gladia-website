---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Shape registration in the time of transformers
subtitle: ''
summary: ''
authors:
- G. Trappolini
- L. Cosmo
- L. Moschella
- R. Marin
- S. Melzi
- E. Rodolà
tags: []
categories: []
date: '2021-01-01'
lastmod: 2023-02-08T19:53:22+01:00
featured: false
draft: false

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
publishDate: '2023-02-08T18:53:21.588350Z'
publication_types:
- '1'
abstract: In this paper, we propose a transformer-based procedure for the efficient
  registration of non-rigid 3D point clouds. The proposed approach is data-driven
  and adopts for the first time the transformer architecture in the registration task.
  Our method is general and applies to different settings. Given a fixed template
  with some desired properties (e.g. skinning weights or other animation cues), we
  can register raw acquired data to it, thereby transferring all the template properties
  to the input geometry. Alternatively, given a pair of shapes, our method can register
  the first onto the second (or vice-versa), obtaining a high-quality dense correspondence
  between the two. In both contexts, the quality of our results enables us to target
  real applications such as texture transfer and shape interpolation. Furthermore,
  we also show that including an estimation of the underlying density of the surface
  eases the learning process. By exploiting the potential of this architecture, we
  can train our model requiring only a sparse set of ground truth correspondences
  (10 ∼ 20% of the total points). The proposed model and the analysis that we perform
  pave the way for future exploration of transformer-based architectures for registration
  and matching applications. Qualitative and quantitative evaluations demonstrate
  that our pipeline outperforms state-of-the-art methods for deformable and unordered
  3D data registration on different datasets and scenarios. © 2021 Neural information
  processing systems foundation. All rights reserved.
publication: '*Advances in Neural Information Processing Systems*'
links:
- name: URL
  url: https://www.scopus.com/inward/record.uri?eid=2-s2.0-85127296298&partnerID=40&md5=0cc00c1e34904f8c64b064c9cbb7da33
---
