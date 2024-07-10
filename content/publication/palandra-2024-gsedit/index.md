---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'GSEdit: Efficient Text-Guided Editing of 3D Objects via Gaussian Splatting'
subtitle: ''
summary: ''
authors:
- Francesco Palandra
- Andrea Sanchietti
- baieri
- rodola
tags: []
categories: []
date: '2024-05-21'
lastmod: 2023-10-02T:26:44
featured: false
draft: false
publication_short: "Preprint"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-10-02T:26:44'
publication_types:
- '3'
abstract: "We present GSEdit, a pipeline for text-guided 3D object editing based on Gaussian Splatting models. Our method enables the editing of the style and appearance of 3D objects without altering their main details, all in a matter of minutes on consumer hardware. We tackle the problem by leveraging Gaussian splatting to represent 3D scenes, and we optimize the model while progressively varying the image supervision by means of a pretrained image-based diffusion model. The input object may be given as a 3D triangular mesh, or directly provided as Gaussians from a generative model such as DreamGaussian. GSEdit ensures consistency across different viewpoints, maintaining the integrity of the original object's information. Compared to previously proposed methods relying on NeRF-like MLP models, GSEdit stands out for its efficiency, making 3D editing tasks much faster. Our editing process is refined via the application of the SDS loss, ensuring that our edits are both precise and accurate. Our comprehensive evaluation demonstrates that GSEdit effectively alters object shape and appearance following the given textual instructions while preserving their coherence and detail."
publication: '*arXiv preprint*'
links:
- name: 'arXiv'
  url : https://arxiv.org/abs/2403.05154
---