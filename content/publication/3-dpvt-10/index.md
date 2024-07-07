---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Robust game-theoretic inlier selection for bundle adjustment"
subtitle: ''
summary: ''
authors:
- Andrea Albarelli
- rodola
- Andrea Torsello
tags: []
categories: []
date: '2010-05-01'
lastmod: 2023-02-02T06:55:37+01:00
featured: false
draft: false
publication_short: "3DPVT 2010"

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
publishDate: '2023-02-02T05:55:36.962822Z'
publication_types:
- '1'
abstract: "Bundle Adjustment is a widely adopted self-calibration technique that allows to estimate scene structure and camera parameters at once. Typically this happens by iteratively minimizing the reprojection error between a set of 2D stereo correspondences and their predicted 3D positions. This optimization is almost invariantly carried out by means of the Levenberg-Marquardt algorithm, which is very sensitive to the presence of outliers in the input data. For this reason many structure-from-motion techniques adopt some inlier selection algorithm. This usually happens both in the initial feature matching step and by pruning matches with larger reprojection error after an initial optimization. While this works well in many scenarios, outliers that are not filtered before the optimization can still lead to wrong parameter estimation or even prevent convergence. In this paper we introduce a novel stereo correspondences selection schema that exploits Game Theory in order to perform a robust inlier selection before any optimization step. The practical effectiveness of the proposed approach is confirmed by an extensive set of experiments and comparisons with state-of-the-art techniques."
publication: "*Proc. Int'l Symposium on 3D Data Processing, Visualization and Transmission*"

links:
- name: 'PDF'
  url: https://iris.unive.it/retrieve/e4239ddb-5205-7180-e053-3705fe0a3322/3dpvt2010.pdf
- icon: award
  icon_pack: fas
  name: 'Best Student Paper Award'
  url: 
---
