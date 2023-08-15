-- dislplays the average temperature by city and ordered by temperature(descending)

SELECT city, AVG(value) AS `avg_temp` FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;
