from locust import HttpUser, task, between
import StarLineMapsGeocoder.consts as consts


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def Geocoder_V1_API(self):
        self.client.get(consts.REVERSE_URL, params={
            'lat': consts.REVERSE_LAT,
            'lon': consts.REVERSE_LON,
            'radius': consts.REVERSE_RADIUS,
            'sings_only': consts.SIGNS_ONLY,
        })

    def on_start(self):
        self.client.get('/')