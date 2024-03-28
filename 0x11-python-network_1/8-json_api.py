#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST
request to URL with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    payload = {'q': q}

    try:
        response = requests.post(
            'http://0.0.0.0:5000/search_user', data=payload
        )
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
