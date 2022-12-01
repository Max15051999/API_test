import requests
from VectorTile.consts import LAYER, X, Y, Z, URL

def check_status_code(resp, code, message=''):
    status = resp.status_code
    assert status == code, f'Server response statue is not equal {code}'

def check_tag_in_headers(resp, *args):
    for tag in args:
        assert resp.headers.get(tag), f'Headers has not tag {tag}'


def check_tag_in_header_equal_param(tag_name, tag_value):
    assert resp.headers.get(tag_name) == tag_value, f'{tag_name} is not equal {tag_value}'


resp = requests.get(URL)

def test_available_methods():
    methods = resp.headers.get('access-control-allow-methods')
    available_methods = 'GET, OPTIONS, GET, POST, PUT, DELETE, OPTIONS'
    assert methods == available_methods


def test_time_response():
    assert resp.elapsed.seconds < 1, 'Response time more than 1s'


def test_status_code200():
    check_status_code(resp=resp, code=200, message='OK - Binary tile successfully retrieved')

def test_application_type():
    check_tag_in_header_equal_param('content-type', 'application/x-protobuf')

def test_content_encoding_gzip():
    check_tag_in_header_equal_param('content-encoding', 'gzip')

def test_transfer_encoding_chunked():
    check_tag_in_header_equal_param('transfer-encoding', 'chunked')

def test_tags_in_headers_with_everything_code():
    check_tag_in_headers(resp, 'access-control-allow-credentials')

def test_tags_in_headers_with_code200():
    check_tag_in_headers(resp, 'etag', 'expires', 'content-type')

def test_status_code204():
    check_status_code(resp=resp, code=204, message='Undocumented')

def test_status_code304():
    check_status_code(resp=resp, code=304,
                      message='The resource cached in the client (identified by the if-none-match) header has not changed.')

def test_status_code400():
    check_status_code(resp=resp, code=400, message='''
    Possible messages due to request URI validation error.

    1) Layer 'some' is invalid.
    2) Zoom level 100 is invalid. Accepted zoom levels are - [1-17].'''
                      )
    check_tag_in_header_equal_param('content-type', 'application/json')

def test_status_code401():
    check_status_code(resp=resp, code=401, message='Access token is missing or invalid.')
    check_tag_in_header_equal_param('content-type', 'application/json')

def test_status_code404():
    check_status_code(resp=resp, code=404, message='Layer \'some\' is invalid')


def test_status_code500():
    check_status_code(resp=resp, code=500)


def test_correct_params_in_link():
    assert LAYER in ('ozbasemap', 'pol'), 'Layer \'some\' is invalid.'
    assert Z.isdigit(), 'Z is not digit'
    assert 0 <= int(Z) <= 17, 'Z not in the interval from 0-17'
    assert X.isdigit(), 'X is not digit'
    assert 0 <= int(X) <= 2 ** (int(Z) - 1), 'X not in the interval from 0-2^z-1'
    assert Y.isdigit(), 'Y is not digit'
    assert 0 <= int(Y) <= 2 ** (int(Z) - 1), 'Y not in the interval from 0-2^z-1'