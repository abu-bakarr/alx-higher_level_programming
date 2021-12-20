#!/usr/bin/python3
"""Module get all states"""
import MySQLdb
import sys


if __name__ == '__main__':
    database = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = database.cursor()
    states = cur.execute("SELECT cities.id, cities.name, states.name\
                          FROM cities JOIN states\
                          ON cities.state_id = states.id\
                          ORDER BY cities.id")
    result = cur.fetchall()
    for row in result:
        print(row)
