import random
from pathlib import Path

from locust import task, constant_throughput
from locust.contrib.fasthttp import FastHttpUser

testing_urls = Path('sitemap.txt').read_text().splitlines()


class WebUser(FastHttpUser):
    host = testing_urls[0]

    """
    0.2 = task runs at most 0.2 times per second, i.e. once every 5 seconds on average
    
    @see https://docs.locust.io/en/stable/writing-a-locustfile.html#wait-time-attribute
    """
    wait_time = constant_throughput(0.2)

    @task
    def load_test(self):
        url = random.choice(testing_urls)
        self.client.get(url)
