import requests
import check_functions as chk

resp = requests.get('https://maps.starline.ru/api/geocoder/v2/metrics')  # GET-запрос на сервер

print(resp.status_code)
print(resp.headers)
print(resp.content)
print(resp.json())

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

