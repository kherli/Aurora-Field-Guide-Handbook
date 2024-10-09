# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Handbook'
copyright = '2024, ARCTICS'
author = 'ARCTICS'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
extensions.append("sphinx_wagtail_theme")
html_theme = "sphinx_wagtail_theme"
extensions = ["sphinx.ext.imgmath", "sphinx_wagtail_theme", "sphinxcontrib.bibtex"]
bibtex_bibfiles = ["../../references.bib"]
html_static_path = ["_static"]
master_doc = "index"
html_extra_path = ["_static"]
numfig = True
numfig_secnum_depth = 3
