from setuptools import setup

with open('readme.md') as f:
	longdescr=f.read()

setup(
name='framework',
version='2.0',
author='masonasons',
author_email='mason@masonasons.me',
description='Python3 compatible audiogame Framework using Synthizer and Lucia',
long_description=longdescr,
long_description_content_type='text/markdown',
url='https://github.com/masonasons/framework'
)