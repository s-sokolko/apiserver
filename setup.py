__author__ = 'godzilla'

import os
from setuptools import setup

# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="apiserver",
    version="0.0.1",
    author="Stanislav Sokolko",
    author_email="s.sokolko@gmail.com",
    description=("Asyncio-based micro API server template and example"),
    long_description=read('README.md'),
    packages=["apiserver"],
    test_suite="tests",
    tests_require=[
        'asynctest==0.12.2'
    ],
    install_requires=[
        'cli_logging==0.0.2',
	'aiohttp==3.3.2',
    ],
    dependency_links=[
        'git+https://github.com/s-sokolko/python-cli-logging.git@master#egg=cli_logging-0.0.2',
    ],
)

