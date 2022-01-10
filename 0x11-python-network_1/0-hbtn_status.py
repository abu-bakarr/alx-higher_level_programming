#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import urllib.request as req


if __name__ == "__main__":
    rr = req.Request('https://intranet.hbtn.io/status')
    with req.urlopen(rr) as res:
        body = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode("utf-8")))