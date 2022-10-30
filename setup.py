#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import LanguageSwitcher

setup(
    name="LanguageSwitcher",
    version=LanguageSwitcher.__version__,
    author="LL",
    author_email="orange_jack_liu@outlook.com",
    description="Lnaguage tools",
    long_description='A langugae tool, you can use this to load different language with 3 ~ 4 lines of code.',
    long_description_content_type="text/markdown",
    license="MIT",
    url="",
    packages=find_packages(),
    install_requires=[
        ],
    classifiers=[
        "Environment :: Console",
        'Topic :: Games/Entertainment :: Puzzle Games',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
