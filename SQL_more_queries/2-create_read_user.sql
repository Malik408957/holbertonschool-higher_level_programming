-- 2-create_read_user.sql
-- This script creates the database hbtn_0d_2 and user user_0d_2 with SELECT privilege

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it doesn't exist and set password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege only on hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;
