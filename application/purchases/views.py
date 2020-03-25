from application import app, db
from flask import redirect, render_template, request, url_for
from application.purchases.models import Purchase
from application.purchases.forms import PurchaseForm

@app.route("/purchases", methods=["GET"])
def purchases_index():
    return render_template("purchases/list.html", purchases = Purchase.query.all())

@app.route("/purchases/new/")
def purchases_form():
    return render_template("purchases/new.html", form = PurchaseForm())

@app.route("/purchases/<purchase_id>/", methods=["POST"])
def purchases_set_amount(purchase_id):

    p = Purchase.query.get(purchase_id)
    p.amount = p.amount + 1
    db.session().commit()
  
    return redirect(url_for("purchases_index"))

#tasks_create
@app.route("/purchases/", methods=["POST"])
def purchases_add():
    form = PurchaseForm(request.form)

    if not form.validate():
        return render_template("purchases/new.html", form = form)

   # p = Purchase(request.form.get("name"))
    p = Purchase(form.name.data)
    p.amount = form.amount.data

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("purchases_index"))
