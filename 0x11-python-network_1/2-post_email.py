#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    getData = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = request.Request(argv[1], getData)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
