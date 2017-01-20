from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='partstem',
      version=version,
      description="0.1",
      long_description="""\
      Fork NLTK Snowball stemmer""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='snowball nltk',
      author='Andrey Perelygin',
      author_email='andrey@perelygin.me',
      url='perelygin.me',
      license='Apache License v.2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            "nltk"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
