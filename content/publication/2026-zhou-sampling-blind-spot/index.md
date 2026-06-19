---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Hard or Just Unreached? Diagnosing the Sampling Blind Spot in Math-Reasoning Difficulty Estimation"
subtitle: ''
summary: ''
authors:
- zhou
- Sajel Shah
- rodola
- Roberto Dessì


tags: []
categories: []
date: '2026-06-19'
lastmod: 2025-02-27T:26:44
featured: false
draft: false
publication_short: "ICML 2026 Workshop AI4Math"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2025-27-02T:26:44'
publication_types:
- '1'
abstract: "Math and science reasoning benchmarks rely on pass@k, the fraction of sampled chains that reach gold, as the canonical per-example difficulty signal. The same signal drives RL with verifiable rewards, math data curation, synthetic curricula, and verifier training. We show this proxy has a persistent blind spot on its hardest stratum: on the eight free-form math cells we test (GSM8K and MATH across four open-weight models), 10.3-22.9% of the examples that no sampling seed solves in six tries are instead solved at matched compute by a six-chain deterministic regime. These are greedy decoding plus five cheap residual-stream perturbations applied via activation grafting, while greedy alone solves at most 6% on these math cells. Recovery scales with the additional budget, across perturbations whose mechanistic distinctness we verify across all twelve cells (cross-kind fix-set Jaccard <= 0.47 in every setup). Activation grafting is used as an intervention on internal representations, not a decoding method; we use it purely as a diagnostic and diversification tool, and our recovered items show that the pass@k= 0 % stratum is structurally identifiable in the residual stream rather than that the unmodified model reaches them under ordinary inference."

links:
- name: arXiv
  url : https://arxiv.org/pdf/2606.19636

publication: '*AI4Math Workshop at ICML 2026*'
---