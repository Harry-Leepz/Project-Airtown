import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_posts")
def get_posts():
    posts = mongo.db.posts.find()
    # print(list(posts))
    return render_template("posts.html", posts=posts)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # Check if username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # If Username exists then flash message
            # and redirect back to signup page
            flash("Username already exists, Please try another Username")
            return redirect(url_for("sign_up"))

        # Take user input and place as users in database
        sign_up = {
            "username": request.form.get("username").lower(),
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        # Place new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up complete, Welcome to Air Town")
    return render_template("sign-up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
