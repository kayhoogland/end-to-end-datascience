#!/usr/bin/env python

from setuptools import setup, find_packages

base_packages = [
    "fastapi",
    "scikit-learn",
    "scikit-lego",
    "gin-config",
    "jupyterlab",
    "flake8",
    "black",
    "mypy",
    "pytest",
    "nb-black",
    "memo",
    "pandas-profiling",
]

setup(
    name="src",
    version="1.0",
    description="End to end data science pipeline",
    author="Kay Hoogland",
    author_email="kayhoogland@hey.com",
    url="https://github.com/kayhoogland/datascience-end-to-end",
    install_requires=base_packages,
    packages=find_packages(exclude=["notebooks"]),
)
