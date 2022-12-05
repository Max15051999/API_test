QUERY = 'углово' # Строка запроса
TYPE = 'address' # address or poi
MAPPING_KEY = '' # Конкретезирует poi поиск
SUBCLASS = '' # Конкретезирует poi поиск
FORWARD_LAT = None # Широта для запроса FORWARD_URL
FORWARD_LON = None # Долгота для запроса FORWARD_URL

REVERSE_LAT = 60.0690540450461 # Широта для запроса REVERSE_URL
REVERSE_LON = 30.7383083316701 # # Долгота для запроса REVERSE_URL
RADIUS = None # Радиус, в котором будет производиться поиск
SIGNS_ONLY = None # Накладывает на выдачу ограничение, при котором выдаются только дорожные знаки

FORWARD_URL = 'http://maps.starline.ru/api/geocoder/v1/forward'
REVERSE_URL = 'http://maps.starline.ru/api/geocoder/v1/reverse'

# Словари параметров, передаваемых в запрос
DICT_FORWARD_PARAMS = dict()
DICT_REVERSE_PARAMS = dict()

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
if RADIUS:
    DICT_REVERSE_PARAMS['radius'] = RADIUS
if SIGNS_ONLY:
    DICT_REVERSE_PARAMS['sings_only'] = SIGNS_ONLY

KEYS_TYPES_IN_JSON_CODE_200 = {'id': int, 'lat': float, 'lon': float, 'city': str, 'name': str, 'type': str, 'osm_id': int,
                         'name_en': str, 'name_ru': str, 'quarter': str, 'distance': float, 'postcode': int,
                         'subclass': str, 'housenumber': str, 'mapping_key': str
                         }

ALLOW_METHODS = 'GET, POST, PUT, DELETE, OPTIONS'
