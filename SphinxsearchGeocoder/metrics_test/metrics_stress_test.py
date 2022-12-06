from locust import HttpUser, task, between
import SphinxsearchGeocoder.consts as consts


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def Geocoder_V2_API(self):
        self.client.get(consts.METRICS_URL)

    def on_start(self):
        self.client.get('/')