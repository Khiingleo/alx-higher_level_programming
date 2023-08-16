-- creates a database <hbtn_0d_2> and the user <user_0d_2>
-- user_od_2 only has SELECT privilege in the database hbtn_0d_2
-- the user_0d_2 password is set to user_0d_2_pwd
-- if the database hbtn_0d_2 already exists, the script does not fail
-- if the user <user_0d_2> exists, the script does not exist

CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
