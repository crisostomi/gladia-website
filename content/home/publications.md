---
active: true

widget: pages

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 40

title: Featured Publications
subtitle: ''

content:
  # Page type to display. E.g. post, talk, publication...
  page_type: publication
  # Choose how much pages you would like to display (0 = all pages)
  count: 10
  # Choose how many pages you would like to offset by
  offset: 0
  # Page order: descending (desc) or ascending (asc) date.
  order: desc
  # Filter on criteria
  filters:
    tag: 'featured'
    category: ''
    publication_type: ''
    author: ''
    exclude_featured: false
design:
  # Choose a view for the listings:
  #   1 = List
  #   2 = Compact
  #   3 = Card
  #   4 = Citation (publication only)
  view: community/paper
---

{{% callout note %}}
Find the complete list in [publications](./publication/).
{{% /callout %}}
