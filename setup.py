from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

_version_ = "0.0.6"
REPO_NAME = "mongodbconnector"
PKG_NAME= "databaseautomation"
AUTHOR_USER_NAME = "sachin62025"
AUTHOR_EMAIL = "sachinkumar18449@iiitmanipur.ac.in"

setup(
    name=PKG_NAME,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    )