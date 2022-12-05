LAYER = 'ozbasemap'  # Valid: ozbasemap, pol
Z = '17'  # Valid: 0-17
X = '19044'  # Valid: 0-2^z-1
Y = '38293'  # Valid: 0-2^z-1

URL = f'https://maps.starline.ru/api/tiles/{LAYER}/{Z}/{X}/{Y}.pbf'

KEYS_TYPES_IN_JSON_CODE_400 = {'code': str, 'status': int, 'cause': str,
                               'correlationId': str, 'title': str, 'action': str
                               }

KEYS_TYPES_IN_JSON_CODE_401 = {'error': str, 'error_description': str}

RESP_BODY_500 = '<html><title>500: Internal Server Error</title><body>500: Internal Server Error</body></html>'
RESP_BODY_504 = '<html><head><title>504 Gateway Time-out</title></head><body><center><h1>504 Gateway ' \
                'Time-out</h1></center><hr><center>nginx</center></body></html> '
ALLOW_METHODS = 'GET, OPTIONS, GET, POST, PUT, DELETE, OPTIONS'
