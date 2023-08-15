-- creates a table (first table) in my current database
-- description *id INT *name VARCHAR(256)
-- if (first table) exists, the script should not fail

CREATE TABLE IF NOT EXISTS `first_table` (
	id INT,
	name VARCHAR(256)
);
