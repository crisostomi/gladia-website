---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Robust camera calibration using inaccurate targets
subtitle: ''
summary: ''
authors:
- Andrea Albarelli
- rodola
- Andrea Torsello
tags: []
categories: []
date: '2010-08-03'
lastmod: 2023-02-02T06:55:33+01:00
featured: false
draft: false
publication_short: "BMVC 2010"

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
publishDate: '2023-02-02T05:55:32.878132Z'
publication_types:
- '1'
abstract: "Accurate intrinsic camera calibration is essential to any computer vision task that involves image based measurements. Given its crucial role with respect to precision, a large number of approaches have been proposed over the last decades. Despite this rich literature, steady advancements in imaging hardware regularly push forward the need for even more accurate techniques. Some authors suggest generalizations of the camera model itself, others propose novel designs for calibration targets or different optimization schemas. In this paper we take a completely different route by directly addressing one of the most overlooked problems in practical calibration scenarios. Specifically, we drop the assumption that the target is known with enough precision and we adjust it in an iterative way as part of the whole process. This is in fact the case with the typical target used in most of the calibration literature, which is usually printed on paper and stitched on a flat surface. In the experimental section we show that even with such a cheaply crafted target it is possible to obtain a very accurate camera calibration that outperforms those obtained with well-known standard techniques."
publication: '*Proc. British Machine Vision Conference (BMVC)*'

links:
- name: 'PDF'
  url: https://bmva-archive.org.uk/bmvc/2010/conference/paper16/paper16.pdf
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://bmva-archive.org.uk/bmvc/2010/conference/paper16/index.html
---
