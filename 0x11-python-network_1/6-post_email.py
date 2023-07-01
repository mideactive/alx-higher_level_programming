#!/usr/bin/python3
"""Post email address passed through a url"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    resp = requests.post(url, data=data)
    print(resp.text)
