import math
from pathlib import Path
from locust import LoadTestShape, between, task
from locust.contrib.fasthttp import FastHttpUser
import random

testing_urls = Path('sitemap.txt').read_text().splitlines()


class WebUser(FastHttpUser):

    @task
    def load_test(self):
        url = random.choice(testing_urls)
        self.client.get(url)
