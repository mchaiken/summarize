from flask import Flask, render_template, request, flash, session, redirect, url_for
from pymongo import MongoClient
from bs4 import BeautifulSoup, SoupStrainer
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
            if 'logged_in' not in session:
                flash("You must be logged in to see this page")
                return redirect('/')
            return f(*args)
        return inner
    return decorate

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html",home=True)



@app.route("/summary/<url>",methods=["GET", "POST"])
def summarize(url):

    print url
    url=unicodedata.normalize('NFKD', url).encode('ascii','ignore')
    url = url.replace("%9l","/")
    print url

    text = get_text(url)
    paragraphs = get_paragraph_points(text[0])
    print paragraphs
    #paragraphs=[(10, 10,'HAUSFKHDSFHDJ'),(10, 10,'dsaffgdhdgdhd')]
    return render_template("summary.html",paragraphs=paragraphs, title = text[1])


#def get_text(url):
#    data=""
#    p=requests.get(url).content
#    soup=BeautifulSoup(p)    
#    paragraphs=soup.select("p.story-body-text.story-content")
#    data=p
#    text=""
#    for paragraph in paragraphs:
#        text+=paragraph.text
#    text=text.encode('ascii', 'ignore')
#    return str(text)


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
            flash("Invalid Login")
            print "Login Failed"
        
    return render_template("login.html", login=True)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret"
    app.run()


