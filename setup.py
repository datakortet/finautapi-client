#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""finautapi-client - sample finautapi client
"""

classifiers = """\
Development Status :: 3 - Alpha
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Topic :: Software Development :: Libraries
"""

import setuptools

version = '0.1.0'


setuptools.setup(
    name='finautapi-client',
    version=version,
    install_requires=[],
    description=__doc__.strip(),
    classifiers=[line for line in classifiers.split('\n') if line],
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(exclude=["tests"]),
    zip_safe=False,
)
