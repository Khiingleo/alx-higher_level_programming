#!/usr/bin/python3
"""
takes an argument and displays all values in the states table
of the database give where name matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2],
                             db=argv[3])

        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (argv[4],))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"MySQLdb Error: {e}")
