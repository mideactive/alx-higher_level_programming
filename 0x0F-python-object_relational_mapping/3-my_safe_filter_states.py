#!/usr/bin/python3
"""A script that prevents mysql injection"""
import MySQLdb
import sys


def get_state(username, password, database, sn):
    # Connect to db
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='hbtn_0e_0_usa'
            )
    # sql object cursor
    cursor = conn.cursor()

    # Query mysql db

    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
    cursor.execute(query, (sn,))

    # fetch rows

    row = cursor.fetchall()

    # Close cursor
    cursor.close()

    # Close db

    conn.close()

    for row in row:
        print(row)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage <username> <password> <database> <sn>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        sn = sys.argv[4]

        # call function

        get_state(username, password, database, sn)
