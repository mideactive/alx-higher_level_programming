#!/usr/bin/python3
'''takes name of a state as an arg and lists all cities in that state'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT a.name FROM cities AS a JOIN states AS b ON "
                "a.state_id = b.id WHERE b.name = %s ORDER BY a.id",
                (argv[4],))
    db.close()
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
