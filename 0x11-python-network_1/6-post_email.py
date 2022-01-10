#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from requests import post
from sys import argv


if __name__ == "__main__":
    res = post(argv[1], {'email': argv[2]})
    print(res.text)
