# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'dbdicom'
copyright = '2022, QIB-Sheffield'
author = 'QIB-Sheffield'
release = '1.0'

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones
extensions = ['sphinx.ext.napoleon', # parsing of NumPy and Google style docstrings
                'sphinx.ext.autodoc', # sphinx autodocumentation generation
                'sphinx.ext.autosummary', # generates function/method/attribute summary lists
                'sphinx.ext.viewcode', # viewing source code
                'sphinx.ext.intersphinx', # generate links to the documentation of objects in external projects
                'sphinx_rtd_theme'] # ReadTheDocs theme

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path
exclude_patterns = []

# -- Extension configuration -------------------------------------------------
# Map intersphinx to pre-exisiting documentation from other projects used in this project
intersphinx_mapping = {'python': ('https://docs.python.org/3/', None),
                        'numpy': ('https://numpy.org/doc/stable/', None)}
                        
autosummary_generate = True # enable autosummary extension

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css"
html_static_path = ['_static']

# The suffix(es) of source filenames.
#source_suffix = ['.rst', '.md']