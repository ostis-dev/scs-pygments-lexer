#!/usr/bin/env python
"""Setup pymdown-lexers."""
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
scs=lexer:SCsLexer
'''

setup(
    name='scs-pygments-lexer',
    version='0.1.0',
    description='Pygments lexer package for SCs-language support.',
    author='Denis Koronchik',
    author_email='denis.koronchik [at] gmail.com',
    url='',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.1'
    ],
    zip_safe=True,
    license='MIT License',
    classifiers=[
    ]
)
