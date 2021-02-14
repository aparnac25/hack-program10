#!/usr/bin/env python

"""
Install icecream package. To install locally use:
	pip install -e .
"""

from setuptools import setup

setup(
    name="chranalyze",
    version="0.0.1",
    entry_points={
        'console_scripts': ['chranalyze = chranalyze.__main__:run_program']
    }
)