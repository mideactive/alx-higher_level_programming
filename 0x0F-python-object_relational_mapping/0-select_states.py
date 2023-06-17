#!/usr/bin/python3
import MySQLdb
from sys import argv

""" A script that lists all states from the database hbtn_0e_usa """


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
