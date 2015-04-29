#import re, google, urllib



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
    regex = "([A-Z]\w*|Mr.|Mrs.|Ms.|Dr.|Sir.)\s([A-Z]\w*\s?)+"
    for match in re.finditer(regex, text):
        addToDict(match.group(),names)
    return findMostCommon(names, content)



# return response
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
        if (counter > 0) & (len(str(x)) > 3 ):
            #print str(x),str(y)+"\n"
            counter-=1
    print c
    return c

def get_paragraph_points(text):
    paras = text.split("\n\n")
    paradict={}
    key_words= get_key_words(text)
    for para in paras:
        paradict[para]=0
        for word in para.split(" "):
            if word in key_words.keys():
                paradict[para]+=key_words[word]
                    # for para in paradict.keys():
        #paradict[para]/=len(para.split(" "))
        #print para + " " +str(paradict[para])
#print "\n"

    return paradict


def findNMostCommon(dict,n):
    
    most_common=[]
    for key in dict.keys():
        most_common.append((dict[key], key));
    
    minScore= sorted(most_common)[::-1][n-1:n][0][0]
    print minScore
    for x in dict.keys():
        if dict[x] >= minScore:
            print x + "\n"

findNMostCommon(get_paragraph_points(open("communist.txt",'r').read()), 3)


