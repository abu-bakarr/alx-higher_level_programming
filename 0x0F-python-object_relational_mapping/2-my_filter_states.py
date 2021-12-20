#!/usr/bin/python3
"""Module get all states"""
import MySQLdb
import sys


if __name__ == '__main__':
    database = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY\
                name='{:s}' ORDER BY id ASC".format(sys.argv[4]))
    result = cur.fetchall()
    for row in result:
        print(row)
