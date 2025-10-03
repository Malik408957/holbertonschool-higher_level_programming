-- 3-force_name.sql
-- This script creates the table force_name with id and name columns
-- name column cannot be null

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
