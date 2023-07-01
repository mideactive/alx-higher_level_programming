#!/usr/bin/python3
"""A script that takes letter, sends post request
to url with letter param"""
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ''

    # Create a dictionary with the letter parameter
    data = {'q': letter}

    # Send POST request with the letter as a parameter
    response = requests.post(url, json=data)

    try:
        json_data = response.json()
        if 'id' in json_data and 'name' in json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
