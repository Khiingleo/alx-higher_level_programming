#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]

    payload = {'q': letter}

    r = requests.post(url, data=payload)

    try:
        response = r.json()
        if 'id' in response and 'name' in response:
            print(f"[{response.get('id')}] {response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
