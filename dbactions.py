from pymongo import MongoClient


#mongo setup
conn = MongoClient()
db = conn["summarize"]

#inserts the user's fb id and username into the collection
def register_user(fname,lname,email,passwd):
    if not user_exists(email):
        print "trying to register"
        db.summarize.insert({"fname":fname , "lname":lname,"email":email,"passwd":passwd, "folders":[],"urls":[]})
        return True
    return False

def change_settings(fname,lname,email,passwd,new_passwd):
    if not user_exists(email):
        print "trying to change settings"
        return False
    user = db.summarize.find_one({'email':email})
    if user['passwd'] == passwd:
        db.summarize.update({"email":email},{"$set":{"passwd":new_passwd}})
        return True
    else:
        print "original pass"
        return False

def user_exists(email):
    check = None
    check = db.summarize.find_one({'email':email})
    if check:
        return True
    return False

def authenticate_login(email, password):
    user = db.summarize.find_one( { 'email' : email },{"_id":False})
    if user == None:
        return None
    passwd = user["passwd"]
   
   
    if passwd == password:
        return user["email"]
    else:
        
        return None
def get_user_info(email,id):
    user = db.summarize.find_one({'email':email})
    folder = user["folders"]
    id= int(id)
    return folder[id]


def saved_page(email,title,url,date):
    user = db.summarize.find_one({'email':email})
    folder = user["folders"]
    urls = user["urls"]
    if url not in urls:
        folder.append( (url,title,date) )
        urls = user["urls"]
        urls.append(url)
        db.summarize.update({"email":email},{"$set":{"folders":folder,"urls":urls}})
        return "Your URL has been successfully saved!"
    else:
        return "You've already saved this url!"
def remove_page(email,title,url,date):
    user = db.summarize.find_one({'email':email})
    folders = user["folders"]
    urls = user["urls"]
    print folders
    folders.pop(folders.index([url,title,date]))
    urls.pop(urls.index(url))
    db.summarize.update({"email":email},{"$set":{"folders":folders,"urls":urls}})

def has_url(url):
    check = None
    check = db.urls.find_one({'url':url})
    return check

def add_scrape(url,list,title,key_words):
    if not(has_url(url)):
        db.urls.insert({"url":url,"list":list,"title":title,"key_words":key_words})

def get_user_urls(email):
    x= db.summarize.find_one({'email':email})["folders"]
    print x
    return x


