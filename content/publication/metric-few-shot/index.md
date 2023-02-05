---
title: "Metric based Few-Shot Graph Classification"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- crisostomi
- Simone Antonelli
- Valentino Maiorca
- moschella
- rodola
- Riccardo Marin

# Author notes (optional)
author_notes:
- ""
- ""

date: "2022-06-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: Learning On Graphs (LoG) 2022
publication_short: LoG

abstract: Many modern deep-learning techniques do not work without enormous datasets. At the same time, several fields demand methods working in scarcity of data. This problem is even more complex when the samples have varying structures, as in the case of graphs. Graph representation learning techniques have recently proven successful in a variety of domains. Nevertheless, the employed architectures perform miserably when faced with data scarcity. On the other hand, few-shot learning allows employing modern deep learning models in scarce data regimes without waiving their effectiveness. In this work, we tackle the problem of few-shot graph classification, showing that equipping a simple distance metric learning baseline with a state-of-the-art graph embedder allows to obtain competitive results on the task.While the simplicity of the architecture is enough to outperform more complex ones, it also allows straightforward additions. To this end, we show that additional improvements may be obtained by encouraging a task-conditioned embedding space. Finally, we propose a MixUp-based online data augmentation technique acting in the latent space and show its effectiveness on the task.

# Summary. An optional shortened abstract.
summary: 

tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

links:
- icon: "github"
  icon_pack: "fab"
  name: Github
  url: https://github.com/crisostomi/metric-few-shot-graph

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

<!-- {{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}} -->

Supplementary notes can be added here, including [code, math, and images](https://wowchemy.com/docs/writing-markdown-latex/).
