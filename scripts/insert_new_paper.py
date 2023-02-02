import os

bib_entry = """
@article{<ARTICLE_ID>,
  doi = {<DOI>},
  url = {<ARTICLE_URL>},
  author = {<Author1_LastName>, <Author1_Name> and <Author2_LastName>, <Author2_Name>} and <Author3_LastName>, <Author3_Name>}
  keywords = {<KEYWORDS>},
  title = {<PAPERTITLE>},
  publisher = {<CONFERENCE>},
  year = {<YEAR>},
  copyright = {<COPYRIGHTS>},
  abstract={<ABSTRACT>}
}
"""

def extract_info(bib_entry):
    bib_lines = bib_entry.strip().split("\n")
    article_id = bib_lines[0].split("{")[1].split(",")[0]
    doi = [line.split("{")[1].split("}")[0] for line in bib_lines if "doi" in line][0]
    url = [line.split("{")[1].split("}")[0] for line in bib_lines if "url" in line][0]
    authors = [line.split("{")[1].split("}")[0] for line in bib_lines if "author" in line][0]
    author_names = [author.split(", ")[::-1] for author in authors.split(" and ")]
    title = [line.split("{")[1].split("}")[0] for line in bib_lines if "title" in line][0]
    conference = [line.split("{")[1].split("}")[0] for line in bib_lines if "publisher" in line][0]
    year = [line.split("{")[1].split("}")[0] for line in bib_lines if "year" in line][0]
    abstract = [line.split("{")[1].split("}")[0] for line in bib_lines if "abstract" in line][0]
    return article_id, doi, url, author_names, title, conference, year, abstract

def create_index_md(article_id, doi, url, author_names, title, conference, year, abstract):
    index_md = f"""
---
title: "{title}"

authors:
{
    "\n".join(
        [f"- {first_name} {last_name}" for first_name, last_name in author_names]
    )
}

author_notes:
{
    "\n".join(
        [f"- \"\"" for _ in author_names]
    )
}

date: {year}
doi: "{doi}"

publishDate: ""

publication_types: ["1"]

publication: {conference}
publication_short: ""

abstract: {abstract}

summary: ""

tags: []

featured: true

url_pdf: {url}
url_code: ''
url_dataset: ''
url_poster: ''
url_project:
'''
"""

    return index_md