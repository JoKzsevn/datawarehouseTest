from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Opdracht maken van BartWesthoff'
LONG_DESCRIPTION = 'Een library gemaakt als opdracht voor BartWesthoff'

# Setting up
setup(
    name="hrfmp",
    version=VERSION,
    author="Sven Satimin",
    author_email="1064415@hr.nl",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas'],
    keywords=['python', 'school', 'Data Science | Data Engineer'],
    classifiers=[
        "Development Status :: 3 - Release",
        "Intended Audience :: Students",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix Test",
        "Operating System :: MacOS Test :: MacOS X Test",
        "Operating System :: Microsoft :: Windows",
    ]
)