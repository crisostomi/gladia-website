---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "MoGround: Measuring and Mitigating Modality Distraction in Vision-Language Models"
subtitle: ''
summary: ''
authors:
- zhou
- Bo Zhao
- Rose Yu
- rodola
- Roberto Dessì

tags: []
categories: []
date: '2026-09-27'
lastmod: 2026-09-29T00:00:00
featured: false
draft: false
publication_short: "Preprint"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2026-09-29T00:00:00'
publication_types:
- '3'
abstract: "We release MoGround, a vision-language dataset spanning four visual domains in which the answer to every question is guaranteed to be available from exactly one modality. This guarantee enables us to measure modality distraction, the failure in which a model answers a question correctly from one modality alone and then flips to a wrong answer once irrelevant content from the other modality is added. Existing probes rarely establish single-modality answerability this way, making it hard to isolate distraction in the first place. Across seven open-source VLMs, we find that modality distraction is not universal but model-dependent. The weaker-grounded modality is the more distracted one (r = +0.86), and distraction scales inversely with grounding strength (r = -0.90). The single-modality guarantee also enables a mitigation method that needs to distinguish between relevant and irrelevant context. Trained on one split of MoGround alone, a weight-space robustness vector reduces distraction on all seven models by 9% to 51%, at a cost of only 0.1 average points of accuracy on standard multimodal tasks."

links:
- name: PDF
  url : https://arxiv.org/pdf/2609.33431
- name: Code
  url : https://github.com/LuckerZOfficiaL/Modality-Distraction
- name: Dataset
  url : https://huggingface.co/datasets/LuckerZ/MoGround

publication: '*ArXiv preprint*'
---
