#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
from requests import post
from sys import argv


if __name__ == "__main__":
    search = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        qry = argv[1]
    else:
        qry = ""
    try:
        res = post(search, data={'q': qry}).json()
        if res == {}:
            print('No result')
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except ValueError:
        print('Not a valid JSON')
