from application import db
from application.models import Base

class Purchase(Base):

    name = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.amount = 1
