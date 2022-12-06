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
