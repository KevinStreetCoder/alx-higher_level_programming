-- List records with a score >= 10 in the table second_table in the specified database
USE `hbtn_0c_0`;

-- Display records with score >= 10, ordered by score (top first) with score and name
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
