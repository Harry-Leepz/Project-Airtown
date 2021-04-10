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
        return redirect(url_for("account", username=session["user"]))
    return render_template("sign-up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # Check user password input versus database password
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(
                    request. form.get("username")))
                return redirect(url_for(
                    "account", username=session["user"]))
            else:
                # Display message for incorrect password
                flash("Incorrect Username/Password")
                return redirect(url_for("login"))
        else:
            # Display message for incorrect username
            flash("Incorrect Username/Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # Obtaining the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("account.html", username=username)


@app.route("/logout")
def signout():
    # Removing the user from the session cookie
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/the_wall")
def the_wall():
    posts = list(mongo.db.posts.find())
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("wall.html", posts=posts, categories=categories)


@app.route("/the_wall", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        post = {
            "post_author": session["user"],
            "post_title": request.form.get("post_title"),
            "category_name": request.form.get("category_name"),
            "post_content": request.form.get("post_content")
        }
        mongo.db.posts.insert_one(post)
        flash("Sucessfully posted on The Wall")
        return redirect(url_for("the_wall"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
