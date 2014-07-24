aprsquake
=========

Queries USGS for earthquakes and outputs APRS commands

```
usage: aprsquake.py [-h] [--type {significant,4.5,2.5,1.0,all}]
                     [--interval {hour,day,week,month}]

Queries USGS for earthquakes

optional arguments:
  -h, --help            show this help message and exit
  --type {significant,4.5,2.5,1.0,all}, -t {significant,4.5,2.5,1.0,all}
                        The type of earthquake to retrieve (default: significant)
  --interval {hour,day,week,month}, -i {hour,day,week,month}
                        The interval to retrieve (default: hour)
```

installation
------------

Install dependencies (just http://python-requests.org) with:

```
pip install -r requirements.txt
```

then call aprsquake.py

```
python aprsquake.py
```
