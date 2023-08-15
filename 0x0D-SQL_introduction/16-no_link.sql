-- lists all records of the table (second_table)
-- does not lists rows without a `name` value
-- results display records are listed by descending order

SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
