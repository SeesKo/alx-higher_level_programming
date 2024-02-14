-- This script creates a database and a table on a MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL);
