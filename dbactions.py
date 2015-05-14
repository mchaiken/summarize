from pymongo import Connection


#mongo setup
conn = Connection()
db = conn["summarize"]

#inserts the user's fb id and username into the collection
def register_user(user_name,passwd):
    db.users.insert({"name":user_name , "passwd":passwd, "folders":[]})
    return True


#True if user has registered through fb, False otherwise
def isRegistered(user_name):
    results = db.users.find({"name":user_name})
    i=0
    for result in results:
        i+=1
    if i == 1:
        return True
    return False

def user_exists(email, user_type, db):
    check = None
    if user_type == "tutee":
        check = db.tutees.find_one({'email':email})
    else:
        check == db.tutor.find_one({'email':email})
    if check:
        return True
    return False

def authenticate(user_name, password):

    user = db.summarize.find_one( { 'user_name' : user_name })  
    if user == None:
        return None
    passwd = user["passwd"]
   
   
    if passwd == password:
        return user
    else:
        
        return None






