#!/usr/bin/env python

import os
import sys

import sortalgos

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'sortalgos',
]

requires = []

setup(
    name='sortalgos',
    version=sortalgos.__version__,
    description='Educational sorting algorithms',
    long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
    author='Gavin Bong',
    author_email='gb.javouhey@gmail.com',
    url='http://raverun.com/projects/2013/algos/',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'sortalgos': 'sortalgos'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
