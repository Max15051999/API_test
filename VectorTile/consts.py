LAYER = 'ozbasemap'  # Valid: ozbasemap, pol
Z = '17'  # Valid: 0-17
X = '19044'  # Valid: 0-2^z-1
Y = '38293'  # Valid: 0-2^z-1

URL = f'https://maps.starline.ru/api/tiles/{LAYER}/{Z}/{X}/{Y}.pbf'

RESP_BODY_500 = '<html><title>500: Internal Server Error</title><body>500: Internal Server Error</body></html>'
ALLOW_METHODS = 'GET, OPTIONS, GET, POST, PUT, DELETE, OPTIONS'