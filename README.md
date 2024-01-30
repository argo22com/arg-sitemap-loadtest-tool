# Load test a website using random URLs from a sitemap

## Getting started

```sh
# Create and activate virtualenv
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Download sitemap for a website
```shell
python sitemap_download.py https://www.example.com/
```

### Start the web ui for the load test

The UI is available at [http://localhost:8089](http://localhost:8089)

```sh
make test

# press ctrl+c to exit
```
### Controls 

The "User" in the current configuration will attempt to access one page from the sitemap every 5 seconds.

To adjust the load, you can change the number of users. For example, if you set the number of users to 100, you'll get RPS of about 20.

You can change the number of users during the test:
- in the Web UI, click "Edit" in the top menu
- in the CLI, press w or W to increase the number of users by 1 or 10 respectively, or s or S to decrease the number of users by 1 or 10 respectively


### How to read the results

The test collects the following key metrics:
- Median (ms) - the median (50th percentile) response time, ie 50% of requests were faster than this
- 95%ile (ms) - the 95th percentile response time - this is what majority of users will experience, excluding outliers
- RPS - requests per second

The Charts tab will be the most useful for understanding the performance characteristics of the site. 
You should ramp up the number of users until you see:
- the response time start to increase significantly
- or, the RPS start to decrease significantly

That will be the maximum number of users your site can handle given the current setup.

The Statistics tab will show you the median and 95th percentile response times for each URL. This could help you find the slowest URLs on your site.