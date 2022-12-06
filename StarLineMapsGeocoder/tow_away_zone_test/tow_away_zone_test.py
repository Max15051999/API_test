import requests
import StarLineMapsGeocoder.consts as consts
import check_functions as chk

resp = requests.get(consts.TOW_AWAY_ZONE_URL,
                    params=consts.DICT_TOW_AWAY_ZONE_PARAMS)  # GET-запрос на сервер

def test_time_response():
    """ Тест, проверяющий, что время получения ответа от сервера меньше 1-ой секунды """

    chk.check_time_resp(resp=resp, seconds=1)


def test_status_code200():
    """ Тест, проверяющий что код ответа сервера равен 200 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=200, message='')

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type',
                                        tag_value='application/json')

    # Получение json-файла от сервера
    json_data = resp.json()

    if json_data:  # Если json не null

        chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-encoding',
                                            tag_value='br')

        # Проверка соответствия структуры полученного json-файла заданной структуре
        chk.check_application_json_equal_template(json_data=json_data,
                                                  keys_in_json=consts.KEYS_TYPES_IN_TOW_AWAY_ZONE_JSON_CODE_200)
    else:
        chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-length', tag_value='4')

def test_status_code404():
    """ Тест, проверяющий что код ответа сервера равен 404 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=404)

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/json')
    # chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-encoding', tag_value='br')

    params = ''

    if not consts.TOW_AWAY_ZONE_LAT:
        params += 'lat,'
    if not consts.TOW_AWAY_ZONE_LON:
        params += 'lon,'
    if not consts.TOW_AWAY_ZONE_SIGN:
        params += 'sign'

    chk.check_resp_json(
        resp=resp,
        message='404 Not Found',
        description=f'Missing parameters: {params}'
)

def test_status_code500():
    """ Тест, проверяющий что код ответа сервера равен 400 """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=400)

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/json')
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-length', tag_value='513')

    # Проверка соответствия стуктуры полученного от сервера json-файла заданной структуре
    chk.check_resp_json(
        resp=resp,
        message=consts.RESP_MESSAGE_500,
        description=consts.RESP_DESCRIPTION_500
    )


def test_tag_equal_value():
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