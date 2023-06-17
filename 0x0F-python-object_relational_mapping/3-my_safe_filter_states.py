#!/usr/bin/python3
"""A script that prevents mysql injection"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: <un> <pw> <db> <sn>")
    else:
        un = sys.argv[1]
        pw = sys.argv[2]
        dt = sys.argv[3]
        sn = sys.argv[4]
    # Connect to db
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=un,
            passwd=pw,
            db=dt
            )
    # sql object cursor
    cursor = conn.cursor()

    # Query mysql db

    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
    cursor.execute(query, (sn,))

    # fetch rows

    rows = cursor.fetchall()

    # print rows
    for row in rows:
        print(row)

    # Close cursor
    cursor.close()

    # Close db
    conn.close()
