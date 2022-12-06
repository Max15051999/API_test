import requests
import check_functions as chk
import SphinxsearchGeocoder.consts as consts

resp = requests.get(consts.METRICS_URL)  # GET-запрос на сервер

def test_time_response():
    """ Тест, проверяющий, что время получения ответа от сервера меньше 1-ой секунды """

    chk.check_time_resp(resp=resp, seconds=1)

def test_status_code200():
    """ Тест, проверяющий что код ответа сервера равен 200,
        а также его заголовки и тело ответа
    """

    # Проверка кода ответа сервера
    chk.check_status_code(resp=resp, code=200, message='')

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type',
                                        tag_value='application/json')


def test_tag_equal_value():
    """ Тест, проверяющий что значение заголовков равны соответствующим значениям """

    # Проверка соответствия заголовков ответа сервера определённым значениям
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='server', tag_value='nginx')
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='access-control-allow-methods',
                                        tag_value=consts.ALLOW_METHODS)

    # Проверка, что длина данных в теле ответа не равна 0
    assert len(resp.content) != 0


def test_tags_in_headers():
    """ Тест, проверяющий, что в ответе сервера содержатся заголовки """

    # Проверка наличия определённых тегов в заголовках ответа сервера
    chk.check_tag_in_headers(resp=resp, tags=('access-control-allow-credentials',
                                              'access-control-allow-headers', 'date', 'server',
                                              'access-control-allow-methods', 'access-control-allow-origin',))