#!/usr/bin/python3
"""A url script that takes,sends and
displays the the variable X-Reqest-Id"""

import requests
import sys

url = sys.argv[1]
resp = requests.get(url)
if 'X-Request-Id' in resp.headers:
    r = resp.headers['X-Request-Id']
    print(r)
