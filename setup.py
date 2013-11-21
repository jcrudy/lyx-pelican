from distutils.core import setup

import sys
import os
sys.path.insert(0, os.path.join('.', 'lyxpelican'))
from _version import __version__

# Create a dictionary of arguments for setup
setup_args = {'name': 'lyx-pelican',
              'version': __version__,
              'author': 'Jason Rudy',
              'author_email': 'jcrudy@gmail.com',
              'packages': ['lyxpelican', 'lyxpelican.test'],
              'license': 'LICENSE.txt',
              'description':
              'A Pelican plugin for reading lyx files',
              'long_description': open('README.md', 'r').read(),
              'py_modules': ['lyxpelican.lyxpelican',
                             'lyxpelican.elyxer', 
                             'lyxpelican.elyxer_adapter', 
                             'lyxpelican._version'],
              'classifiers': ['Development Status :: 3 - Alpha'],
              'requires': ['pelican']}

# Finally
setup(**setup_args)
