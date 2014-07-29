import sys

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['requests', ]

version = sys.version_info[:2]

if version < (2, 7) or (3, 0) <= version <= (3, 1):
    install_requires += ['argparse', ]

setup(name='aprsquake',
      version='0.0.1',
      description='Queries USGS for earthquakes and sends APRS commands',
      long_description=long_description,
      url='https://github.com/casell/aprsquake',
      license='unlicense.org',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'License :: Public Domain',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.0',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Communications :: Ham Radio',
          'Topic :: Scientific/Engineering',
      ],
      test_suite='nose.collector',
      install_requires=install_requires,
      tests_require=['nose', 'httmock'],
      keywords='aprs earthquake usgs',
      packages=find_packages(),
      entry_points={
          'console_scripts': ['aprsquake = aprsquake:main', ],
      })
