#!/usr/bin/python3
"""
takes a URL and email, sends POST request to the passed URL with the email
as a parameter and displays the body of the response(decoded in utf-8)
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
