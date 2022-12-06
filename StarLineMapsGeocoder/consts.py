QUERY = 'Moscow' # Строка запроса
TYPE = 'address' # address or poi
MAPPING_KEY = '' # Конкретезирует poi поиск
SUBCLASS = '' # Конкретезирует poi поиск
FORWARD_LAT = None # Широта для запроса FORWARD_URL
FORWARD_LON = None # Долгота для запроса FORWARD_URL

REVERSE_LAT = 60.0690540450461 # Широта для запроса REVERSE_URL
REVERSE_LON = 30.7383083316701 # # Долгота для запроса REVERSE_URL

REVERSE_RADIUS = None # Радиус, в котором будет производиться поиск для REVERSE_URL
SIGNS_ONLY = None # Накладывает на выдачу ограничение, при котором выдаются только дорожные знаки

TOW_AWAY_ZONE_LAT = None # Широта для запроса TOW_AWAY_ZONE_URL
TOW_AWAY_ZONE_LON = None # Долгота для запроса TOW_AWAY_ZONE_URL
TOW_AWAY_ZONE_RADIUS = None # Радиус для запроса TOW_AWAY_ZONE_URL
TOW_AWAY_ZONE_SIGN = None

# API's URL
FORWARD_URL = 'http://maps.starline.ru/api/geocoder/v1/forward'
REVERSE_URL = 'http://maps.starline.ru/api/geocoder/v1/reverse'
TOW_AWAY_ZONE_URL = 'http://maps.starline.ru/api/geocoder/v1/tow_away_zone'

# Словари параметров, передаваемых в запрос для различных URL
DICT_FORWARD_PARAMS = dict() # Для FROWARD_URL
DICT_REVERSE_PARAMS = dict() # Для REVERSE_URL
DICT_TOW_AWAY_ZONE_PARAMS = dict() # Для TOW_AWAY_ZONE_URL

# Заполнение словаря параметров для FORWARD_URL
if QUERY:
    DICT_FORWARD_PARAMS['query'] = QUERY
if TYPE:
    DICT_FORWARD_PARAMS['type'] = TYPE
if MAPPING_KEY:
    DICT_FORWARD_PARAMS['mapping_key'] = MAPPING_KEY
if SUBCLASS:
    DICT_FORWARD_PARAMS['subclass'] = SUBCLASS
if FORWARD_LAT:
    DICT_FORWARD_PARAMS['lat'] = FORWARD_LAT
if FORWARD_LON:
    DICT_FORWARD_PARAMS['lon'] = FORWARD_LON

# Заполнение словаря параметров для REVERSE_URL
if REVERSE_LAT:
    DICT_REVERSE_PARAMS['lat'] = REVERSE_LAT
if REVERSE_LON:
    DICT_REVERSE_PARAMS['lon'] = REVERSE_LON
if REVERSE_RADIUS:
    DICT_REVERSE_PARAMS['radius'] = REVERSE_RADIUS
if SIGNS_ONLY:
    DICT_REVERSE_PARAMS['sings_only'] = SIGNS_ONLY

# Заполнение словаря параметров для TOW_AWAY_ZONE_URL
if TOW_AWAY_ZONE_LAT:
    DICT_TOW_AWAY_ZONE_PARAMS['lat'] = TOW_AWAY_ZONE_LAT
if TOW_AWAY_ZONE_LON:
    DICT_TOW_AWAY_ZONE_PARAMS['lon'] = TOW_AWAY_ZONE_LON
if TOW_AWAY_ZONE_RADIUS:
    DICT_TOW_AWAY_ZONE_PARAMS['radius'] = TOW_AWAY_ZONE_RADIUS
if TOW_AWAY_ZONE_SIGN:
    DICT_TOW_AWAY_ZONE_PARAMS['sign'] = TOW_AWAY_ZONE_SIGN

KEYS_TYPES_IN_FORWARD_REVERSE_JSON_CODE_200 = {
                            'id': int,
                            'lat': float,
                            'lon': float,
                            'city': str,
                            'name': str,
                            'type': str,
                            'osm_id': int,
                            'name_en': str,
                            'name_ru': str,
                            'quarter': str,
                            'distance': float,
                            'postcode': int,
                            'subclass': str,
                            'housenumber': str,
                            'mapping_key': str
                    } # Словарь ключей и их параметров, ожидаемых в json-файле для FORWARD_URL или REVERSE_URL

KEYS_TYPES_IN_TOW_AWAY_ZONE_JSON_CODE_200 = {
        'side': str,
        'type': str,
        'distance': str,
        'direction': str,
        'evacuation': bool,
        'coordinates': list,
        'related_road': int
} # Тело ответов сервера при разном коде ответа

RESP_MESSAGE_400 = '400 Bad Request'
RESP_DESCRIPTION_400 = 'Coordinates must be float'

RESP_MESSAGE_404 = '404 Not Found'
RESP_DESCRIPTION_404 = 'Missing parameters: lat,lon'

RESP_MESSAGE_500 = '500 Internal Server Error'
RESP_DESCRIPTION_500 = 'The server encountered an unexpected condition which prevented it from fulfilling the request.'

# Доступные методы
ALLOW_METHODS = 'GET, POST, PUT, DELETE, OPTIONS'
