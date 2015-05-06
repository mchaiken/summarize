from flask import Flask, render_template, request, flash, session, redirect, url_for
from pymongo import Connection
from bs4 import BeautifulSoup, SoupStrainer
from getResults import *
import urllib
import unicodedata
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



@app.route("/summary/<url>",methods=["GET", "POST"])
def summarize(url):
    print url
    url=unicodedata.normalize('NFKD', url).encode('ascii','ignore')
    url = url.replace("%9l","/")
    print url
    search_results=""
    only_p= SoupStrainer("p")
    paras= []
    paras.append(BeautifulSoup(urllib.urlopen(url).read(),parse_only=only_p).get_text())
    #top = findNMostCommon(get_paragraph_points(paras))
    print "HTML: "+str(paras)


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


