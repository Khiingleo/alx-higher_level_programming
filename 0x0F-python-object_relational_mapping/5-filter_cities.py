#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities
in that state using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2],
                             db=argv[3])

        cur = db.cursor()

        query = """SELECT cities.name
                   FROM cities
                   INNER JOIN states ON cities.state_id = states.id
                   WHERE states.name LIKE %s
                   ORDER BY cities.id ASC"""

        cur.execute(query, (argv[4],))

        rows = cur.fetchall()
        print(", ".join(["{}".format(row[0]) for row in rows]))

        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e})
