from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    purchases = db.relationship("Purchase", backref='account', lazy=True)
    #recipes = db.relationship("Purchase", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

    @staticmethod
    def find_users_with_no_purchases(amount=0):
        stmt = text("SELECT Account.id, Account.name FROM Account "
                    "LEFT JOIN Purchase ON Purchase.account_id = Account.id "
                    "WHERE (Purchase.amount IS null OR Purchase.amount = :amount) "
                    "GROUP BY Account.id "
                    "HAVING COUNT(Purchase.id) = 0").params(amount=amount)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response