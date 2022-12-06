from locust import HttpUser, task, between
import StarLineMapsGeocoder.consts as consts


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def Geocoder_V1_API(self):
        self.client.get(consts.FORWARD_URL, params={
            'query': consts.QUERY,
            'type': consts.TYPE,
            'mapping_key': consts.MAPPING_KEY,
            'subclass': consts.SUBCLASS,
            'lat': consts.FORWARD_LAT,
            'lon': consts.FORWARD_LON,
        })

    def on_start(self):
        self.client.get('/')