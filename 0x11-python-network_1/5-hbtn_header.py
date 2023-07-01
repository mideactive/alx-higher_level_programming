#!/usr/bin/python3
"""A url script that takes,sends and
displays the the variable X-Reqest-Id"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    resp = requests.get(url)
        print(resp.headers.get('X-Request-Id'))
