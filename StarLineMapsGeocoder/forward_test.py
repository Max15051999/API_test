import requests
import StarLineMapsGeocoder.consts as consts
import check_functions as chk
from StarLineMapsGeocoder import same_func

resp = requests.get(consts.FORWARD_URL, params=consts.DICT_FORWARD_PARAMS)  # GET-запрос на сервер

# print('Status code:', resp.status_code)
# print('Headers:', resp.headers)
print(resp.json() == consts.JSON_CODE_400)

def test_time_response():
    """ Тест, проверяющий, что время получения ответа от сервера меньше 1-ой секунды """

    chk.check_time_resp(resp=resp, seconds=1)

def test_status_code200():
    """ Тест, проверяющий что код ответа сервера равен 200,
        а также его заголовки и тело ответа
    """

    chk.check_status_code(resp=resp, code=200, message='')

    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type',
                                        tag_value='application/json')

    json_data = resp.json()

    with open(file='json_data.log', mode='w', encoding='UTF-8') as ff:
        ff.write(str(json_data))

    if json_data:

        chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-encoding',
                                            tag_value='br')

        chk.check_application_json_equal_template(json_data=json_data,
                                                  keys_in_json=consts.KEYS_TYPES_IN_JSON_CODE_200)
    else:
        chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-length', tag_value='4')

def test_status_code400():
    """ Тест, проверяющий что код ответа сервера равен 400,
            а также его заголовки и тело ответа
    """

    chk.check_status_code(resp=resp, code=400)
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/json')
    chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-length', tag_value='513')

    assert resp.json() == same_func.resp_json_with_code_400_or_500(message='400 Bad Request',
                                                                description='Type must be "address" or "poi"')


def test_tag_equal_value():
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

    assert consts.TYPE in ('address', 'poi'), f'type must be "address" or "poi". Got {consts.TYPE}'
