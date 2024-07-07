---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Imposing Semi-local Geometric Constraints for Accurate Correspondences Selection
  in Structure from Motion: a Game-Theoretic Perspective'
subtitle: ''
summary: ''
authors:
- Andrea Albarelli
- rodola
- Andrea Torsello
tags: []
categories: []
date: '2012-03-01'
lastmod: 2023-02-02T06:55:01+01:00
featured: false
draft: false
publication_short: "IJCV"

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
publishDate: '2023-02-02T05:55:01.175945Z'
publication_types:
- '2'
abstract: "Most Structure from Motion pipelines are based on the iterative refinement of an initial batch of feature correspondences. Typically this is performed by selecting a set of match candidates based on their photometric similarity; an initial estimate of camera intrinsic and extrinsic parameters is then computed by minimizing the reprojection error. Finally, outliers in the initial correspondences are filtered by enforcing some global geometric property such as the epipolar constraint. In the literature many different approaches have been proposed to deal with each of these three steps, but almost invariably they separate the first inlier selection step, which is based only on local image properties, from the enforcement of global geometric consistency. Unfortunately, these two steps are not independent since outliers can lead to inaccurate parameter estimation or even prevent convergence, leading to the well known sensitivity of all filtering approaches to the number of outliers, especially in the presence of structured noise, which can arise, for example, when the images present several repeated patterns. In this paper we introduce a novel stereo correspondence selection scheme that casts the problem into a Game-Theoretic framework in order to guide the inlier selection towards a consistent subset of correspondences. This is done by enforcing geometric constraints that do not depend on full knowledge of the motion parameters but rather on some semi-local property that can be estimated from the local appearance of the image features. The practical effectiveness of the proposed approach is confirmed by an extensive set of experiments and comparisons with state-of-the-art techniques."
publication: '*International Journal of Computer Vision (IJCV)*'

links:
- name: 'PDF'
  url: https://www.isi.imi.i.u-tokyo.ac.jp/~rodola/ijcv-2011.pdf
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://link.springer.com/article/10.1007/s11263-011-0432-4
---
