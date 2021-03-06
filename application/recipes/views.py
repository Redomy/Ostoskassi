from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

from application.ingredients.models import Ingredient


@app.route("/recipes", methods=["GET"])
#@login_required
def show_recipes():
	return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/edit/<recipe_id>/", methods=["POST"])
@login_required
def recipes_edit(recipe_id):

    form = RecipeForm(request.form)
    recipe = Recipe.query.get(recipe_id)

    if not form.validate():
        return render_template("recipes/edit.html", form = form, recipe=recipe)

    recipe.name = form.name.data
    db.session().commit()
    return redirect(url_for("show_recipes"))

@app.route("/recipes/edit/<recipe_id>/", methods=["GET"])
@login_required
def recipes_editform(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if current_user.id == recipe.account_id:
        return render_template("recipes/edit.html", form = RecipeForm(), recipe=recipe,
                                 ingredients = Ingredient.query.filter_by(recipe_id=recipe_id).all())
    return redirect(url_for("show_recipes"))

@app.route("/recipes/view/<recipe_id>/", methods=["GET"])
def recipes_view(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    return render_template("recipes/view.html", recipe=recipe,
                             ingredients = Ingredient.query.filter_by(recipe_id=recipe_id).all())

@app.route("/recipes/edit/<recipe_id>/delete/")
@login_required
def recipes_delete(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if current_user.id == recipe.account_id:
        ingredients = Ingredient.query.filter_by(recipe_id=recipe_id).all()
        db.session().delete(recipe)
        for ingredient in ingredients:
            db.session().delete(ingredient)

        db.session().commit()
        return redirect("/recipes")
    return redirect(url_for("show_recipes"))

@app.route("/recipes/", methods=["POST"])
@login_required
def recipes_add():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

    r = Recipe(form.name.data)
    r.account_id = current_user.id
    #r.account_name = current_user.name

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("show_recipes"))