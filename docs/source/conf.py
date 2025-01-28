import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Unichunk Time Series Forecasting'
copyright = '2025, Unichunk LLC'
author = 'Unichunk LLC'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',     # For automatically documenting Python modules
    'sphinx.ext.napoleon',    # For parsing Google-style docstrings
    'sphinx.ext.viewcode',    # For adding links to source code
    'sphinx.ext.githubpages', # For GitHub Pages compatibility
    'myst_parser',           # For Markdown support
    'sphinx_rtd_theme',      # Add this line to enable the theme
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Using Read the Docs theme instead of alabaster
html_static_path = []
html_show_sourcelink = True
html_theme_options = {
    'navigation_depth': 4,
    'titles_only': False
}

# -- Napoleon settings -----------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
