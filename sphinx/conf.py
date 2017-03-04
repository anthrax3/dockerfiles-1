# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

extensions = [
        'sphinx.ext.mathjax',
        'sphinx.ext.todo',
        'sphinxcontrib.seqdiag',
        'sphinxcontrib.actdiag',
        'sphinxcontrib.blockdiag',
        'sphinxcontrib.nwdiag',
        'sphinxcontrib.spelling'
        ]

templates_path = ['templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Wiki'
copyright = u'2017 toko'
author = u'toko'
language = None
exclude_patterns = ['.build', 'Thumbs.db', '.DS_Store', 'README.rst', 'themes']
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = "f6"
html_theme_path = ['themes']
html_context = {
    'css_files': ['_static/custom.css'],
}
html_logo = "static/logo.png"
html_static_path = ['static']
htmlhelp_basename = 'sample-wikidoc'
spelling_word_list_filename='spelling_wordlist.txt'
