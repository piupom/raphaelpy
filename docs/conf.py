# -*- coding: utf-8 -*-
# RaphaëlPy documentation build configuration file, created by sphinx-quickstart

import sys
import os

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.inheritance_diagram',
]
templates_path = ['_templates']
source_suffix = '.rst'
# The master toctree document.
master_doc = 'index'
project = u'RaphaëlPy'
author = u'Jan Stránský'
copyright = u'2018, {}'.format(author)

version = '1'
release = '1'
pygments_style = 'sphinx'
html_theme = 'classic'
