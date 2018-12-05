#!/usr/bin/env python3
import time

import requests
from influxdb import InfluxDBClient

PAGES = [
    "https://www.google.com/",
    "https://www.lemonde.fr/"
]

client = InfluxDBClient(
    host='localhost',
    port=8086,
    database='my_cool_db'
)

while True:
    for page in PAGES:
        response = requests.get(page)
        point = {
            "measurement": "webpage_load",
            "tags": {
                "page": page,
            },
            "fields": {
                "load_time": response.elapsed.total_seconds(),
                "size": len(response.text),
                "status_ok": response.status_code == 200
            }
        }
        client.write_points([point])
        print(f"Wrote point to db: {point}")
        time.sleep(1)
