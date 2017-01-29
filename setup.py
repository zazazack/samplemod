# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Zachary Wilson',
    author_email='wilsonze@gmail.com',
    url='https://github.com/zazazack/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
