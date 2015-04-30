#import re, google, urllib
import re



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
    #exp = '''[^\s.\"?] ([A-Z]\w+)'''
    #accounting for second word
    exp = '''[^\s.\"?] ([A-Z]\w+( [A-Z]\w+)?)'''
    prop_nouns = re.findall(exp,text)
    pn={}
    for x in prop_nouns:
        if x[0] in pn.keys():
            pn[x[0]] +=1
        else:
            pn[x[0]]=1
    print pn        
    for x in l:
        x=x.strip("()!,?.\n:");
        if x in c.keys():
            c[x]+=1
        else:
            c[x]=1
    counter = 25
    for x,y in sorted(c.iteritems(), key=lambda item: -item[1]):
            if (counter > 0) & (len(str(x)) > 4 or (str(x) in pn.keys())):
            #print str(x),str(y)+"\n"
                counter-=1
    print c
    return c


def get_key_phrases(text):
    l =text.split(" ")
    c={}
    for x in range(0,len(l)-1):
        phrase = l[x].strip("()!,?.\n:")+" "+l[x+1].strip("()!,?.\n:")
        #x=x.strip("()!,?.\n:");
        if phrase in c.keys():
            c[phrase]+=1
        else:
            c[phrase]=1
    counter = 25
    # for x,y in sorted(c.iteritems(), key=lambda item: -item[1]):
    #  if (counter > 0) & (len(str(x)) > 4 or str(x).isupper()):
    #       #print str(x),str(y)+"\n"
    #       counter-=1
    #print c
    return c
def get_paragraph_points(text):
    paras = text.split("\n\n")
    paradict={}
    key_phrases= get_key_phrases(text)
    key_words= get_key_words(text)
    print key_words
    for para in paras:
        paradict[para]=0
        l=para.split(" ")
        for x in range(0,len(l)-1):
            phrase = l[x].strip("()!,?.\n:")+" "+l[x+1].strip("()!,?.\n:")
            word = l[x].strip("()!,?.\n:")
            if phrase in key_phrases.keys():
                paradict[para]+=(key_phrases[phrase]*5)
            elif word in key_words.keys():
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


