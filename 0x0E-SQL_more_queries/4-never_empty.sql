-- creates the table <id_not_null> on the MySQL server
-- decription
-- id INT default value 1
-- name VARCHAR(245)
-- if id_not_null exists, the script does not fail

CREATE TABLE IF NOT EXISTS `id_not_null` (
	`id` INT DEFAULT 1,
	`name` VARCHAR(256)
);
