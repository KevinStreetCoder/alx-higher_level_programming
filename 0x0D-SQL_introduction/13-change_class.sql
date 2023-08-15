-- Remove records with a score <= 5 from the table second_table in the specified database
USE `hbtn_0c_0`;

-- Remove records with score <= 5
DELETE FROM `second_table` WHERE `score` <= 5;
