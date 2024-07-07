---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Fully spectral partial shape matching
subtitle: ''
summary: ''
authors:
- Or Litany
- rodola
- Alex M. Bronstein
- Michael M. Bronstein
tags: []
categories: []
date: '2017-05-01'
lastmod: 2023-02-02T06:54:53+01:00
featured: false
draft: false
publication_short: "CGF (Proc. EG 2017)"

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
publishDate: '2023-02-02T05:54:52.354713Z'
publication_types:
- '2'
abstract: "We propose an efficient procedure for calculating partial dense intrinsic correspondence between deformable shapes performed entirely in the spectral domain. Our technique relies on the recently introduced partial functional maps formalism and on the joint approximate diagonalization (JAD) of the Laplace-Beltrami operators previously introduced for matching non-isometric shapes. We show that a variant of the JAD problem with an appropriately modified coupling term (surprisingly) allows to construct quasi-harmonic bases localized on the latent corresponding parts. This circumvents the need to explicitly compute the unknown parts by means of the cumbersome alternating minimization used in the previous approaches, and allows performing all the calculations in the spectral domain with constant complexity independent of the number of shape vertices. We provide an extensive evaluation of the proposed technique on standard non-rigid correspondence benchmarks and show state-of-the-art performance in various settings, including partiality and the presence of topological noise."
publication: '*Computer Graphics Forum (CGF)*'

links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.13123
- name: 'PDF'
  url: https://cvg.cit.tum.de/_media/spezial/bib/litany-eg17.pdf
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/orlitany/FSPM
---
