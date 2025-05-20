# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Estruturas Organizacionais'
copyright = '2025, Demor'
author = 'Diretoria de Modelos Organizacionais'
project_copyright = 'Estruturas Organizacionais'

release = ''
version = '0.2'

language = 'pt_BR'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
    'sphinx.ext.viewcode',
    
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

numfig = True

numfig_format = {
    'figure': 'Figura %s',
    'table': 'Tabela %s', 
    'code-block': 'Listagem %s',
    'section': 'Seção %s'
}

numfig_secnum_depth = 1

# -- Options for HTML output

html_theme = 'furo'
html_title = ""

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#006778",  # Títulos e links principais – teal escuro
        "color-brand-content": "#008891",  # Links secundários e ênfase – azul esverdeado
        "color-sidebar-background": "#f8f9fa",  # Fundo da barra lateral – cinza muito claro
        "color-sidebar-link-text": "#212529",  # Texto dos links da sidebar – quase preto
        "color-sidebar-link-text--top-level": "#006778",  # Link de primeiro nível – teal escuro
        "color-sidebar-link-text--active": "#008891",  # Link ativo na sidebar – azul esverdeado
        "color-admonition-background": "#e0f7fa",  # Fundo de blocos informativos – azul claro
        "color-foreground-primary": "#212529",  # Cor padrão do texto – quase preto
        "color-foreground-muted": "#6c757d",  # Texto menos importante – cinza médio
        "color-background-primary": "#ffffff",  # Fundo principal – branco
    },
    "dark_css_variables": {
        "color-brand-primary": "#66d9ef",  # Títulos e links – azul ciano claro
        "color-brand-content": "#38b2ac",  # Links secundários – verde azulado suave
        "color-sidebar-background": "#1e1e1e",  # Fundo da barra lateral – cinza escuro
        "color-sidebar-link-text": "#d1d5db",  # Texto dos links da sidebar – cinza claro
        "color-sidebar-link-text--top-level": "#66d9ef",  # Link de primeiro nível – azul claro
        "color-sidebar-link-text--active": "#38b2ac",  # Link ativo – verde azulado suave
        "color-admonition-background": "#2d3748",  # Fundo de blocos informativos – cinza azulado escuro
        "color-foreground-primary": "#e2e8f0",  # Texto principal – cinza muito claro
        "color-foreground-muted": "#a0aec0",  # Texto secundário – cinza médio
        "color-background-primary": "#121212",  # Fundo principal – quase preto
    },
    "navigation_with_keys": True,  # Permite navegação via teclas ← ↑ → ↓
}




html_static_path = ['_static']


html_favicon = 'icone_principal.png'

# -- Options for EPUB output
epub_show_urls = 'footnote'

latex_elements = {
    'babel': '\\usepackage[brazil]{babel}',
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': r'''
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{2}
''',
}

bibtex_bibfiles = ['referencias.bib']
bibtex_default_style = 'alpha'

