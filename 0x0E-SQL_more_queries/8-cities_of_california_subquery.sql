-- List cities of California using subquery
USE hbtn_0d_usa;
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
