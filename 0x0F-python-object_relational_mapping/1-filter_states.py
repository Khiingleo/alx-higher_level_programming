#!/usr/bin/python3
"""
lists all states with a name starting with 'N'(upper)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2],
                             db=argv[3])

        cur = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
