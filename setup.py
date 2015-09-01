#!/usr/bin/env python

from distutils.core import setup

setup(name='Distutils',
  version='1.0',
  description='A lexicographic binary encoding. Encode strings, bytearrays, integers, floats, and lists in a compact binary form preserving lexicographic sorting order.',
  author=['Greg Ward', 'Neal Clark'],
  author_email='neal@skiomusic.com',
  url='https://github.com/nealclark/lexical-binary',
  py_modules=['lexicalbinary'],
)
