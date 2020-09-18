#!/usr/bin/python3
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='sanic-fire',
    version='0.1',
    description=(
        'sanic-fire is an extension for Sanic that adds support for commands to your application.'
    ),
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    author='Anna',
    author_email='',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/tim2anna/sanic-fire',
    install_requires=[
        'fire>=0.3.1',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)