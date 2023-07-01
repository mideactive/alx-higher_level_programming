#!/usr/bin/python3
"""A script that takes, sends and displays the url body"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
