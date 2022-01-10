#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import urllib.request as req
import sys

if __name__ == "__main__":
    rr = req.Request(sys.argv[1])
    with req.urlopen(rr) as res:
        print(res.getheader('X-Request-Id'))
