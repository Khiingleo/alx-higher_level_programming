#!/usr/bin/python3
"""
list 10 most commits (most recent to oldest) in the repository 'rails'
by the user 'rails'
"""
import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"

    r = requests.get(url)
    commits = r.json()

    for i in commits[:10]:
        print(i.get('sha'), end=': ')
        print(i.get('commit').get('author').get('name'))
