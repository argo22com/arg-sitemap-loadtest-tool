## Create and source venv

python -m venv venv && source venv/bin/activate

## Install dependencies

pip install -r requirements.txt

## Download sitemap

python sitemap_download.py https://www.example.com/

## Run locust

locust
