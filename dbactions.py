from pymongo import MongoClient


#mongo setup
conn = MongoClient()
db = conn["summarize"]

#inserts the user's fb id and username into the collection
def register_user(fname,lname,email,passwd):
    if not user_exists(email):
        print "trying to register"
        db.summarize.insert({"fname":fname , "lname":lname,"email":email,"passwd":passwd, "folders":[]})
        return True
    return False

def user_exists(email):
    check = None
    check = db.summarize.find_one({'email':email})
    if check:
        return True
    return False

def authenticate(email, password):
    user = db.summarize.find_one( { 'email' : email },{"_id":False})
    if user == None:
        return None
    passwd = user["passwd"]
   
   
    if passwd == password:
        return user
    else:
        
        return None

def saved_page(email,url,date):
    user = db.summarize.find_one({'email':email})
    folder = user["folder"]
    folder.append((url,date))
    
def has_url(url):
    check = None
    check = db.urls.find_one({'url':url})
    return check

def add_scrape(url,list,title):
    if not(has_url(url)):
        db.urls.insert({"url":url,"list":list,"title":title})




