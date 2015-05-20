from flask import Flask, render_template, request, flash, session, redirect, url_for
from pymongo import MongoClient
from bs4 import BeautifulSoup, SoupStrainer
import time
from datetime import date
from getResults import *
from dbactions import *
import urllib
import unicodedata
import requests
app = Flask(__name__)



def auth(page):
    def decorate(f):
        @wraps(f)
        def inner(*args):
            if 'user' not in session:
                flash("You must be logged in to see this page")
                return redirect('/')
            return f(*args)
        return inner
    return decorate

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html",home=True)

@app.route("/add/<url>/<title>")
def add(url, title):
    if "user" in session:
        today = date.today()
        date = str(today.month) + "/" + str(today.day) +"/" +str(today.year)
        saved_page(session["user"],title,url,date)
        message = ("Your article has been saved")
    else:
        message = ("You must log in ")

@app.route("/summary/<url>",methods=["GET", "POST"])
def summarize(url):
    check = has_url(url)
    old_url = url
    if check:
        paragraphs = check["list"]
        title = check["title"]
        print "Retrieved"
    else:
        print url
        url=unicodedata.normalize('NFKD', url).encode('ascii','ignore')
        url = url.replace("%9l","/")
        print url
        text = get_text(url)
        paragraphs = get_paragraph_points(text[0])
        print paragraphs
        title = text[1]
        add_scrape(old_url, paragraphs,title)
    return render_template("summary.html",paragraphs=paragraphs, url=url,title = title)

@app.route("/about", methods=["GET","POST"])
def about():
    return render_template("about.html",about=True)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        
        registered = register_user(request.form["fname"],request.form["lname"],request.form["email"],request.form["passwd"])
        print registered
        if registered:
            flash("You have been registered! Login!", "success")
            return redirect("/login")
        else:
            flash("That email is already registered!", "danger")


    return render_template("register.html",register=True)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user  = authenticate(request.form["email"],request.form["passwd"])
        if not user == None:
            session["user"]= user
            return redirect("/")
        else:
            flash("Invalid Login", "danger")
            print "Login Failed"
        
    return render_template("login.html", login=True)

@app.route("/home", methods=["GET","POST"])
def home():
    return render_template("home.html", home=True)


@app.route("/links")
def links():
    links = [x  for x in get_user_urls(session["user"])]
    return json.dumps(urls)

@app.route ("/link")
def link(id = None):
    j = request.get_json();
    print id, j
    if id == None:
        id =j['content']


    return json.dumps({'result':x})

@app.route("/settings", methods=["GET","POST"])
def settings():
    return render_template("settings.html", settings=True)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret"
    app.run()


