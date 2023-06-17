#!/usr/bin/python3
import MySQLdb
import sys
""" A script that selects all state that starts with N from 
hbtn_0e_0_usa database
"""

def get_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to select states
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows
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
        print("Usage: <username> <password> <database>")
    else:
        # Retrieve the arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Call the function to get the states
        get_states(username, password, database)

