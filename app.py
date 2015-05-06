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
    url = url.replace("%9","/")
    print url
    search_results=""
    only_p= SoupStrainer("p")
    paras= []
    html = urllib.urlopen('http://python.org/').read()
    #top = findNMostCommon(get_paragraph_points(paras))
    print html


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
    app.run()