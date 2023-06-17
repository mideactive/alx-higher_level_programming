#!/usr/bin/python3
import MySQLdb
import sys
"""A script that takes in an argument and displays all
values in the state table of hbtn_0e_0_usa"""


def get_states(username, password, database, sn):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='hbtn_0e_0_usa'
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve matching states
    qr = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sn)
    cursor.execute(qr)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    # Print the matching states
    for row in rows:
        print(row)


if __name__ == '__main__':
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: <username> <password> <database> <state>")
    else:
        # Retrieve the arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        sn = sys.argv[4]

        # Call the function to get the matching states
        get_states(username, password, database, sn)
