#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id"
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (state_name,)
    )
    rows = cursor.fetchall()
    cities = ', '.join(row[0] for row in rows)
    print(cities)
    cursor.close()
    conn.close()
