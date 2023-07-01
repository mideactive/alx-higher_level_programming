#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
resp = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(resp.text))
print("\t- content:", (resp.text))
