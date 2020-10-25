# -*- coding: utf-8 -*-
"""A setuptools based setup module.

Code style:
    python -m isort -rc osl154ua tests
    python -m black osl154ua tests

Build wheel:
    python setup.py bdist_wheel

Update requirements:
    python -m pip freeze -r requirements.txt > requirements.txt

Upload to pypi:
    python -m twine upload dist/*

"""

# To use a consistent encoding
from codecs import open
from os import path

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

from osl154ua import __version__ as app_version

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="osl154ua",
    version=app_version,
    description="Opc Da command line test client for Osl154 specification",
    long_description=long_description,
    keywords="osl154 specification test client",
    url="https://github.com/fholmer/Osl154TestClientUa",
    author="Frode Holmer",
    author_email="fholmer+osl154@gmail.com",
    license="GNU General Public License (GPL)",
    project_urls={"Source Code": "https://github.com/fholmer/Osl154TestClientUa"},
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    packages=find_packages(include=["osl154ua*"]),
    install_requires=[
        "cryptography==3.1.1",
        "opcua==0.98.12",
        "Pillow==8.0.1",
    ],
    entry_points={
        'console_scripts': [
            'osl154ua=osl154ua.__main__:main',
        ],
    },
)
