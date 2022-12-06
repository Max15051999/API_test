QUERY = 'Moscow' # Строка запроса
LAT = None # Широта
LON = None # Долгота
OBJECT_TYPE = None # Тип объекта (poi, street,city)
RESPONSE = None

# API's URL
METRICS_URL = 'https://maps.starline.ru/api/geocoder/v2/metrics'
FORWARD_URL = 'https://maps.starline.ru/api/geocoder/v2/forward'

# Словари параметров, передаваемых в запрос для различных URL
DICT_FORWARD_PARAMS = dict() # Для FROWARD_URL

# Заполнение словаря параметров для FORWARD_URL
if QUERY:
    DICT_FORWARD_PARAMS['query'] = QUERY
if LAT:
    DICT_FORWARD_PARAMS['lat'] = LAT
if LON:
    DICT_FORWARD_PARAMS['lon'] = LON
if OBJECT_TYPE:
    DICT_FORWARD_PARAMS['object_type'] = OBJECT_TYPE
if RESPONSE:
    DICT_FORWARD_PARAMS['response'] = RESPONSE


KEYS_TYPES_IN_FORWARD_REVERSE_JSON_CODE_200 = {
                        'osm_id': int,
                        'osm_type': str,
                        'object_type': str,
                        'lat': float,
                        'lon': float,
                        'display_name': str,
                        'address': {
                            'name': str,
                            'house_number': str,
                            'street': str,
                            'city': str,
                            'city_type': str,
                            'district': str,
                            'region': str,
                            'postcode': str,
                            'country': str
                        },
                        'distance': None
  } # Тело ответов сервера при разном коде ответа

# Доступные методы
ALLOW_METHODS = 'GET, POST, PUT, DELETE, OPTIONS'