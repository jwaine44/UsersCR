# Remember to import all functionalities of Flask you need like request, redirect, render_template, etc. as needed in each file

from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User
app = Flask(__name__)


@app.route("/users")
def display_all_users():
    # call the get all classmethod to get all users
    users = User.get_all()
    return render_template("all_users.html", all_users = users)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string in user.py.
    # data = {
    #     "fname": request.form["fname"],
    #     "lname": request.form["lname"],
    #     "eml": request.form["eml"]
    # }
    # We pass the data dictionary into the create method from the user class.
    User.create(request.form)
    # Don't forget to redirect after saving to the database because we don't want to render on a post.
    return redirect('/users')
            
if __name__ == "__main__":
    app.run(debug=True)

"""
Functions as SQL Queries
SELECT:
def get_all()       If we're selecting everything i.e. SELECT *
def get_one()       If we're selecting one

INSERT:
def create()        If we're doing an insert

DELETE:
def delete_one()    If we're doing a delete

DELETE:
DEF update_one()    If we're doing an update/edit
def edit_one()      

"""