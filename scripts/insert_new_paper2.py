import os


def parse_bibtex_entry(bib_entry):
    bib_lines = bib_entry.strip().split("\n")
    article_id = bib_lines[0].split("{")[1].split(",")[0]
    doi = [line.split("{")[1].split("}")[0] for line in bib_lines if "doi" in line][0]
    url = [line.split("{")[1].split("}")[0] for line in bib_lines if "url" in line][0]
    authors = [line.split("{")[1].split("}")[0] for line in bib_lines if "author" in line][0]
    author_names = [author.split(", ")[::-1] for author in authors.split(" and ")]
    title = [line.split("{")[1].split("}")[0] for line in bib_lines if "title" in line][0]
    conference = [line.split("{")[1].split("}")[0] for line in bib_lines if "publisher" in line][0]
    year = [line.split("{")[1].split("}")[0] for line in bib_lines if "year" in line][0]
    try:
        abstract = [line.split("{")[1].split("}")[0] for line in bib_lines if "abstract" in line][0]
    except:
        abstract = ""
    return article_id, doi, url, author_names, title, conference, year, abstract

def create_dir_and_files(entry_data):
    article_id = entry_data['ARTICLE_ID']
    os.makedirs(article_id, exist_ok=True)
    os.chdir(article_id)

    with open('cite.bib', 'w') as f:
        f.write(entry)

    with open('index.md', 'w') as f:
        f.write(f"""
---
title: "{entry_data['PAPERTITLE']}"

authors:
- {entry_data['Author1_Name']} {entry_data['Author1_LastName']}
- {entry_data['Author2_Name']} {entry_data['Author2_LastName']}
- {entry_data['Author3_Name']} {entry_data['Author3_LastName']}

author_notes:
- ""
- ""
- ""

date: {entry_data['YEAR']}
doi: "{entry_data['DOI']}"

publishDate: ""

publication_types: ["1"]

publication: {entry_data['CONFERENCE']}
publication_short: ""

abstract: {entry_data['ABSTRACT']}

summary: ""

tags: []

featured: true

url_pdf: {entry_data['ARTICLE_URL']}
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# links:
# - icon: "github"
#   icon_pack: "fab"
#   name: Github
#   url: "github_url"

image:
  caption: ""
  focal_point: ""
  preview_only: false

slides: ""
---
        """)

if __name__ == '__main__':
    with open('example.bib', 'r') as f:
        entry = f.read()
    entry_data = parse_bibtex_entry(entry)
    create_dir_and_files(entry_data)