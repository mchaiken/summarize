from flask import Flask, render_template, request, flash, session, redirect, url_for
from pymongo import Connection

app = Flask(__name__)



def auth(page):
    def decorate(f):
        @wraps(f)
        def inner(*args):
            if 'logged_in' not in session:
                flash("You must be logged in to see this page")
                return redirect('/')
            return f(*args)
        return inner
    return decorate

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET","POST"])
def about():
    return render_template("about.html")

@app.route("/register", methods=["GET","POST"])
def register():
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    return "login"

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret"
    app.run()

