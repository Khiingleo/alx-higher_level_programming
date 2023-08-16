-- creates a unique_id table
-- id INT default value of 1
-- name VARCHAR(256)
-- if table exists, script does not fail

CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
