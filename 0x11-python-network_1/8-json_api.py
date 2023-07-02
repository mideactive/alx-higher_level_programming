#!/usr/bin/python3
"""A script that takes letter, sends post request
to url with letter param"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if len(argv) > 1:
        q = argv[1]
    r = requests.post(url, data={'q': q})
    try:
        json = r.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except ValueError:
        print("Not a valid JSON")
