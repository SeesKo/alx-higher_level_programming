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
    state_name = sys.argv[4]
    # Execute SQL query to select cities of the given state
    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    ORDER BY states.id")
    # Fetching all rows
    rows = cursor.fetchall()
    # Extracting city names for the given state
    cities_list = []
    for row in rows:
        if row[2] == state_name:
            cities_list.append(row[1])
    # Displaying results
    print(', '.join(cities))
    # Closing cursor and database connection
    cursor.close()
    conn.close()
