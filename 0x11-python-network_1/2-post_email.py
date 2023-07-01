#!/usr/bin/python3
"""A script That takes a url and email
sends POST request passed to URL with email
and displays body resposne"""

from urllib.request import Request, urlopen
import urllib.parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urlopen(url, data) as resp:
        print(resp.read().decode('utf-8'))
