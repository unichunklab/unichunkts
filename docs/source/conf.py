import os
import sys

# If you need to import your code:
# sys.path.insert(0, os.path.abspath('../../'))  # adjust as needed

# Make sure to import the theme (this line is optional but good practice)
import sphinx_rtd_theme

project = 'Unichunk Time Series Forecasting'
author = 'Unichunk LLC'
release = '1.0'

extensions = [
    'sphinx_rtd_theme',
    # ... if you have other extensions
]

# If you don't need any static files, you can empty this
html_static_path = []

# The important part: pick the theme
html_theme = 'sphinx_rtd_theme'
