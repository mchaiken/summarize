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
import json
from functools import wraps
app = Flask(__name__)


def auth(f):
    @wraps(f)
    def inner(*args):
        if 'user' in session:
            return f(*args)
        else:
            flash("You must be logged in to see this page")
            session['next'] = f.__name__
            return redirect( url_for('index') )
    return inner
@app.route("/home",methods=["GET","POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    if "user" in session:
        return render_template("home.html",has_saved = (len(get_user_urls(session["user"])) > 0))
    else:
        return render_template("index.html",home=True)

@app.route("/save/<url>/<title>")
def add(url, title):
    from datetime import date
    if "user" in session:
        today = date.today()
        date = str(today.month) + "/" + str(today.day) +"/" +str(today.year)
        #saved_page(session["user"],title,url,date)
        message =  saved_page(session["user"],url,title,date)
    else:
        return redirect("/")
    return render_template("saved_success.html",message=message)

@app.route("/remove/<url>/<title>/<date>")
def remove(url, title, date):

    if "user" in session:
        remove_page(session["user"],url,title,date.replace("%9l","/"))
        flash ("Page successfully removed","success")
    return redirect("/")


@app.route("/saved/<id>/<url>/")
def saved(url,id):
    res = get_user_info(session["user"],id)
    article = has_url(url)
    old_url = url
    paragraphs=[]
    title =""
    if article:
        paragraphs = article["list"]
        title = article["title"]
        print "Retrieved"
    return render_template("saved.html",url=url,date=res[2].replace("/","%9l"), paragraphs=paragraphs,title=title )
    

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
        url = url.replace("%9s"," ")
        print url
        text = get_text(url)
        paragraphs = get_paragraph_points(text[0])
        print paragraphs
        title = text[1]
        add_scrape(old_url, paragraphs,title)
    return render_template("summary.html",loggedIn = ("user" in session), paragraphs=paragraphs, url=old_url,title = title)

@app.route("/about", methods=["GET","POST"])
def about():
    if "user" in session:
        return render_template("about.html",about=True,login=True)
    else:
        return render_template("about.html",about=True,login=False)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        
        registered = register_user(request.form["fname"],request.form["lname"],request.form["email"],request.form["passwd"])
        print registered
        if registered:
            session["user"]=request.form["email"]
            flash("You've successfully registered!","success")
            return redirect("/")
        else:
            flash("That email is already registered!", "danger")
    return render_template("register.html",register=True)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user  = authenticate_login(request.form["email"],request.form["passwd"])
        if not user == None:
            session["user"]= user
            return redirect("/")
        else:
            flash("Invalid Login", "danger")
            print "Login Failed"
            return redirect("/")
        
    return render_template("login.html", login=True)


@app.route("/links")
def links():
    print "called"
    links = []
    #print get_user_urls(session["user"])
    i=0
    for link  in get_user_urls(session["user"]):
        print link[0][0]
        links.append({"url_display":link[1].replace("%9l","/"),"url":link[1], "title":link[0],"date":link[2],"_id":i});
        i+=1
    #links = [x  for x in get_user_urls(session["user"])]
    print links
    return json.dumps(links)

@app.route ("/link")
def link(id = None):
    j = request.get_json();
    print id, j
    if id == None:
        id =j['content']


    return json.dumps({'result':x})

@app.route("/settings", methods=["GET","POST"])
@auth
def settings():
    if request.method == "POST":
        settings = change_settings(request.form["fname"],request.form["lname"],request.form["email"],request.form["passwd"],request.form["new_passwd"])
        print settings
        if settings:
            session["user"]=request.form["email"]
            flash("You've successfully changed your password!","success")
            return redirect("/")
        else:
            flash("That email is already registered!", "danger")
    return render_template("settings.html", settings=True)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("user")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret"
    app.run()


