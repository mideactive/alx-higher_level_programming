#!/usr/bin/python3
"""A script that lists all cities in
hbtn_0e_4_usa db"""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database>")
    else:
        un = sys.argv[1]
        pw = sys.argv[2]
        dt = sys.argv[3]

    # Connect my mysql db
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=un,
            passwd=pw,
            db=dt
            )
    # Myslq object cursor
    cursor = conn.cursor()

    # query mysql db

    cursor.execute("""SELECT cities.id, cities.name, states.name
            FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC""")

    # fetch rows

    rows = cursor.fetchall()

    # print rows
    for row in rows:
        print(row)

    # Close cursor & db

    cursor.close()
    conn.close()
