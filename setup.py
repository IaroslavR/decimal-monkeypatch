import sys
import os

from distutils.core import setup
from distutils.sysconfig import get_python_lib

setup_kwargs = dict(
    name = 'autowrapt',
    version = '1.0',
    description = 'Boostrap mechanism for monkey patches.',
    author = 'Graham Dumpleton',
    author_email = 'Graham.Dumpleton@gmail.com',
    license = 'BSD',
    url = 'https://github.com/GrahamDumpleton/autowrapt',
    py_modules = ['autowrapt'],
    data_files = [(get_python_lib(prefix=''), ['autowrapt-init.pth'])],
)

setup(**setup_kwargs)