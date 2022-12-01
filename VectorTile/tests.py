import requests
from VectorTile.consts import LAYER, X, Y, Z, URL, RESP_BODY_500, ALLOW_METHODS


def check_status_code(code, message=''):
    """ Функция, проверяющая код ответа сервера """

    status = resp.status_code
    assert status == code, f'Server response statue is not equal {code}'


def check_tag_in_headers(*args):
    """ Функция, проверяющая наличие тега в заголовках ответа сервера """

    for tag in args:
        assert resp.headers.get(tag), f'Headers has not tag {tag}'


def check_tag_in_header_equal_param(tag_name, tag_value):
    """ Функция, проверяющая что тег в заголовках ответа сервера равен определённому значению """

    assert resp.headers.get(tag_name) == tag_value, f'{tag_name} is not equal {tag_value}'


def check_response_body_equal_param(expect_text, text_split):
    """ Функция, прооверяющая соответствует ли текст контента, который вернул сервер шаблонному тексту """

    # Получение текста контента, который вернул сервер
    resp_body = str(resp.content).split(text_split)[1]

    # Проверка, что текст контента равен шаблонной строке
    assert resp_body == expect_text, f'Response body is not such expected. This is: {resp_body}'


resp = requests.get(URL)  # GET-запрос на сервер


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

    check_status_code(code=200, message='OK - Binary tile successfully retrieved')
    check_tag_in_headers('etag', 'expires', 'content-encoding', 'content-encoding')
    check_tag_in_header_equal_param('content-type', 'application/x-protobuf')


def test_status_code204():
    """ Тест, проверяющий что код ответа сервера равен 200 и что в нём
            содержатся соответствующие заголовки
    """

    check_status_code(code=204, message='Undocumented')
    check_tag_in_headers(resp, 'expires', 'content-security-policy',
                         'cache-control', 'access-control-allow-private-network')


def test_status_code304():
    """ Тест, проверяющий что код ответа сервера равен 304 """

    check_status_code(code=304,
                      message='The resource cached in the client (identified by the if-none-match) header has not changed.')


def test_status_code400():
    """ Тест, проверяющий что код ответа сервера равен 400 """

    check_status_code(code=400, message='''
                                    Possible messages due to request URI validation error.

                                    1) Layer 'some' is invalid.
                                    2) Zoom level 100 is invalid. Accepted zoom levels are - [1-17].
                                '''
                      )
    check_tag_in_header_equal_param('content-type', 'application/json')


def test_status_code401():
    """ Тест, проверяющий что код ответа сервера равен 401 """

    check_status_code(code=401, message='Access token is missing or invalid.')
    check_tag_in_header_equal_param('content-type', 'application/json')


def test_status_code404():
    """ Тест, проверяющий что код ответа сервера равен 404 """

    check_status_code(404)
    check_response_body_equal_param(expect_text=f'Function source \'{LAYER}\' not found', text_split='"')


def test_status_code500():
    """ Тест, проверяющий что код ответа сервера равен 500 """

    check_status_code(500)
    check_response_body_equal_param(expect_text=RESP_BODY_500, text_split="'")
    check_tag_in_header_equal_param('content-type', 'text/html; charset=UTF-8')


def test_tag_equal_value():
    """ Тест, проверяющий что значение заголовков равны соответствующим значениям """

    check_tag_in_header_equal_param('server', 'nginx')
    check_tag_in_header_equal_param('access-control-allow-methods', ALLOW_METHODS)


def test_tags_in_headers_():
    """ Тест, проверяющий, что в ответе сервера содержатся заголовки """

    check_tag_in_headers(resp, 'access-control-allow-credentials',
                         'access-control-allow-headers', 'date', 'server',
                         'access-control-allow-methods', 'access-control-allow-origin')


def test_correct_params_in_link():
    """ Тест, проверяющий корректность переданных в запрос параметров """

    assert LAYER in ('ozbasemap', 'pol'), 'Layer \'some\' is invalid.'
    assert Z.isdigit(), 'Z is not digit'
    assert 0 <= int(Z) <= 17, 'Z not in the interval from 0-17'
    assert X.isdigit(), 'X is not digit'
    assert 0 <= int(X) <= 2 ** (int(Z) - 1), 'X not in the interval from 0-2^z-1'
    assert Y.isdigit(), 'Y is not digit'
    assert 0 <= int(Y) <= 2 ** (int(Z) - 1), 'Y not in the interval from 0-2^z-1'
