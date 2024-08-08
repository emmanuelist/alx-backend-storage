-- Check if the column 'country' exists
SET @column_exists = (
    SELECT COUNT(*)
    FROM information_schema.columns
    WHERE
        table_schema = 'holberton'
        AND table_name = 'users'
        AND column_name = 'country'
);

-- If the column does not exist, add it
SET @query = IF(
    @column_exists = 0,
    'ALTER TABLE users ADD COLUMN country ENUM(''US'', ''CO'', ''TN'') DEFAULT ''US'' NOT NULL;',
    'SELECT "Column already exists"'
);

PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
