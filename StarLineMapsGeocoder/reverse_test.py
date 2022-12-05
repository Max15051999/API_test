import requests
import StarLineMapsGeocoder.consts as consts
import check_functions as chk
import same_func

resp = requests.get(consts.REVERSE_URL, params=consts.DICT_REVERSE_PARAMS)  # GET-запрос на сервер

def test_time_response():
    """ Тест, проверяющий, что время получения ответа от сервера меньше 1-ой секунды """

    chk.check_time_resp(resp=resp, seconds=1)

# def test_status_code200():
#     """ Тест, проверяющий что код ответа сервера равен 200,
#         а также его заголовки и тело ответа
#     """
#
#     chk.check_status_code(resp=resp, code=200, message='')
#     chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-type', tag_value='application/json')
#
#     json_data = resp.json()
#
#     with open(file='json_data.log', mode='w', encoding='UTF-8') as ff:
#         ff.write(str(json_data))
#
#     if json_data:
#
#         chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-encoding',
#                                             tag_value='br')
#
#         for dic in json_data:
#             for key, type in consts.KEYS_TYPES_IN_JSON_CODE_200.items():
#                 assert key in dic, f'Key "{key}" is not contains in Json Response'
#                 el_type = dic[key]
#                 assert isinstance(el_type, type), f'Type "{key}" must be {type}. Got {el_type}'
#     else:
#         chk.check_tag_in_header_equal_param(resp=resp, tag_name='content-length', tag_value='4')

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

def test_status_code_500():
    """ Тест, проверяющий, что ответ сервера равен 500 """

    assert resp.json() == same_func.resp_json_with_code_400_or_500(message='500 Internal Server Error',
                                          description='The server encountered an unexpected condition which prevented it from fulfilling the request.')
