#!/usr/bin/python3
import MySQLdb
import sys

""" A script that lists all states from the database hbtn_0e_usa """


def get_states(username, password, database):
    # Connect to MySQL
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create  cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()

    # Print the states
    for row in rows:
        print(row)


if __name__ == '__main__':
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
    else:
        # Retrieve the arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Call the function to get the states
        get_states(username, password, database)
