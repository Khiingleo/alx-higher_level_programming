-- creates the database hbtn_0d_usa and the table states(in the database hbtn_0d_usa)
-- id INT unique, auto generated, can't be null and is a primary key
-- name VARCHAR(256) can't be NULL
-- if the table states already exists, and the database hbtn_0d_usa already exists
-- the script should not fail

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS states (
	`id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL
);
