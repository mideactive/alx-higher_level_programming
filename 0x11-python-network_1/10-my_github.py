#!/usr/bin/python3
"""A script that gets my user ID from github"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    resp = requests.get(url, auth=(username, password))
    print(resp.json().get('id'))
