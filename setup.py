#!/usr/bin/env python

from __future__ import absolute_import
from distutils.core import setup

setup(
  name='lexicalbinary',
  version='1.0',
  description='A lexicographic binary encoding. Encode strings, bytearrays, integers, floats, and lists in a compact binary form preserving lexicographic sorting order.',
  author=['Greg Ward', 'Neal Clark'],
  author_email='neal@skiomusic.com',
  url='https://github.com/skio-music/lexical-binary',
  license='MIT',
  py_modules=['lexicalbinary'],
)
