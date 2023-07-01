#!/usr/bin/python3
"""A script that takes url, sends request
and displays the body of the response
in utf-8"""
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urlopen(url) as resp:
            r = resp.read().decode('utf-8')
            print(r)
    except HTTPError as h:
        print("Error code: {}".format(h.code))
    except URLError as e:
        print("Error code: {}".format(e.reason))
