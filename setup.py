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
          'Topic :: Communications :: Ham Radio',
          'Topic :: Scientific/Engineering',
      ],
      install_requires=install_requires,
      keywords='aprs earthquake usgs',
      packages=find_packages(),
      entry_points={
          'console_scripts': ['aprsquake = aprsquake:main', ],
      })
