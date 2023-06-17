#!/usr/bin/python3
import MySQLdb
import sys
"""A script that filters cities in the
hbtn_0e_4_usa db"""


def get_cities_by_state(username, password, database, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities of the specified state
    query = "SELECT DISTINCT cities.name\
             FROM cities JOIN states\
             ON cities.state_id = states.id\
             WHERE states.name = %s"
    cursor.execute(query, (state_name, ))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    # Print the cities
    for row in rows:
        print(row)


if __name__ == '__main__':
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage:<username> <password> <database> <state_name>")
    else:
        # Retrieve the arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        # Call the function to get the cities by state
        get_cities_by_state(username, password, database, state_name)
