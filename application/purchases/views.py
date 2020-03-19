from application import app, db
from flask import redirect, render_template, request, url_for
from application.purchases.models import Purchase

@app.route("/purchases", methods=["GET"])
def purchases_index():
    return render_template("purchases/list.html", purchases = Purchase.query.all())

@app.route("/purchases/new/")
def purchases_form():
    return render_template("purchases/new.html")

@app.route("/purchases/<purchase_id>/", methods=["POST"])
def purchases_set_amount(purchase_id):

    p = Purchase.query.get(purchase_id)
    p.amount = p.amount + 1
    db.session().commit()
  
    return redirect(url_for("purchases_index"))

#tasks_create
@app.route("/purchases/", methods=["POST"])
def purchases_add():
    p = Purchase(request.form.get("name"))

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("purchases_index"))
