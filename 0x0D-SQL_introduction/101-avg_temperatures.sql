-- This script displays the average temperature by city, in descending order.
USE hbtn_0c_0;
SELECT city, AVG(temperature) AS average_temperature FROM temperatures GROUP BY city ORDER BY average_temperature DESC;
