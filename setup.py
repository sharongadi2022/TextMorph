from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='TextMorph',
    version='1.0.0',
    packages=[''],
    install_requires=[required],
    url='',
    license='',
    author='TextMorph',
    author_email='sharongadi2004@gmail.com'
    description=''
)
