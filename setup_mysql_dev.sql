-- this script prepares a MySQL server
-- CREATE DATABASE : hbnb_dev_db
-- sets the password : hbnb_dev_pwd if it dosen't exist
-- grant the created user all privileges to the DATABASE
-- must flush privileges to reset

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
