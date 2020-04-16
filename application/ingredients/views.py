from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm

@app.route("/recipes/edit/<recipe_id>/new/", methods=["GET"])
@login_required
def show_ingredientform(recipe_id):
	#recipe = Recipe.query.get(recipe_id)
	#if current_user.id == recipe.account_id:
	return render_template("ingredients/new.html", form = IngredientForm())

@app.route("/recipes/edit/<recipe_id>/new/", methods=["POST"])
@login_required
def add_ingredient(recipe_id):
	form = IngredientForm(request.form)

	if not form.validate():
		return render_template("ingredients/new.html", form = form)

	ingredient = Ingredient(form.name.data, form.amount.data)
	#ingredient.amount = form.amount.data
	ingredient.recipe_id = recipe_id

	db.session().add(ingredient)
	db.session().commit()

	return redirect(url_for("show_recipes"))

@app.route("/recipes/edit/<recipe_id>/<ingredient_id>/", methods=["GET"])
@login_required
def show_ingredienteditform(recipe_id, ingredient_id):
	#recipe = Recipe.query.get(recipe_id)
    #if current_user.id == recipe.account_id:
	return render_template("ingredients/edit.html", form = IngredientForm())
	#return redirect(url_for("show_recipes"))

@app.route("/recipes/edit/<recipe_id>/<ingredient_id>/", methods=["POST"])
@login_required
def edit_ingredient(recipe_id, ingredient_id):
	form = IngredientForm(request.form)
	ingredient = Ingredient.query.get(ingredient_id)

	if not form.validate():
		return render_template("ingredient/edit.html", form = form)

	ingredient.name = form.name.data
	ingredient.amount = form.amount.data
	db.session().commit()
	return redirect(url_for("show_recipes"))

@app.route("/recipes/edit/<recipe_id>/<ingredient_id>/delete/")
@login_required
def delete_ingredient(recipe_id, ingredient_id):
	#recipe = Recipe.query.get(recipe_id)
    #if current_user.id == recipe.account_id:
	ingredient = Ingredient.query.get(ingredient_id)
	db.session().delete(ingredient)
	db.session.commit()
	return redirect(url_for("show_recipes"))

	#return redirect(url_for("show_recipes"))