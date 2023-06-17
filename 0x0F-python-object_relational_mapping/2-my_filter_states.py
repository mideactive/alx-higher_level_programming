#!/usr/bin/python3
"""A script that takes in an argument and displays all
values in the state table of hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    us = sys.argv[1]
    pw = sys.argv[2]
    dt = sys.argv[3]
    sn = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=us,
        passwd=pw,
        db=dt,
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve matching states
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
    '{}' ORDER BY id".format(sn))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the matching states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
