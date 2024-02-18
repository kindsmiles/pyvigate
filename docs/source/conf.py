# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import subprocess

sys.path.insert(0, os.path.abspath('../../'))

project = 'pyvigate'
copyright = '2024, Abhijith Neil Abraham'
author = 'Abhijith Neil Abraham'
release = '0.0.2'

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



extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# Custom addition for running sphinx-apidoc automatically
def run_apidoc(_):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    module_dir = os.path.join(current_dir, "../../pyvigate")  # Adjust path to your module
    output_path = os.path.join(current_dir, "docs/source")  # Adjust path to output .rst files
    cmd_path = 'sphinx-apidoc'
    if os.name == 'nt':
        cmd_path += '.exe'
    subprocess.check_call([cmd_path, '-f', '-e', '-o', output_path, module_dir, '--force'])

def setup(app):
    app.connect('builder-inited', run_apidoc)

autodoc_mock_imports = ['pyvigate.services.ai']