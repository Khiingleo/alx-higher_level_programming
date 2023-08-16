-- lists all the cities of California tha can be found in the database hbtn_0d_usa

SELECT `id`, `name` FROM `cities`
WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = "california")
ORDER BY `id` ASC;
