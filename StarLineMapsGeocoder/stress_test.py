from locust import HttpUser, task, between
from VectorTile.consts import LAYER, X, Y, Z


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def Vector_Tile_API(self):
        self.client.get(f'/api/tiles/{LAYER}/{Z}/{X}/{Y}.pbf')

    def on_start(self):
        self.client.get('/')