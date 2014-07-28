from nose.tools import assert_is_none, assert_equal

from aprsquake import parse_arguments, generateAPRScommand


TEST_FEATURE = {
    u'geometry': {
        u'type': u'Point',
        u'coordinates':
        [-120.6203,
         39.7553,
         15.43]
    },
    u'type':
    u'Feature',
    u'properties': {
        u'rms': None,
        u'code':
        u'00453361',
        u'cdi': None,
        u'sources': u',nn,',
        u'nst': 8,
        u'tz': -420,
        u'title': u'M 1.7 - 14km WSW of Portola, California',
        u'magType': u'ml',
        u'detail': u'http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nn00453361.geojson',
        u'sig': 47,
        u'net': u'nn',
        u'type': u'earthquake',
        u'status': u'automatic',
        u'updated': 1406558373057,
        u'felt': None,
        u'alert': None,
        u'dmin': 0.133,
        u'mag': 1.74,
        u'gap': 160.07,
        u'types': u',general-link,geoserve,nearby-cities,origin,phase-data,',
        u'url': u'http://earthquake.usgs.gov/earthquakes/eventpage/nn00453361',
        u'ids': u',nn00453361,',
        u'tsunami': None,
        u'place': u'14km WSW of Portola, California',
        u'time': 1406558282550,
        u'mmi': None
    },
    u'id': u'nn00453361'
}


TEST_COMMAND = u'APRS:;281438q17*281438z3945.32N\\12037.22WQMag (ml) 1.74 Depth 15 km @ 14km WSW of Portola, California\n'


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
