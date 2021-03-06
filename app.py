import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    # Render Home page as landing page
    return render_template("home.html")


@app.route("/jordan_page")
def jordan_page():
    # Render Jordan brand page
    return render_template("jordan.html")


@app.route("/nike_page")
def nike_page():
    # Render Nike brand page
    return render_template("nike.html")


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
                    request. form.get("username").capitalize()))
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
    # Obtaining the session user from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    posts = list(mongo.db.posts.find(
        {"post_author": session["user"]}).sort("post_date", -1))
    return render_template("account.html", posts=posts, username=username)


@app.route("/signout")
def signout():
    # Removing the user from the session cookie
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/the_wall")
def the_wall():
    # Obtaining the posts collection from the database and sorting by date
    # Obtaining the categories collection from the data and sorting
    posts = list(mongo.db.posts.find().sort("post_date", -1))
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template(
        "wall.html", posts=posts, categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    posts = list(mongo.db.posts.find({"$text": {"$search": query}}))
    return render_template("wall.html", posts=posts)


@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    # Inserting a new post into the database
    if request.method == "POST":
        post = {
            "post_author": session["user"],
            "post_date": datetime.datetime.utcnow().strftime(
                '%d %B %Y - %H:%M:%S'),
            "post_title": request.form.get("post_title"),
            "category_name": request.form.get("category_name"),
            "post_content": request.form.get("post_content")
        }
        mongo.db.posts.insert_one(post)
        flash("Sucessfully posted on The Wall")
        return redirect(url_for("the_wall"))
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template(
        "create-post.html", categories=categories)


@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    # Editing a post in the database
    if request.method == "POST":
        submit = {
            "post_author": session["user"],
            "post_date": datetime.datetime.utcnow().strftime(
                '%d %B %Y - %H:%M:%S'),
            "post_title": request.form.get("post_title"),
            "category_name": request.form.get("category_name"),
            "post_content": request.form.get("post_content")
        }
        mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
        flash("Post Updated!")
    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template(
        "edit-post.html", post=post, categories=categories)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    # Deleting a post from the database
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post Deleted!")
    return redirect(url_for("the_wall"))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
