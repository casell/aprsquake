#!/usr/bin/env python
'''Queries USGS for earthquakes and outputs APRS commands'''
from argparse import ArgumentParser
from datetime import datetime

from requests import get


URL = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/%s_%s.geojson'

BASE_APRS = r'APRS:;%(date)sq%(magNoDec)02d*%(date)sz%(lat)s\%(lng)sQ'
APRS_COMMENT = r'Mag (%(magType)s) %(mag)s Depth %(depth)d km @ %(place)s'

APRS_COMMAND = BASE_APRS+APRS_COMMENT


def toDMM(value):
    '''Converts from Decimal degrees to 0 padded APRS format'''
    dmmval = int(value) * 100
    return dmmval + ((value - int(value)) * 60)


def toDMMLat(value):
    '''Converts latitude from Decimal degrees to 0 padded APRS format'''
    postf = 'N' if value > 0 else 'S'
    return '%07.2f%s' % (toDMM(abs(value)), postf)


def toDMMLong(value):
    '''Converts longitude from Decimal degrees to 0 padded APRS format'''
    postf = 'E' if value > 0 else 'W'
    return '%08.2f%s' % (toDMM(abs(value)), postf)


def generateAPRScommand(feature):
    '''Generates the APRS command using BASE_APRS as template starting
    from a geoJSON feature'''
    detail = dict(zip(
        ('lng', 'lat', 'depth'),
        feature['geometry']['coordinates']
    ))
    detail['lng'] = toDMMLong(detail['lng'])
    detail['lat'] = toDMMLat(detail['lat'])
    qdate = datetime.utcfromtimestamp(feature['properties']['time'] / 1000.0)
    detail['date'] = qdate.strftime('%d%H%M')
    detail['mag'] = feature['properties']['mag']
    if detail['mag'] is None:
        detail['mag'] = 0
    detail['magNoDec'] = detail['mag'] * 10
    detail['magType'] = feature['properties']['magType']
    detail['place'] = feature['properties']['place']
    detail['id'] = feature['id']
    return APRS_COMMAND % detail


def fetch_data(quake_type, interval):
    '''Fetches data from USGS and returns the parsed JSON'''
    response = get(URL % (quake_type, interval))
    return response.json()


def main():
    '''Parses arguments and calls other parts'''
    parser = ArgumentParser(description='Queries USGS for earthquakes'
                            ' and outputs APRS commands')
    parser.add_argument('--type', '-t',
                        choices=('significant', '4.5', '2.5', '1.0', 'all'),
                        default='significant',
                        help='The type of earthquake to retrieve')
    parser.add_argument('--interval', '-i',
                        choices=('hour', 'day', 'week', 'month'),
                        default='hour',
                        help='The interval to retrieve')
    args = parser.parse_args()
    json_response = fetch_data(args.type, args.interval)
    commands = (generateAPRScommand(feature)
                for feature in json_response['features'])

    for command in commands:
        print(command)

if __name__ == '__main__':
    main()
