#!/usr/bin/python3
"""A script that selects all state that starts with N from
hbtn_0e_0_usa database"""

import MySQLdb
import sys

if __name__ == '__main__':
    h = 'localhost'
    us = sys.argv[1]
    pw = sys.argv[2]
    dt = sys.argv[3]

    db = MySQLdb.connect(
        host=h,
        port=3306,
        user=us,
        passwd=pw,
        db=dt
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to select states
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # fetch rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # closing cursor and db
    cursor.close()
    db.close()
