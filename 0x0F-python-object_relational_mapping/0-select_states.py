#!/usr/bin/python3
"""
Script that lists all `states` from the database `hbtn_0e_0_usa`.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieving command line arguments
    username, password, database = sys.argv[1:4]
    # Connecting to MySQL database
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    # Creating cursor object
    cursor = conn.cursor()
    # Executing SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetching all rows
    rows = cursor.fetchall()
    # Displaying results
    for row in rows:
        print(row)
    # Closing cursor and database connection
    cursor.close()
    conn.close()
