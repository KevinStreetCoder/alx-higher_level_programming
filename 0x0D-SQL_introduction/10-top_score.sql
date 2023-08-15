-- List all records of the table second_table in the specified database
USE `hbtn_0c_0`;

-- Display records ordered by score (top first) with score and name
SELECT `score`, `name` FROM `second_table` ORDER BY `score` DESC;
