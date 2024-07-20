# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Cpplex'
copyright = '2024, Marc Melikyan'
author = 'Marc Melikyan'

release = '0.1'
version = '0.1.0'

# -- General configuration

mathjax3_config = {'chtml': {'displayAlign': 'left'}}

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
highlight_language = 'c++'

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
