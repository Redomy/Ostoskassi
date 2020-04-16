from application import db
from application.models import Base

class Recipe(Base):

	__tablename__ = "recipe"

	name = db.Column(db.String(144), nullable=False)

	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
	#account_name = db.Column(db.String, db.ForeignKey('account.name'), nullable=False)

	def __init__(self, name):
		self.name = name




