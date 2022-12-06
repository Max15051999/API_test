def check_time_resp(resp, seconds):
    """
    Функция, проверяющая, что время получения ответа от сервера меньше seconds

    :param resp: Ответ сервера
    :param seconds: Максимальное время в секундах, за которое сервер должен дать ответ

    """

    assert resp.elapsed.seconds < seconds, f'Response time more than {seconds}s'

def check_status_code(resp, code, message=''):
    """
    Функция, проверяющая код ответа сервера

    :param resp: Ответ сервера
    :param code: Ожидаемый код ответа сервера
    :param message: Сообщение, выводимое при совпадении реального кода ответа сервера с ожидаемым
    """

    status = resp.status_code
    assert status == code, f'Server response statue is not equal {code}'


def check_tag_in_headers(resp, tags):
    """
    Функция, проверяющая наличие тега в заголовках ответа сервера

    :param resp: Ответ сервера
    :param tags: Набор тегов, которые должны содержаться в заголовках ответа сервера

    """

    for tag in tags:
        assert resp.headers.get(tag), f'Headers has not tag {tag}'


def check_tag_in_header_equal_param(resp, tag_name, tag_value):
    """
    Функция, проверяющая что тег в заголовках ответа сервера равен определённому значению

    :param resp: Ответ сервера
    :param tag_name: Название тега, который должен содержаться в заголовках ответа сервера
    :param tag_value: Значение, которому должен равняться данный тег

    """

    assert resp.headers.get(tag_name) == tag_value, f'{tag_name} is not equal {tag_value}'

def check_response_body_equal_param(resp, expect_text, text_split):
    """
    Функция, прооверяющая соответствует ли текст контента, который вернул сервер шаблонному тексту

    :param resp: Ответ сервера
    :param expected_text: Текст, который должен содержаться в теле ответа сервера
    :param text_split: Символ, по которому будет разбиваться текст, полученный от сервера

    """

    # Получение текста контента, который вернул сервер
    resp_body = str(resp.content).split(text_split)[1]

    # Проверка, что текст контента равен шаблонной строке
    assert resp_body == expect_text, f'Response body is not such expected. This is: {resp_body}'

def check_application_json_equal_template(json_data, keys_in_json):
    """
    Функция, проверяющая что структура json-файла, полученного от сервера соответствует шаблону

    :param json_data: json-файл
    :param keys_in_json: ключи и их типы, которые должны содержаться в json

    """

    for dic in json_data:
        for key, type in keys_in_json.items():
            assert key in dic, f'Key "{key}" is not contains in Json Response'
            el_type = dic[key]
            assert isinstance(el_type, type), f'Type "{key}" must be {type}. Got {el_type}'

def check_resp_json(resp, message, description):
    """
    Функция, сравнивающая структуру json-файла, который вернул сервер с заданной структурой

    :param resp: Ответ сервера
    :param message: Сообщение о деталях статуса в json-файле
    :param description: Описание деталей статуса в json-файле

    """

    assert resp.json() == {
        'status': 'Failure', 'status_details': {
            'message': message, 'description': description
        }
    }

