# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import sphinx_rtd_theme

project = 'Phenopackets Domain Analysis'
copyright = '2020, Phenopackets Domain Analysis Team'
author = 'Phenopackets Domain Analysis Team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx_rtd_theme',
'recommonmark',
'rst2pdf.pdfbuilder'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
pdf_documents = [
('index', u'PhenopacketsDomainAnalysis', u'Sample doc Title', u'author name')
]

html_theme_options = {
    'collapse_navigation': False,
    'includehidden': False,
     'titles_only': True
}

master_doc = 'toc'

pdf_break_level = 1
pdf_breakside = 'any'

sphinx = {
    'fail_on_warning': True
}

# from: https://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
# TODO: check this issue: https://github.com/readthedocs/sphinx_rtd_theme/issues/117
html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }