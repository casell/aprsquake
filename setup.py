import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = ['requests', ]

version = sys.version_info[:2]

if version < (2, 7) or (3, 0) <= version <= (3, 1):
    install_requires += ['argparse', ]

setup(name='APRSQuake',
      install_requires=install_requires,
      long_description='Queries USGS for earthquakes and outputs APRS commands',
      packages=['aprsquake', ],
      package_data={'': ['LICENSE', 'README.md']},
      package_dir={'requests': 'requests', },
      include_package_data=True,
      entry_points={
          'console_scripts': ['aprsquake = aprsquake:main', ],
      })
