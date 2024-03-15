#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":

    username, password, database, state_name = sys.argv[1:5]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           database=database)

    # Creating cursor object
    cursor = conn.cursor()
    # Executing SQL query to select cities of the given state
    cursor.execute("SELECT c.name"
                   "FROM cities AS c"
                   "JOIN states AS s ON c.state_id = s.id"
                   "WHERE s.name = %s"
                   "ORDER BY c.id ASC", (state_name,))

    # Fetching all rows
    rows = cursor.fetchall()

    # Storing cities of the given state in a list
    cities = []
    for row in rows:
        cities.append(row[0])

    # Displaying results
    print(', '.join(cities))
    # Closing cursor and database connection
    cursor.close()
    conn.close()
