-- This script displays the top 3 cities' temperatures during July and August.
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
