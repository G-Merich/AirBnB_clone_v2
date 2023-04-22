-- this script prepares a MySQL server
-- CREATE DATABASE : hbnb_dev_db
-- sets the password : hbnb_dev_pwd if it dosen't exist
-- grant the created user all privileges to the DATABASE
-- must flush privileges to reset

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
