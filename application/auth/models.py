from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

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
    def find_users_with_no_recipes():
        stmt = text("SELECT Account.id, Account.name FROM Account "
                    "LEFT JOIN Recipe ON Recipe.account_id = Account.id "
                    "GROUP BY Account.id "
                    "HAVING COUNT(Recipe.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response

    @staticmethod
    def find_lazy_users():
        #ei toimi vielä
        stmt = text("SELECT Account.id, Account.name FROM Account "
                    "LEFT JOIN Recipe ON Recipe.account_id = Account.id "
                    "LEFT JOIN Ingredient ON Recipe.id = Ingredient.recipe_id "
                    "GROUP BY Account.id "
                    "HAVING COUNT(Ingredient.id) < 3")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response