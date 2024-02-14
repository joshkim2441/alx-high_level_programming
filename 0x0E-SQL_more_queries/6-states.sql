-- Create database 'hbtn_0d_usa' and table 'states'
CREATE TABLE IF NOT EXISTS states
(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	name VARCHAR(256)
);
