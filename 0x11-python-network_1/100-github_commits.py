#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from requests import get, auth
from sys import argv


if __name__ == "__main__":
    resp = get("https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])).json()
    count = 0
    for lines in resp:
        print("{}: {}".format(lines.get('sha'),
                              lines.get('commit').get('author').get('name')))
        count += 1
        if count == 10:
            break
