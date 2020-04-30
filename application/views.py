from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html",
    						 has_no_recipes=User.find_users_with_no_recipes(),
    						 is_great=User.has_recipes(), is_famous=User.has_fame())
