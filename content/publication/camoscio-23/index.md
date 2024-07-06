---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Camoscio: an Italian Instruction-tuned LLaMA"
subtitle: ''
summary: ''
authors:
- santilli
- rodola

tags:
- LLM

categories: []
date: '2023-12-18'
lastmod: 2022-09-30T11:32:00+02:00
featured: false
draft: false
publication_short: "CLiC-it 2023"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
# image:
#   caption: ''
#   focal_point: 'Center'
#   preview_only: false

links:
- name: PDF
  url: https://ceur-ws.org/Vol-3596/paper44.pdf
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/teelinsan/camoscio
- icon: award
  icon_pack: fas
  name: 'Best Student Paper Award'
  url: https://clic2023.ilc.cnr.it/awards/

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-04-28T10:30:59.888843Z'
publication_types:
- '1'
abstract: 'In recent years Large Language Models (LLMs) have increased the state of the art on several natural language processing tasks. However, their accessibility is often limited to paid API services, posing challenges for researchers in conducting extensive investigations. On the other hand, while some open-source models have been proposed by the community, they are typically English-centric or multilingual without a specific adaptation for the Italian language. In an effort to democratize the available and open resources for the Italian language, in this paper we introduce Camoscio: a language model specifically tuned to follow users' prompts in Italian. Specifically, we finetuned the smallest variant of LLaMA (7b) with LoRA on a corpus of instruction prompts translated to Italian via ChatGPT. Results indicate that the model's zero-shot performance on various downstream tasks in Italian competes favorably with existing models specifically finetuned for those tasks. All the artifacts (code, dataset, model) are released to the community.'

publication: '*Italian Conference on Computational Linguistics (CLiC-it 2023)*'
---
