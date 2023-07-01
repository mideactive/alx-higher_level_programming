#!/usr/bin/python3
"""A script that, sends request to URL
and displays the value X-Request-Id"""
from urllib.request import Request, urlopen
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    r1 = Request(url)

    with urlopen(r1) as r:
        print(r.info()['X-Request-Id'])
