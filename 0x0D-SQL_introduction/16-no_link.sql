-- This script lists all records of the table second_table with a name value,
-- displaying both score and name, and orders the result by descending order.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
