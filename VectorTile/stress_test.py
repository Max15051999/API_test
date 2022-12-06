from locust import HttpUser, task, between
from random import randint


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def Vector_Tile_API(self):

        layer = 'ozbasemap'
        z = randint(0, 17) # Зум (от 0 до 17 включительно)
        x = randint(0, 2 ** (z - 1)) # Координата X (от 0 до 2^z-1 включительно)
        y = randint(0, 2 ** (z - 1)) # Координата Y (от 0 до 2^z-1 включительно)

        self.client.get(f'/api/tiles/{layer}/{z}/{x}/{y}.pbf')

    def on_start(self):
        self.client.get('/')