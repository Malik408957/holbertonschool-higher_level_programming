-- 7-cities.sql
-- This script creates the database hbtn_0d_usa and the table cities with foreign key

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
