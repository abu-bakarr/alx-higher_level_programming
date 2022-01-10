#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from requests import get
from sys import argv


if __name__ == "__main__":
    resp = get(argv[1])
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
