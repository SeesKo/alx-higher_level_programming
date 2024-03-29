#!/usr/bin/python3
"""
Script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument (safe from MySQL injection).
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieving command line arguments
    username, password, database, state_name = sys.argv[1:5]
    # Connecting to MySQL database
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    # Creating cursor object
    cursor = conn.cursor()
    # Executing SQL query with parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    # Fetching all rows
    rows = cursor.fetchall()
    # Displaying results
    for row in rows:
        print(row)
    # Closing cursor and database connection
    cursor.close()
    conn.close()
