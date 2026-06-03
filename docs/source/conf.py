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

# -- Configuração para priorizar GIF no HTML (Truque do Asterisco)
from sphinx.builders.html import StandaloneHTMLBuilder

StandaloneHTMLBuilder.supported_image_types = [
    'image/gif',
    'image/png',
    'image/jpeg',
]


html_theme_options = {
    "light_css_variables": {

        # --- CORES PRINCIPAIS DO SITE ---
        "color-brand-primary": "#006778",  # Títulos e links principais
        "color-brand-content": "#008891",  # Links secundários
        "color-sidebar-background": "#f8f9fa",  # Fundo da barra lateral 
        "color-sidebar-link-text": "#212529",  # Texto dos links do menu
        "color-sidebar-link-text--top-level": "#006778",  # Link principal no menu
        "color-sidebar-link-text--active": "#008891",  # Link selecionado no menu
        "color-foreground-primary": "#212529",  # Cor padrão do texto
        "color-foreground-muted": "#6c757d",  # Texto menos importante
        "color-background-primary": "#ffffff",  # Fundo principal branco
        
        # --- CORES DAS CAIXAS DE ALERTA (MODO CLARO) ---
        "color-admonition-title--note": "#005b96", # Azul para a caixa "Nota"
        "color-admonition-title-background--note": "#e6f2ff", # Fundo do título da "Nota"
        
        "color-admonition-title--tip": "#008891", # Verde/Azul para "Dica"
        "color-admonition-title-background--tip": "#e0f7fa", 
        
        "color-admonition-title--important": "#006778", # Verde Escuro para "Importante"
        "color-admonition-title-background--important": "#d0f0f5",
        
        "color-admonition-title--warning": "#d97706", # Laranja para "Aviso"
        "color-admonition-title-background--warning": "#fef3c7",
        
        "color-admonition-title--caution": "#d97706", # Laranja para "Cuidado"
        "color-admonition-title-background--caution": "#fef3c7",
        
        "color-admonition-title--danger": "#dc2626", # Vermelho para "Perigo"
        "color-admonition-title-background--danger": "#fee2e2",
    },
    "dark_css_variables": {

        # --- CORES PRINCIPAIS DO SITE (MODO ESCURO) ---
        "color-brand-primary": "#66d9ef",  
        "color-brand-content": "#38b2ac",  
        "color-sidebar-background": "#1e1e1e",  
        "color-sidebar-link-text": "#d1d5db",  
        "color-sidebar-link-text--top-level": "#66d9ef",  
        "color-sidebar-link-text--active": "#38b2ac",  
        "color-foreground-primary": "#e2e8f0",  
        "color-foreground-muted": "#a0aec0",  
        "color-background-primary": "#121212",  

        # --- CORES DAS CAIXAS DE ALERTA (MODO ESCURO) ---
        "color-admonition-title--note": "#66d9ef",
        "color-admonition-title-background--note": "rgba(102, 217, 239, 0.1)",
        
        "color-admonition-title--tip": "#38b2ac",
        "color-admonition-title-background--tip": "rgba(56, 178, 172, 0.1)",
        
        "color-admonition-title--important": "#66d9ef",
        "color-admonition-title-background--important": "rgba(102, 217, 239, 0.1)",
        
        "color-admonition-title--warning": "#f6ad55",
        "color-admonition-title-background--warning": "rgba(246, 173, 85, 0.1)",
        
        "color-admonition-title--caution": "#f6ad55",
        "color-admonition-title-background--caution": "rgba(246, 173, 85, 0.1)",
        
        "color-admonition-title--danger": "#fc8181",
        "color-admonition-title-background--danger": "rgba(252, 129, 129, 0.1)",
    },
    "navigation_with_keys": True,  
}


html_static_path = ['_static']
html_favicon = '_static/images/favicon.png'
html_css_files = ['custom.css']

latex_additional_files = ['_static/images/capa_pdf.png']

# -- Options for EPUB output
epub_show_urls = 'footnote'

latex_elements = {
    'babel': '\\usepackage[brazil]{babel}',
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{2}
\usepackage{graphicx}

''',
'maketitle': f'''
\\begin{{titlepage}}
\\thispagestyle{{empty}}
\\vspace{{1cm}}
\\begin{{center}}
{{\\LARGE \\bfseries Ministério da Gestão e da Inovação em Serviços Públicos}}\\\\[0.2cm]
{{\\Large \\bfseries Secretaria De Gestão e Inovação}}\\\\[0.2cm]
{{\\large \\bfseries {author}}}
\\end{{center}}

\\vspace{{3cm}}
\\begin{{center}}
\\includegraphics[width=16cm]{{capa_pdf.png}}
\\end{{center}}

\\vfill
\\hfill {{\\textbf{{\\today}}}}

\\newpage
\\thispagestyle{{empty}}

\\noindent\\textbf{{Ministério da Economia}}\\\\
Secretaria Especial de Desburocratização, Gestão e Governo Digital\\\\
Secretaria de Gestão\\\\
Departamento de Modelos Organizacionais\\\\[1cm]

\\textbf{{Colaboraram com a 1ª edição:}}\\\\
Juliana Akiko Noguchi Suzuki (Org.), Danyela de Oliveira Felix (Org.), Antonio Augusto Ignacio Amaral, Giovanna de Sá Lúcio, Christiano Perez de Resende, Eduardo Monteiro Pastore, Kaiser Freiras, Manuel Ferreira Filho.\\\\[0.5cm]

\\textbf{{Colaboraram com a 2ª edição:}}\\\\
Juliana Akiko Noguchi Suzuki, Danyela de Oliveira Felix, Frederico Porto de Souza, Marcos Santos Kroll, Giovanna de Sá Lúcio, Christiano Perez de Resende, Sheila Maria Reis Ribeiro, Eduardo Monteiro Pastore, Sylvia Helena Figueiredo Prata, Rodrigo Machado Bolina, Maria Beatriz Teixeira Barral Vidal, Iracema Pontes da Cruz.\\\\[0.5cm]

\\textbf{{Assessoria Especial de Comunicação Social}}\\\\
Supervisão: Letícia Barbosa\\\\
Capa: Jamil Ghani\\\\
Editoração: Rogério Fernandes Guimarães\\\\[0.5cm]

Brasília (DF), 27 de maio de 2019\\\\[1cm]

\\fbox{{
  \\begin{{minipage}}{{0.9\\textwidth}}
  \\small
  B823m\\\\
  Brasil. Ministério da Economia.\\\\[0.5em]
  Manual de Estruturas Organizacionais do Poder Executivo Federal / Ministério da Economia, Secretaria de Gestão. – 2. ed. -- Brasília: Ministério da Economia, 2019.\\\\[0.5em]
  100 p.: il.\\\\[0.5em]
  1. Administração Pública 2. Estrutura Organizacional 3. Poder Executivo Federal\\\\
  I. Título II. Secretaria Especial de Desburocratização, Gestão e Governo Digital.\\\\
  CDU 351:005.72
  \\end{{minipage}}
}}
\\end{{titlepage}}
''',
}



bibtex_bibfiles = ['referencias.bib']
bibtex_default_style = 'apa'
#bibtex_default_style = 'alpha'
#bibtex_reference_style = 'author_year'

