#!/usr/bin/python3
# A script that fetches url contient
from urllib.request import Request, urlopen

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as req:
        r = req.read()

    tp = type(r)
    cont = r.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(tp))
    print("\t- content: {}".format(r))
    print("\t- utf8 content: {}".format(cont))
