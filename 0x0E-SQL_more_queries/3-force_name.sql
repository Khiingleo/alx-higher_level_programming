-- createes the table <force_name> on the MySQL server
-- force_name description
-- id INT
-- name VARCHAR(256) can't be null
-- if the force_name already exists, the script should not fail

CREATE TABLE IF NOT EXISTS `force_name` (
	`id` INT,
	`name` VARCHAR(256) NOT NULL
);
