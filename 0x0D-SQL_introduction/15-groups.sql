-- lists the number of records with the sam score in the (second_table) table\
-- the result displays the score 
-- the number of records for this score is displayed with the label `number`
-- the list is sorted by the number of records(descending)

SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
