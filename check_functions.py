def check_time_resp(resp, seconds):
    """ Функция, проверяющая, что время получения ответа от сервера меньше seconds """
    assert resp.elapsed.seconds < seconds, f'Response time more than {seconds}s'

def check_status_code(resp, code, message=''):
    """ Функция, проверяющая код ответа сервера """

    status = resp.status_code
    assert status == code, f'Server response statue is not equal {code}'


def check_tag_in_headers(resp, tags):
    """ Функция, проверяющая наличие тега в заголовках ответа сервера """

    for tag in tags:
        assert resp.headers.get(tag), f'Headers has not tag {tag}'


def check_tag_in_header_equal_param(resp, tag_name, tag_value):
    """ Функция, проверяющая что тег в заголовках ответа сервера равен определённому значению """

    assert resp.headers.get(tag_name) == tag_value, f'{tag_name} is not equal {tag_value}'

def check_response_body_equal_param(resp, expect_text, text_split):
    """ Функция, прооверяющая соответствует ли текст контента, который вернул сервер шаблонному тексту """

    # Получение текста контента, который вернул сервер
    resp_body = str(resp.content).split(text_split)[1]

    # Проверка, что текст контента равен шаблонной строке
    assert resp_body == expect_text, f'Response body is not such expected. This is: {resp_body}'

def check_application_json_equal_template(json_data, keys_in_json):
    """ Функция, проверяющая что структура json-файла, полученного от сервера соответствует шаблону """

    for dic in json_data:
        for key, type in keys_in_json.items():
            assert key in dic, f'Key "{key}" is not contains in Json Response'
            el_type = dic[key]
            assert isinstance(el_type, type), f'Type "{key}" must be {type}. Got {el_type}'