-- List records of the table second_table in the specified database
-- Exclude rows without a name value
USE `hbtn_0c_0`;

-- Display records with score and name, ordered by descending score
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
