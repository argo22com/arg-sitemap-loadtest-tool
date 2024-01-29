import math
from pathlib import Path
from locust import LoadTestShape, between, task
from locust.contrib.fasthttp import FastHttpUser
from random import shuffle

testing_urls = Path('sitemap.txt').read_text().splitlines()


class WebUser(FastHttpUser):
    urls = testing_urls
    shuffle(urls)
    last_index = 0

    def get_random_url(self):
        if self.last_index >= len(self.urls):
            self.last_index = 0
        return self.urls[self.last_index]

    @task
    def load_test(self):
        url = self.get_random_url()
        self.last_index += 1
        self.client.get(url)


# You can define custom load shape
class StepLoadShape(LoadTestShape):
    """
    A step load shape
    Keyword arguments:
        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds
    """

    step_time = 60
    step_load = 10
    spawn_rate = 1
    time_limit = 86400 # 24h

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)
