from application import db
from application.models import Base

class Ingredient(Base):

	name = db.Column(db.String(144), nullable=False)
	amount = db.Column(db.String(144), nullable=False)

	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

	def __init__(self, name, amount):
		self.name = name
		self.amount = amount