# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Manual de Estruturas Organizacionais'
copyright = '2025, Demor'
author = 'Diretoria de Modelos Organizacionais'
project_copyright = 'Manual de Estruturas Organizacionais'

release = ''
version = '0.2'

# -- General configuration

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
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'
html_title = ""
# -- html_logo = 'pen_logo_sem_fundo.png'
html_theme_options = {
    'navigation_depth': 5,
    
}

html_favicon = 'icone_principal.png'



# --html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
