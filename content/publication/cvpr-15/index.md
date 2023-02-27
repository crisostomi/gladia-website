---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Adopting an unconstrained ray model in light-field cameras for 3D shape reconstruction
subtitle: ''
summary: ''
authors:
- Filippo Bergamasco
- Andrea Albarelli
- cosmo
- Andrea Torsello
- rodola
- Daniel Cremers
tags: []
categories: []
date: '2015-06-01'
lastmod: 2023-02-02T06:55:21+01:00
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

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-02T05:55:20.933811Z'
publication_types:
- '1'
abstract: 'Due to their recent availability as off-the-shelf commercial devices, light-field cameras has gathered increasing attention from both scientific community and industrial operators. However, their composite imaging formation process hinders the ability to exploit the well consolidated stack of calibration methods that are available for traditional cameras. While several efforts have been done to propose practical approaches, most of them still rely on the quasi-pinhole behaviour of the single microlens involved in the capturing process. This results in several drawbacks, ranging from the difficulties in feature detection, due to the reduced size of each microlens, to the need to adopt a model with a relatively small number of parameters. With this paper we propose to embrace a fully non-parametric model for the imaging and we show that it can be properly calibrated with little effort using a dense active target. This process produces a dense set of independent rays that cannot be directly used to produce a conventional image. However, they are an ideal tool for 3D reconstruction tasks, since they are highly redundant, very accurate and they cover a wide range of different baselines. The feasibility and convenience of the process and the accuracy of the obtained calibration are comprehensively evaluated through several experiments.'
publication: "*Proc. Int'l Conference on Computer Vision and Pattern Recognition (CVPR)*"
links:
- name: PDF
  url: https://openaccess.thecvf.com/content_cvpr_2015/papers/Bergamasco_Adopting_an_Unconstrained_2015_CVPR_paper.pdf
---
