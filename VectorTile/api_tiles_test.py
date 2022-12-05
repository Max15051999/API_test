import requests
import VectorTile.consts as consts
import check_functions as chk

resp = requests.get(consts.URL)  # GET-запрос на сервер


def test_available_methods():
    """ Тест, проверяющий наличие списка запросов в заголовке ответа сервера """

    methods = resp.headers.get('access-control-allow-methods')
    available_methods = 'GET, OPTIONS, GET, POST, PUT, DELETE, OPTIONS'
    assert methods == available_methods


def test_time_response():
    """ Тест, проверяющий, что время получения ответа от сервера меньше 1-ой секунды """

    assert resp.elapsed.seconds < 1, 'Response time more than 1s'


def test_status_code200():
    """ Тест, проверяющий что код ответа сервера равен 200 """

    chk.check_status_code(resp=resp, code=200, message='OK - Binary tile successfully retrieved')
    chk.check_tag_in_headers(resp=resp,
                             tags=('etag', 'expires', 'last-modified', 'content-encoding', 'content-encoding',))
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/x-protobuf')
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-encoding', tag_value='br')


def test_status_code204():
    """ Тест, проверяющий что код ответа сервера равен 204 и что в нём
            содержатся соответствующие заголовки
    """

    chk.check_status_code(resp=resp, code=204, message='Undocumented')
    chk.check_tag_in_headers(resp=resp, tags=('expires', 'content-security-policy',
                                              'cache-control', 'access-control-allow-private-network',))


def test_status_code304():
    """ Тест, проверяющий что код ответа сервера равен 304 """

    chk.check_status_code(resp=resp, code=304,
                          message='The resource cached in the client (identified by the if-none-match) header has not '
                                  'changed.')


def test_status_code400():
    """ Тест, проверяющий что код ответа сервера равен 400 """

    chk.check_status_code(resp=resp, code=400, message='''
                                    Possible messages due to request URI validation error.

                                    1) Layer 'some' is invalid.
                                    2) Zoom level 100 is invalid. Accepted zoom levels are - [1-17].
                                '''
                          )
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/json')

    json_data = resp.json()

    chk.check_application_json_equal_template(json_data=json_data,
                                              keys_in_json=consts.KEYS_TYPES_IN_JSON_CODE_400)


def test_status_code401():
    """ Тест, проверяющий что код ответа сервера равен 401 """

    chk.check_status_code(resp=resp, code=401, message='Access token is missing or invalid.')
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/json')

    json_data = resp.json()

    chk.check_application_json_equal_template(json_data=json_data,
                                              keys_in_json=consts.KEYS_TYPES_IN_JSON_CODE_401)


def test_status_code404():
    """ Тест, проверяющий что код ответа сервера равен 404 """

    chk.check_status_code(resp=resp, code=404)
    chk.check_response_body_equal_param(resp=resp, expect_text=f'Function source \'{consts.LAYER}\' not found',
                                        text_split='"')


def test_status_code500():
    """ Тест, проверяющий, что код ответа сервера равен 500 """

    chk.check_status_code(resp=resp, code=500)
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='text/html; charset=UTF-8')
    chk.check_response_body_equal_param(resp=resp, expect_text=consts.RESP_BODY_500, text_split="'")

def test_status_code504():
    """ Тест, проверяющий, что код ответа сервера равен 504 """

    chk.check_status_code(resp=resp, code=504)
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='text/html; charset=UTF-8')
    chk.check_response_body_equal_param(resp=resp, expect_text=consts.RESP_BODY_504, text_split="'")

def test_server_name_and_available_methods():
    """ Тест, проверяющий что значение заголовков равны соответствующим значениям """

    chk.check_tag_in_header_equal_param(resp=resp, tag_name='server', tag_value='nginx')
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='access-control-allow-methods',
                                        tag_value=consts.ALLOW_METHODS)


def test_tags_in_headers():
    """ Тест, проверяющий, что в ответе сервера содержатся заголовки """

    chk.check_tag_in_headers(resp=resp, tags=('access-control-allow-credentials',
                                              'access-control-allow-headers', 'date', 'server',
                                              'access-control-allow-methods', 'access-control-allow-origin',))


def test_correct_params_in_link():
    """ Тест, проверяющий корректность переданных в запрос параметров """

    assert consts.LAYER in ('ozbasemap', 'pol'), 'Layer \'some\' is invalid.'
    assert consts.Z.isdigit(), 'Z is not digit'
    assert 0 <= int(consts.Z) <= 17, 'Z not in the interval from 0-17'
    assert consts.X.isdigit(), 'X is not digit'
    assert 0 <= int(consts.X) <= 2 ** (int(consts.Z) - 1), 'X not in the interval from 0-2^z-1'
    assert consts.Y.isdigit(), 'Y is not digit'
    assert 0 <= int(consts.Y) <= 2 ** (int(consts.Z) - 1), 'Y not in the interval from 0-2^z-1'
