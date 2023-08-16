-- creates the MySQl server <user_od_1>
-- the <user_0d_1> has all privileges on the MySQL server
-- the <user_0d_1> password is set ot 'user_0d_1_pwd'
-- if the user <user_0d_1> already exists, the script doesn't faile

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
