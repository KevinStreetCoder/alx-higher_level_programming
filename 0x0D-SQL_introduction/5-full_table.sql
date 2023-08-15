-- Print the full description of the table first_table from the specified database
USE `hbtn_0c_0`;

-- Store the table description in a variable
SET @table_description = (SELECT table_create FROM information_schema.tables WHERE table_schema = DATABASE() AND table_name = 'first_table');

-- Print the table description
SELECT @table_description;
