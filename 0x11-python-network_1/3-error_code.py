#!/usr/bin/python3
"""
takes in a URL and sends a request to the URL and desplays the body response
"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(respnse.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f'Error code: {e.code}')
