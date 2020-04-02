from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm


@app.route("/recipes", methods=["GET"])
#@login_required
def show_recipes():
	return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/", methods=["POST"])
@login_required
def recipes_add():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

   # p = Purchase(request.form.get("name"))
    r = Recipe(form.name.data)
    r.account_id = current_user.id
    #r.account_name = current_user.name

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("show_recipes"))

@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())
