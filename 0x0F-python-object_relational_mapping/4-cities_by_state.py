#!/usr/bin/python3
import MySQLdb
import sys
"""A script that lists all cities in
hbtn_0e_4_usa db"""


def get_cities(username, password, database):
    # Connect my mysql db
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='hbtn_0e_4_usa'
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

    # Close cursor & db

    cursor.close()
    conn.close()

    for row in rows:
        print(row)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Call function

        get_cities(username, password, database)
