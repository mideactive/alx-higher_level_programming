#!/usr/bin/python3
"""A script that, sends request to URL
and displays the value X-Request-Id"""
from urllib.request import Request, urlopen
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    r1 = Request(url)

    with urlopen(r1) as r:
        r2 = r.headers.get("X-Request-ID")
        if r2:
            sys.stdout.write(r2 + "\n")
        else:
            sys.stdout.write("X-Request-Id header not ound\n")
