-- lists all records with a score >= 10 in the (second_table) table
-- results display both the score and the name(in this order)
-- records are ordered by score(top first)

SELECT `score`, `name` FROM `second_table` WHERE score >= 10 ORDER BY score DESC;
