---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Orthogonalized Fourier polynomials for signal approximation and transfer
subtitle: ''
summary: 'The usual Laplacian eigenbasis is extended to consider also polynomials of the eigenfunctions. The new extended basis has in increased descriptive power in signal reconstruction and transfer tasks, coming at a very reduced cost.'
authors:
- maggioli
- melzi
- Maksim Ovsjanikov
- Michael M Bronstein
- rodola
tags: ["Spectral Geometry", "Shape Matching", "Signal Transfer"]
categories: []
date: '2021-01-01'
lastmod: 2023-02-08T16:41:52+01:00
featured: false
draft: false
publication_short: "EUROGRAPHICS 2021"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

links:
- name: PDF
  url: https://www.lix.polytechnique.fr/~maks/papers/EG21_Fourier_polynomials.pdf
- name: GitHub
  url: https://github.com/filthynobleman/orthogonalized-fourier-polynomial

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-08T15:41:51.287187Z'
publication_types:
- '1'
abstract: We propose a novel approach for the approximation and transfer
  of signals across 3D shapes. The proposed solution is based on taking pointwise
  polynomials of the Fourier-like Laplacian eigenbasis, which provides a compact and
  expressive representation for general signals defined on the surface. Key to our
  approach is the construction of a new orthonormal basis upon the set of these linearly
  dependent polynomials. We analyze the properties of this representation, and further
  provide a complete analysis of the involved parameters. Our technique results in
  accurate approximation and transfer of various families of signals between near-isometric
  and non-isometric shapes, even under poor initialization. Our experiments, showcased
  on a selection of downstream tasks such as filtering and detail transfer, show that
  our method is more robust to discretization artifacts, deformation and noise as
  compared to alternative approaches.
publication: '*Computer Graphics Forum*'
---
