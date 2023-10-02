#!/usr/bin/python3
"""
takes github credentials(username and password) and uses github api to display
id
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    u_name = argv[1]
    passwd = argv[2]
    url = "https://api.github.com/user"

    auth = HTTPBasicAuth(u_name, passwd)
    r = requests.get(url, auth=auth)
    print(r.json().get("id"))
