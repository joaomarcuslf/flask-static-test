#!/usr/bin/python3

import urllib.request

pages = {
    'health': '/health',
    'index': '/',
    'report': '/report',
}

base_url = "http://127.0.0.1:5000"

for page in pages:
    print(base_url + pages[page])
    urllib.request.urlretrieve(
        base_url + pages[page],
        page + ".html"
    )