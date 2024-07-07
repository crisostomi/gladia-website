---
# Documentation: https://wowchemy.com/docs/managing-content/

title: A Simple and Effective Relevance-Based Point Sampling for 3D Shapes
subtitle: ''
summary: ''
authors:
- rodola
- Andrea Albarelli
- Daniel Cremers
- Andrea Torsello
tags: []
categories: []
date: '2015-07-01'
lastmod: 2023-02-02T06:54:57+01:00
featured: false
draft: false
publication_short: "PRL"

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
publishDate: '2023-02-02T05:54:57.137113Z'
publication_types:
- '2'
abstract: "The surface of natural or human-made objects usually comprises a collection of distinct regions characterized by different features. While some of them can be flat or can exhibit a constant curvature, others may provide a more mixed landscape, abundant with high frequency information. Depending on the task to be performed, individual region properties can be helpful or harmful. For instance, surface registration can be eased by a set of non-coplanar smooth areas, while distinctive points with high curvature can be key for object recognition. For this reason, it is often critical to perform a surface sub-sampling that is suitable to the actual processing goal. To this end, most of the shape processing pipelines found in literature come bundled with one or more sampling rules, designed to boost their performance and accuracy. In this paper we introduce a sampling method for 3D surfaces that aims to be general enough to be useful for a wide range of tasks. The main idea of our method is to exploit the extent of the region around each point that exhibits limited local changes, granting higher relevance to points contained in compact neighborhoods. The effectiveness of the proposed method is experimented through its adoption as a point sampler within three very different shape processing scenarios."
publication: '*Pattern Recognition Letters (PRL)*'
---
