#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:{}".format(type(resp.text)))
    print("\t- content:{}".format(resp.text))
