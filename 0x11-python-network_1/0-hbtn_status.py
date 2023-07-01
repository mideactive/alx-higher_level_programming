#!/usr/bin/python3
# A script that fetches url content
import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as req:
        r = req.read()

    tp = type(r)
    cont = r.decode('utf-8')
    print("Body response:")
    print("    - type: {}".format(tp))
    print("    - content: {}".format(r))
    print("    - utf8 content: {}".format(cont))
