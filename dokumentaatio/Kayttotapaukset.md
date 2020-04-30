# Reseptit

### Reseptien lisäys:

	INSERT INTO recipe (id, date_created, date_modified, name, account_id) VALUES (id, date_created, date_modified,
	name, account_id);

### Reseptien poisto:
	
	DELETE FROM recipe WHERE recipe_id = recipe_id;

### Reseptien luku:

	SELECT name FROM recipe;

### Reseptien muokkaus:
	
	UPDATE recipe SET name = name WHERE id = id;

----------------------------------------------------------------------------

# Ainesosat

### Ainesosien lisäys:

	INSERT INTO ingredient (id, date_created, date_modified, name, amount, recipe_id) 
	VALUES (id, date_created, date_modified, name, amount, recipe_id);

### Ainesosien poisto:

	DELETE FROM ingredient WHERE id = id;

### Ainesosien luku:

	SELECT name, amount FROM ingredient WHERE recipe_id = recipe_id;

### Ainesosien muokkaus:

	UPDATE ingredient SET name = name, amount = amount WHERE id = id;

----------------------------------------------------------------------------

# Käyttäjät

### Login:

	SELECT * FROM account WHERE username = username AND password = password;

### Etsitään käyttäjät ilman reseptejä:

	SELECT Account.id, Account.name FROM Account 
    	LEFT JOIN Recipe ON Recipe.account_id = Account.id 
    	GROUP BY Account.id 
    	HAVING COUNT(Recipe.id) = 0
	
### Etsitään käyttäjät, jotka ovat tehneet reseptejä:

	SELECT Account.id, Account.name FROM Account 
    	LEFT JOIN Recipe ON Recipe.account_id = Account.id 
    	GROUP BY Account.id 
    	HAVING COUNT(Recipe.id) > 0
	
### Etsitään parhaat 5 käyttäjää, jotka ovat tehneet eniten reseptejä:

	SELECT Account.name, COUNT(Recipe.id) FROM Account 
    	LEFT JOIN Recipe ON Recipe.account_id = Account.id 
    	GROUP BY Account.name 
    	HAVING COUNT(Recipe.id) > 0 
    	ORDER BY COUNT(Recipe.id) DESC 
    	LIMIT 5
