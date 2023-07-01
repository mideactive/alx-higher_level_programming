#!/usr/bin/python3
"""A script that takes letter, sends post request
to url with letter param"""
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[2] if len(sys.argv) > 1 else ''
    data = {'q': letter}
    resp = requests.post(url, data=data)
    try:
        json_data = resp.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
