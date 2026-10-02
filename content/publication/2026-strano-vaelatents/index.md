---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "How Neural Losses Shape VAE Latents"
subtitle: ''
summary: ''
authors:
- strano
- cerovaz
- mancusi
- mencattini
- rodola

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - 'Equal contribution'
  - ''
  - ''

tags: []
categories: []
date: '2026-05-30'
lastmod: 2026-06-18T20:33:49+02:00
featured: false
draft: false
publication_short: "arXiv 2026"

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
publishDate: '2026-05-30T09:20:56'
publication_types:
- '3'
abstract: "Modern VAEs are rarely trained with the pointwise likelihood implied by the standard β-VAE objective. In practice, pointwise reconstruction is often combined with perceptual and adversarial losses, despite a lack of understanding of how this changes the latent dynamics of the model. We show that the choice of reconstruction loss reshapes the rate-distortion problem itself, altering both the information content and the geometry of the learned latent space in ways that may be invisible from reconstructions alone. First, we prove and verify empirically that augmenting pointwise reconstruction with neural terms, such as perceptual and adversarial objectives, reduces the amount of information stored in the latent representations. Second, we show that neural reconstruction losses systematically change the geometry of the latent space: they make representations more isotropic and distribute uncertainty more evenly across latent dimensions, producing different posterior variance profiles. These findings highlight how the rate-distortion tradeoff is not a comprehensive lens to understand the behavior of VAEs, and we propose a more mechanistic approach to investigate how the choice of a distortion metric reshapes the optimization problem."

links:
- name: arXiv
  url : https://arxiv.org/abs/2606.00635
- name: PDF
  url : https://arxiv.org/pdf/2606.00635

publication: '*arXiv preprint arXiv:2606.00635*'
---
