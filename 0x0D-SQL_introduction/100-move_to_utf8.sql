-- This script converts hbtn_0c_0 database, first_table table, and name field in first_table to UTF8.
USE hbtn_0c_0;
ALTER TABLE first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
