-- 5-unique_id.sql
-- This script creates the table unique_id with unique id constraint

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
