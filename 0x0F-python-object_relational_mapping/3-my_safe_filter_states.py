#!/usr/bin/python3
"""Module get all states"""
import MySQLdb
import sys


if __name__ == '__main__':
    database = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])
    cursor = database.cursor()
    states = cursor.execute("SELECT * FROM states WHERE name = %(state)s ORDER \
BY states.id ASC", {'state': sys.argv[4]})
    result = cursor.fetchall()
    for row in result:
        print(row)
