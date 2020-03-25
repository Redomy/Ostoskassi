from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class PurchaseForm(FlaskForm):
    name = StringField("Purchase name", [validators.Length(min=2)])
    amount = IntegerField("Amount")
 
    class Meta:
        csrf = False
