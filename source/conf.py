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
from datetime import datetime
import os
import sys
sys.path.insert(0, os.path.abspath('./_ext'))

import sphinx_bootstrap_theme
from sphinx_gallery.sorting import ExplicitOrder, FileNameSortKey


# -- Project information -----------------------------------------------------

project = 'lets-plot'
copyright = '2020, JetBrains'
author = 'JetBrains'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'jupyter_sphinx',
    'sphinx_gallery.gen_gallery',
    'sphinx_gallery_jupyter',
    'create_cname',
]

cname_url = 'lets-plot.org'

autodoc_default_options = {
    'member-order': 'bysource',
}

autosummary_generate = True

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_use_param = False

examples_dirs = 'gallery_py'

sphinx_gallery_conf = {
    'examples_dirs': examples_dirs,
    'gallery_dirs': 'gallery',
    'remove_config_comments': True,
    'subsection_order': ExplicitOrder(['{0}/_basics'.format(examples_dirs),
                                       '{0}/_features'.format(examples_dirs),
                                       '{0}/_geoms'.format(examples_dirs),
                                       '{0}/_stats'.format(examples_dirs),
                                       '{0}/_scales'.format(examples_dirs),
                                       '{0}/_coordinate_systems'.format(examples_dirs),
                                       '{0}/_faceting'.format(examples_dirs),
                                       '{0}/_position_adjustments'.format(examples_dirs),
                                       '{0}/_labels'.format(examples_dirs),
                                       '{0}/_legends'.format(examples_dirs),
                                       '{0}/_themes'.format(examples_dirs),
                                       '{0}/_zooming'.format(examples_dirs),]),
    'within_subsection_order': FileNameSortKey,
}

sphinx_gallery_jupyter_conf = {
    'notebooks_dirs': '../source_gallery',
    'examples_dirs': examples_dirs,
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import lets_plot
version = lets_plot.__version__
# The full version, including alpha/beta/rc tags.
release = lets_plot.__version__


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_show_sourcelink = False

html_theme_options = {
    'navbar_title': 'Lets-Plot',
    'navbar_links': [
      ('API', 'pages/api'),
      ('Gallery', 'gallery/index'),
    ],
    'bootswatch_theme': 'flatly', # List of themes for v3: https://bootswatch.com/3
    'navbar_sidebarrel': False,
    'bootstrap_version': '3',
}

html_context = {
    'cur_year': datetime.now().year,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]
html_js_files = [
    'js/custom.js',
    'js/language_data.js',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    # Default to no sidebar
    '**': [],

    # local table of contents for the API page
    'pages/api': ['localtoc.html'],
}