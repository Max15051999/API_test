import requests
import VectorTile.consts as consts
import resp_body_consts as rbc
import check_functions as chk
from time import sleep

resp = requests.get(consts.URL)  # GET-запрос на сервер

def test_time_response():
    """ Тест, проверяющий, что время получения ответа от сервера меньше 1-ой секунды """

    chk.check_time_resp(resp=resp, seconds=1)


def test_status_code200():
    """ Тест, проверяющий что код ответа сервера равен 200 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=200, message='OK - Binary tile successfully retrieved')

    # Проверка наличия определённых тегов в заголовках ответа сервера
    chk.check_tag_in_headers(resp=resp,
                             tags=('etag', 'expires', 'last-modified', 'content-encoding',))

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/x-protobuf')
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-encoding', tag_value='br')


def test_status_code204():
    """ Тест, проверяющий что код ответа сервера равен 204 и что в нём
            содержатся соответствующие заголовки
    """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=204, message='Undocumented')

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/json')

    # Проверка что в теле ответа нет данных
    assert len(resp.content) == 0, 'Length of data is not 0'
    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_headers(resp=resp, tags=('expires', 'content-security-policy',
                                              'cache-control', 'access-control-allow-private-network',))


def test_status_code304():
    """ Тест, проверяющий что код ответа сервера равен 304 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=304,
                          message='The resource cached in the client (identified by the if-none-match) header has not '
                                  'changed.')


def test_status_code400():
    """ Тест, проверяющий что код ответа сервера равен 400 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=400, message='''
                                    Possible messages due to request URI validation error.

                                    1) Layer 'some' is invalid.
                                    2) Zoom level 100 is invalid. Accepted zoom levels are - [1-17].
                                '''
                          )

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/json')

    # Получение json-файла от сервера
    json_data = resp.json()

    # Проверка соответствия структуры полученного json-файла заданной структуре
    chk.check_application_json_equal_template(json_data=json_data,
                                              keys_in_json=consts.KEYS_TYPES_IN_JSON_CODE_400)


def test_status_code401():
    """ Тест, проверяющий что код ответа сервера равен 401 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=401, message='Access token is missing or invalid.')

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/json')

    # Получение json-файла от сервера
    json_data = resp.json()

    # Проверка соответствия структуры полученного json-файла заданной структуре
    chk.check_application_json_equal_template(json_data=json_data,
                                              keys_in_json=consts.KEYS_TYPES_IN_JSON_CODE_401)


def test_status_code404():
    """ Тест, проверяющий что код ответа сервера равен 404 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=404)

    # Проверка соответствия тела ответа сервера шаблонной строке
    chk.check_response_body_equal_param(resp=resp, expect_text=f'Function source \'{consts.LAYER}\' not found',
                                        text_split='"')


def test_status_code500():
    """ Тест, проверяющий, что код ответа сервера равен 500 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=500)

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='text/html; charset=UTF-8')

    # Проверка соответствия тела ответа сервера шаблонной строке
    chk.check_response_body_equal_param(resp=resp, expect_text=rbc.RESP_BODY_500, text_split="'")

def test_status_code504():
    """ Тест, проверяющий, что код ответа сервера равен 504 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=504)

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='text/html; charset=UTF-8')
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-length', tag_value='562')

    # Проверка соответствия тела ответа сервера шаблонной строке
    chk.check_response_body_equal_param(resp=resp, expect_text=rbc.RESP_BODY_504, text_split="'")

def test_server_name_and_available_methods():
    """ Тест, проверяющий что значение заголовков равны соответствующим значениям """

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='server', tag_value='nginx')
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='access-control-allow-methods',
                                        tag_value=consts.ALLOW_METHODS)


def test_tags_in_headers():
    """ Тест, проверяющий, что в ответе сервера содержатся заголовки """

    # Проверка наличия определённых тегов в заголовках ответа сервера
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

def test_resp_ozbasemap_on_all_zoom_levels():
    """ Тест, проверяющий ответ сервера с параметром ozbasemap на всех уровнях зума """

    for uri in consts.URIS_FOR_OZBASEMAP:
        r = requests.get(f'https://maps.starline.ru/api/tiles/{uri}')

        # with open(file='resp.txt', mode='a', encoding='UTF-8') as ff:
        #     ff.write(f'https://maps.starline.ru/api/tiles/{uri}')

        # Проверка, что статус ответа сервера равен 200
        chk.check_status_code(resp=r, code=200, message='OK - Binary tile successfully retrieved')

        # Проверка, что в заголовках ответа сервера содержатся заголовки
        # chk.check_tag_in_headers(resp=r, tags=('etag', 'expires', 'last-modified', 'content-encoding',))

        # Проверка, что определённые заголовки ответа сервера равны определённым значениям
        chk.check_tag_in_header_equal_param(resp=r, tag_name='content-type', tag_value='application/x-protobuf')
        # chk.check_tag_in_header_equal_param(resp=r, tag_name='content-encoding', tag_value='br')

def test_resp_poi_on_all_zoom_levels():
    """ Тест, проверяющий ответ сервера с параметром poi на всех уровнях зума """

    for uri in consts.URIS_FOR_POI:
        r = requests.get(f'https://maps.starline.ru/api/tiles/{uri}')

        # with open(file='resp.txt', mode='a', encoding='UTF-8') as ff:
        #     ff.write(f'https://maps.starline.ru/api/tiles/{uri}')

        # Проверка, что статус ответа сервера равен 200
        chk.check_status_code(resp=r, code=200, message='OK - Binary tile successfully retrieved')

        # Проверка, что в заголовках ответа сервера содержатся заголовки
        # chk.check_tag_in_headers(resp=r, tags=('etag', 'expires', 'last-modified', 'content-encoding',))

        # Проверка, что определённые заголовки ответа сервера равны определённым значениям
        chk.check_tag_in_header_equal_param(resp=r, tag_name='content-type', tag_value='application/x-protobuf')
        # chk.check_tag_in_header_equal_param(resp=r, tag_name='content-encoding', tag_value='br')
