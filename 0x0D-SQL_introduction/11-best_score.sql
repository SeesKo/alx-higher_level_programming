-- This script lists records with a score >= 10 in the table second_table,
-- displaying both score and name, and orders the results by score.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
