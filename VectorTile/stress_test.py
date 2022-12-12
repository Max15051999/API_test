from locust import HttpUser, task, between
from VectorTile.consts import URIS_FOR_OZBASEMAP, URIS_FOR_POI

# URL: https://maps.starline.ru

# locust -f VectorTile/stress_test.py --host https://maps.starline.ru
# -u - user's amount# --headless - start without graphical interface

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    URI_OZBASEMAP_NUMBER = 0 # Номер URI для ozbasemap в кортеже
    URI_POI_NUMBER = 0 # Номер URI для poi в кортеже

    @task
    def ozbasemap_api(self):
        """ Нагрузочный тест для ozbasemap """

        # GET-запрос виртуального пользователя
        self.client.get(f'/api/tiles/{URIS_FOR_OZBASEMAP[QuickstartUser.URI_OZBASEMAP_NUMBER]}')

        QuickstartUser.URI_OZBASEMAP_NUMBER += 1

        if QuickstartUser.URI_OZBASEMAP_NUMBER == len(URIS_FOR_OZBASEMAP):
            QuickstartUser.URI_OZBASEMAP_NUMBER = 0

    @task
    def poi_api(self):
        """ Нагрузочный тест для poi """
        # GET-запрос виртуального пользователя
        self.client.get(f'/api/tiles/{URIS_FOR_POI[QuickstartUser.URI_POI_NUMBER]}')

        QuickstartUser.URI_POI_NUMBER += 1

        if QuickstartUser.URI_POI_NUMBER == len(URIS_FOR_POI):
            QuickstartUser.URI_POI_NUMBER = 0

    def on_start(self):
        self.client.get('/')