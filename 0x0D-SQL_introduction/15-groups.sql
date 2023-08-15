-- List the number of records with the same score in the table second_table in the specified database
USE `hbtn_0c_0`;

-- Display the score and the number of records for each score, sorted by the number of records (descending)
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
