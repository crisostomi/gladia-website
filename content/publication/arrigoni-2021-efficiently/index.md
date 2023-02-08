---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Efficiently parallelizable strassen-based multiplication of a matrix by its
  transpose
subtitle: ''
summary: ''
authors:
- Viviana Arrigoni
- maggioli
- Annalisa Massini
- rodola
tags: []
categories: []
date: '2021-01-01'
lastmod: 2023-02-08T16:41:53+01:00
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
publishDate: '2023-02-08T15:41:52.152423Z'
publication_types:
- '1'
abstract: The multiplication of a matrix by its transpose, ATA, appears as an intermediate
  operation in the solution of a wide set of problems. In this paper, we propose a
  new cache-oblivious algorithm (AtA) for computing this product, based upon the classical
  Strassen algorithm as a sub-routine. In particular, we decrease the computational
  cost to the time required by Strassen’s algorithm, amounting to floating point operations.
  AtA works for generic rectangular matrices, and exploits the peculiar symmetry of
  the resulting product matrix for saving memory. In addition, we provide an extensive
  implementation study of AtA in a shared memory system, and extend its applicability
  to a distributed environment. To support our findings, we compare our algorithm
  with state-of-the-art solutions specialized in the computation of ATA. Our experiments
  highlight good scalability with respect to both the matrix size and the number of
  involved processes, as well as favorable performance for both the parallel paradigms
  and the sequential implementation, when compared with other methods in the literature.
publication: '*50th International Conference on Parallel Processing*'
---
