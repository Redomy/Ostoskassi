# account table:

	CREATE TABLE account (id INTEGER PRIMARY KEY, date_created DATETIME, date_modified DATETIME,
	name VARCHAR(144), username VARCHAR(144), password VARCHAR(144));

# recipe table:

	CREATE TABLE recipe (id INTEGER PRIMARY KEY, date_created DATETIME, date_modified DATETIME,
	name VARCHAR(144), account_id INTEGER);


# ingredient table:

	CREATE TABLE ingredient (id INTEGER PRIMARY KEY, date_created DATETIME, date_modified DATETIME,
	name VARCHAR(144), amount VARCHAR(144), recipe_id INTEGER);
