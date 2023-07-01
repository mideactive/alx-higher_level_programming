#!/usr/bin/python3
# A script that fetches url content
import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    resp = urllib.request.urlopen(url)

    r = resp.read()
    tp = type(r)
    cont = r.decode('utf-8')
    print("Body response:$")
    print("- type: {}$".format(r))
    print("- content: {}$".format(tp))
    print("- utf8 content: {}$".format(cont))
