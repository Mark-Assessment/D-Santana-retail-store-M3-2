import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "name": request.form.get("name").lower(),
            "department": request.form.get("department").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into the 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("get_tasks", username=session["user"]))

      # Retrieve users from the database
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if Username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check to ensure hashed password matches User input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome Back, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "get_tasks", username=session["user"]))
            else:
                # User invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))    

        else:
            # Username doesnt exist
            flash("Incorrect Username and/or Password") 
            return redirect(url_for("login"))          

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Check if user is logged in
    if "user" in session:
        # Grab the session user's username from the database
        user = mongo.db.users.find_one({"username": session["user"]})
        if user:
            username = user["username"]
            today = datetime.date.today()
            tasks = mongo.db.tasks.find({"due_date": today.strftime("%Y-%m-%d")})
            users = mongo.db.users.find()
            return render_template("profile.html", username=username, users=users, tasks=tasks)
    
    # User is not logged in, redirect to the login page
    return redirect(url_for("login"))
   


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = {
            "status": "In Progress",
            "task_name": request.form.get("task_name"),
            "assigned_to": request.form.get("user_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")
        return redirect(url_for("get_tasks"))

    users = mongo.db.users.find().sort("status", 1)
    return render_template("add_task.html", users=users)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "status": request.form.get("status"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
            "assigned_to": request.form.get("user_name")
        }
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": submit})
        flash("Task Successfully Updated")
        return redirect(url_for("get_tasks"))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    users = mongo.db.users.find().sort("status", 1)
    categories = mongo.db.categories.find().sort("status", 1)
    return render_template("edit_task.html", task=task, users=users, categories=categories)


@app.route("/edit_task_status/<task_id>", methods=["GET", "POST"])
def edit_task_status(task_id):
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if request.method == "POST":
        submit = {
            "status": request.form.get("status"),
            "task_name": task["task_name"],
            "task_description": task["task_description"],
            "is_urgent": task["is_urgent"],
            "due_date": task["due_date"],
            "created_by": task["created_by"],
            "assigned_to": task["assigned_to"],
        }
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": submit})
        flash("Task Successfully Updated")
        return redirect(url_for("get_tasks"))
  
    categories = mongo.db.categories.find().sort("status", 1)
    return render_template("edit_task_status.html", task=task, categories=categories)



# Delete function for manage categories section with admin user
@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


@app.route("/get_categories")
def get_categories():
    users = list(mongo.db.users.find().sort("status", 1))
    return render_template("categories.html", users=users)


# Categories that Admin can see on his session 
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "status": request.form.get("status")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Editing function for button in Add Category section
@app.route("/edit_category/<user_id>", methods=["GET", "POST"])
def edit_category(user_id):
    if request.method == "POST":
        submit = {
            "name": request.form.get("name"),
            "department": request.form.get("department")
        }
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": submit})
        flash("User Successfully Updated")
        return redirect(url_for("get_categories"))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_category.html", user=user)


# Delete function for button in Add category section
@app.route("/delete_category/<user_id>")
def delete_category(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
