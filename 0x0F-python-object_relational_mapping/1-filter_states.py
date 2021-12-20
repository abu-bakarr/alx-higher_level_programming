#!/usr/bin/python3
"""Module get all states"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    current = db.cursor()
    states = current.execute("SELECT * FROM states ORDER BY id")
    result = current.fetchall()
    for row in result:
        if row[1][0] == 'N':
            print(row)
