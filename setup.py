#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

from setuptools import setup, find_packages


with open('README.rst') as fl:
    LONG_DESCRIPTION = fl.read()

with open('LICENSE') as fl:
    LICENSE = fl.read()


setup(
    name='CurrencyConverter',
    version='0.13.5',
    author='Ahmad Jourdan',
    author_email='ahmadjourdan@gmail.com',
    url='https://github.com/AhmadJourdan/foreign-currency',
    description='Foreign Currency',
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
        'console_scripts' : [
            'currency_converter=currency_converter.__main__:main'
        ]
    },
)
