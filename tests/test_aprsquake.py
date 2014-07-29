import sys

from nose.tools import assert_equal, assert_raises

from httmock import all_requests, HTTMock

from aprsquake import parse_arguments,\
    generateAPRScommand,\
    run_commands,\
    AUTH_COMMAND,\
    address_port,\
    main

try:
    from nose.tools import assert_is_none
except ImportError:
    from nose.tools import assert_true

    def assert_is_none(obj):
        assert_true(obj is None, '%s is not None' % (obj,))


try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO


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
        'detail': 'http://earthquake.usgs.gov/',
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

TEST_FEATURE_NOMAG = {
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
        'detail': 'http://earthquake.usgs.gov/',
        'sig': 47,
        'net': 'nn',
        'type': 'earthquake',
        'status': 'automatic',
        'updated': 1406558373057,
        'felt': None,
        'alert': None,
        'dmin': 0.133,
        'mag': None,
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


TEST_COMMAND = (u'APRS:;281438q17*281438z3945.32N\\12037.22WQMag (ml) 1.74' +
                ' Depth 15 km @ 14km WSW of Portola, California\n')
TEST_COMMAND_NOMAG = (u'APRS:;281438q00*281438z3945.32N\\12037.22WQMag (ml) ' +
                      '0 Depth 15 km @ 14km WSW of Portola, California\n')


@all_requests
def usgs_mock(url, request):
    return {'content': {'features': [TEST_FEATURE, TEST_FEATURE_NOMAG]}}


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


def test_generate_APRS():
    assert_equal(generateAPRScommand(TEST_FEATURE), TEST_COMMAND)


def test_generate_APRS_MAGNONE():
    assert_equal(generateAPRScommand(TEST_FEATURE_NOMAG), TEST_COMMAND_NOMAG)


def test_address_port_error():
    assert_raises(ValueError, address_port, '127.0.0.1')


TEST_LOGIN = 'TEST'


def test_run_commands_stdout():
    expected_result = (AUTH_COMMAND % TEST_LOGIN) +\
        TEST_COMMAND + \
        TEST_COMMAND_NOMAG
    oldsysout = sys.stdout
    buffer2 = StringIO()
    sys.stdout = buffer2
    run_commands(None,
                 TEST_LOGIN,
                 (generateAPRScommand(comm)
                  for comm in [TEST_FEATURE, TEST_FEATURE_NOMAG]))
    assert_equal(buffer2.getvalue(), expected_result)
    sys.stdout = oldsysout


def test_main_stdout():
    expected_result = (AUTH_COMMAND % TEST_LOGIN) +\
        TEST_COMMAND + \
        TEST_COMMAND_NOMAG
    oldsysout = sys.stdout
    buffer2 = StringIO()
    sys.stdout = buffer2
    with HTTMock(usgs_mock):
        main(('-l%s' % TEST_LOGIN, ))
    assert_equal(buffer2.getvalue(), expected_result)
    sys.stdout = oldsysout
