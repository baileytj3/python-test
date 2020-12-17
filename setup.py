"""
Setup file to create package.
"""
from setuptools import (
    find_packages,
    setup,
    )

setup(
    name='python-test',
    version='1.0.1',
    author='Tyler Bailey',
    packages=find_packages(include='src'),
)
