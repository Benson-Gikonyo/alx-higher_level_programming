#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db_connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT * FROM states ORDER BY states.id ASC')

    rows = db_cursor.fetchall()
    for row in rows:
        print(row)

    db_cursor.close()
    db_connection.close()
