#!/usr/bin/python3
'''lists all states from MySQL database hbtn_0e_0_usa'''


import MySQLdb

from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute('SELECT * FROM states ORDER BY id ASC')
    for rows in c.fetchall():
        print(rows)

    c.close()
    db.close()
