#!/usr/bin/python3
"""A script that takes letter, sends post request
to url with letter param"""
import requests
import sys

if __name__ == '__main__':
     if len(sys.argv) < 2:
        print("No result")
    else:
        payload = {'q': sys.argv[1]}
        resp = requests.post('http://0.0.0.0:5000/search_user', data=payload)

        r_json = resp.json()
        if r_json and type(r_json) == dict:
            print("[{}] {}".format(r_json['id'], r_json['name']))
        elif r_json == {}:
            print("No result")
        else:
            print("Not a valid JSON")
