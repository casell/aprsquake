from nose.tools import assert_is_none, assert_equal

from aprsquake import parse_arguments, generateAPRScommand


TEST_FEATURE = {
    'geometry': {
        'type': 'Point',
        'coordinates':
        [-120.6203,
         39.7553,
         15.43]
    },
    'type':
    'Feature',
    'properties': {
        'rms': None,
        'code':
        '00453361',
        'cdi': None,
        'sources': ',nn,',
        'nst': 8,
        'tz': -420,
        'title': 'M 1.7 - 14km WSW of Portola, California',
        'magType': 'ml',
        'detail': 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nn00453361.geojson',
        'sig': 47,
        'net': 'nn',
        'type': 'earthquake',
        'status': 'automatic',
        'updated': 1406558373057,
        'felt': None,
        'alert': None,
        'dmin': 0.133,
        'mag': 1.74,
        'gap': 160.07,
        'types': ',general-link,geoserve,nearby-cities,origin,phase-data,',
        'url': 'http://earthquake.usgs.gov/earthquakes/eventpage/nn00453361',
        'ids': ',nn00453361,',
        'tsunami': None,
        'place': '14km WSW of Portola, California',
        'time': 1406558282550,
        'mmi': None
    },
    'id': 'nn00453361'
}


TEST_COMMAND = 'APRS:;281438q17*281438z3945.32N\\12037.22WQMag (ml) 1.74 Depth 15 km @ 14km WSW of Portola, California\n'


def test_default_args_address():
    assert_is_none(parse_arguments('').address)


def test_default_args_login():
    assert_is_none(parse_arguments('').login)


def test_default_args_type():
    assert_equal(parse_arguments('').type, 'significant')


def test_default_args_interval():
    assert_equal(parse_arguments('').interval, 'hour')


def test_args_address_parse():
    assert_equal(parse_arguments(('-a127.0.0.1:2222',)).address,
                 ('127.0.0.1', 2222))


def test_args_login_parse():
    assert_equal(parse_arguments(('-ltest',)).login, 'test')


def test_args_type_parse():
    assert_equal(parse_arguments(('-tall',)).type, 'all')


def test_args_interval_parse():
    assert_equal(parse_arguments(('-iday',)).interval, 'day')


def test_generate_APRS_():
    assert_equal(generateAPRScommand(TEST_FEATURE), TEST_COMMAND)
