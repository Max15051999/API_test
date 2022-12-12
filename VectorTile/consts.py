LAYER = 'poi'  # Valid: ozbasemap, poi
Z = '17'  # Valid: 0-17
X = '19044'  # Valid: 0-2^z-1
Y = '38293'  # Valid: 0-2^z-1

URL = f'https://maps.starline.ru/api/tiles/{LAYER}/{Z}/{X}/{Y}.pbf'

KEYS_TYPES_IN_JSON_CODE_400 = {'code': str, 'status': int, 'cause': str,
                               'correlationId': str, 'title': str, 'action': str
                               }

KEYS_TYPES_IN_JSON_CODE_401 = {'error': str, 'error_description': str}

ALLOW_METHODS = 'GET, OPTIONS, GET, POST, PUT, DELETE, OPTIONS'

# Кортеж URI для тестирования ответа сервера с уровнем OZBASEMAP
URIS_FOR_OZBASEMAP = (
    'ozbasemap/0/0/0.pbf',
    'ozbasemap/1/1/1.pbf',
    'ozbasemap/2/1/0.pbf',
    'ozbasemap/3/4/1.pbf',
    'ozbasemap/4/9/5.pbf',
    'ozbasemap/5/18/10.pbf',
    'ozbasemap/6/37/17.pbf',
    'ozbasemap/7/74/36.pbf',
    'ozbasemap/8/149/73.pbf',
    'ozbasemap/9/299/148.pbf',
    'ozbasemap/10/598/297.pbf',
    'ozbasemap/11/1197/595.pbf',
    'ozbasemap/12/2716/1378.pbf',
    'ozbasemap/13/5434/2759.pbf',
    'ozbasemap/14/10868/5516.pbf',
    'ozbasemap/15/21737/11033.pbf',
    'ozbasemap/16/43474/22066.pbf',
    'ozbasemap/17/19044/38293.pbf',
)

# Кортеж URI для тестирования ответа сервера с уровнем POI
URIS_FOR_POI = (
    'poi/11/1196/594.pbf',
    'poi/12/2392/1190.pbf',
    'poi/13/4562/2601.pbf',
    'poi/14/9124/5203.pbf',
    'poi/15/18249/10407.pbf',
    'poi/16/36499/20816.pbf',
    'poi/17/72997/41633.pbf',
)
