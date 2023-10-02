#!/usr/bin/python3
"""
takes in a URL and sends a request to the URL and displays the value of
X-Request-Id variable found in the header of the response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
