|Build Status| |Coverage Status|

aprsquake
=========

Queries USGS for earthquakes and outputs APRS commands

::

    usage: aprsquake.py [-h] [--address ADDRESS] [--login LOGIN]
                        [--type {significant,4.5,2.5,1.0,all}]
                        [--interval {hour,day,week,month}]

    Queries USGS for earthquakes and outputs APRS commands

    optional arguments:
      -h, --help            show this help message and exit
      --address ADDRESS, -a ADDRESS
                            Host to send commands to as HOST:PORT
      --login LOGIN, -l LOGIN
                            Login credentials
      --type {significant,4.5,2.5,1.0,all}, -t {significant,4.5,2.5,1.0,all}
                            The type of earthquake to retrieve (default:
                            significant)
      --interval {hour,day,week,month}, -i {hour,day,week,month}
                            The interval to retrieve (default: hour)

installation
------------

Install dependencies (just http://python-requests.org) with:

::

    pip install -r requirements.txt

then call aprsquake.py

::

    python aprsquake.py

.. |Build Status| image:: https://travis-ci.org/casell/aprsquake.svg?branch=master
   :target: https://travis-ci.org/casell/aprsquake

.. |Coverage Status| image:: https://coveralls.io/repos/casell/aprsquake/badge.png
  :target: https://coveralls.io/r/casell/aprsquake
