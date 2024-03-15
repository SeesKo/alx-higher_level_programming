#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieving command line arguments
    username, password, database, state_name = sys.argv[1:5]
    # Connecting to MySQL database
    conn = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = conn.cursor()
    # Execute SQL query to select cities of the given state
    cursor.execute("SELECT * FROM cities JOIN states "
                   "ON cities.state_id = states.id "
                   "WHERE states.name = %s "
                   "ORDER BY cities.id ASC", (state_name,))
    # Fetching all rows
    rows = cursor.fetchall()
    # Extracting city names for the given state
    cities = [row[2] for row in rows if row[4] == check[0]]
    # Displaying results
    print(', '.join(cities))
    # Closing cursor and database connection
    cursor.close()
    conn.close()
