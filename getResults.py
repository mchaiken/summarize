import re, google, urllib
from bs4 import BeautifulSoup, SoupStrainer


def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;

def findMostCommon(dict, content):
    most_common_key = ""
    most_common_count = 0;
    for key in dict.keys():
        if dict[key] > most_common_count and key.lower()[:len(key)-1] not in content.lower():
            most_common_key = key
            most_common_count = dict[key]
    #print most_common_name.lower()
    #print content_words.lower()
    return most_common_key

def findWho(text, content):
    names = {}
    regex = "([A-Z]\w*|Mr.|Mrs.|Ms.|Dr|Sir.)\s([A-Z]\w*\s?)+"
    for match in re.finditer(regex, text):
        addToDict(match.group(),names)
    return names
#return findMostCommon(names, content)

def findWhen(text, content):
    dates = {}
    regex = "(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{1,4}( BC| AD|)?"
    for match in re.finditer(regex, text):
        addToDict(match.group(),dates)
    return findMostCommon(dates, content)

def findWhere(google_results, content):
    locations=["street","alley","avenue","place","st","drive","ave","manor","house","school","tower","building","road","city","state","nation"]
    regex="((\d{1,4}\w?) [A-Z]\w+ ([A-Z]\S+ )+)"
    results = re.findall(regex,google_results)
    answers={}
    print results
    for result in results:
        loc=False;
        for word in result[0].split(" "):
            if word.lower() in locations:
                loc=True
        if loc:
            addToDict(result[0],answers)
    print answers
    return findMostCommon(answers,content)



f=findWho(open("communist.txt",'r').read(),"")
#print f
#r=findMostCommon(f,"")
#print r


def search_query(question):
    question_word= (question.split(" ")[0]).lower()
    content_words=" ".join(question.split(" ")[1:])
    g= google.search(question, num=20, stop=20)
    search_results=""
    only_p= SoupStrainer("p")

    for result in g:
        search_results += BeautifulSoup(urllib.urlopen(result),parse_only=only_p).get_text()
        #print search_results

    response=""
    if question_word == "who":
        response = findWho(search_results,content_words)
    elif question_word == "where":
        response = findWhere(search_results, content_words)
    elif question_word == "when":
        response = findWhen(search_results,content_words)
    return response
def get_key_words(text):
    l =text.split(" ")
    c={}
    for x in l:
        x=x.strip("()!,?.\n:");
        if x in c.keys():
            c[x]+=1
        else:
            c[x]=1
    counter = 25
    for x,y in sorted(c.iteritems(), key=lambda item: -item[1]):
            if (counter > 0) & (len(str(x)) > 4 or str(x).isupper()):
            #print str(x),str(y)+"\n"
            counter-=1
    return c

def get_paragraph_points(text):
    paras = text.split("\n")
    paradict={}
    key_words= get_key_words(text)
    for para in paras:
        paradict[para]=0
        for word in para.split(" "):
            if word in key_words.keys():
                paradict[para]+=key_words[word]
    for para in paradict.keys():
        #paradict[para]/=len(para.split(" "))
        print para + " " +str(paradict[para])
        print "\n"

    return paradict

print findMostCommon(get_paragraph_points(open("communist.txt",'r').read()), "")


