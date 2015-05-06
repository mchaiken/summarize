#import re, google, urllib
import re

EXP = '''[^\s.\"?] (([A-Z]\w+ )+)'''

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
    prop_nouns = re.findall(EXP,text)
    for x in prop_nouns:
        if x[0] in c.keys():
            c[x[0]] +=1
        else:
            c[x[0]]=1
    print c
    for x in l:
        punc = '''()!,?.\n:\;"'''
        while (x[0] in punc) or (x[len(x)-1] in punc):
                x = x.strip(punc)
        if x.islower() and len(x) > 3:
            if x in c.keys():
                c[x]+=1
            else:
                c[x]=1
    for x in c.keys():
        if c[x] < 3:
            c[x] = 0

    return c


def get_key_phrases(text):
    l =text.split(" ")
    c={}
    for x in range(0,len(l)-1):
        phrase = l[x].strip("()!,?.\n:")+" "+l[x+1].strip("()!,?.\n:")
        #x=x.strip("()!,?.\n:;");
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
    #key_phrases= get_key_phrases(text)
    key_words= get_key_words(text)
    print key_words
    for para in paras:
        paradict[para]=0
        l=para.split(" ")
        prop_nouns = re.findall(EXP,para)
        for x in range(0,len(l)-1):
            #phrase = l[x].strip("()!,?.\n:")+" "+l[x+1].strip("()!,?.\n:")
            punc = '''()!,?.\n:\"'''
            word = l[x]
            while (word[0] in punc) or (word[len(word)-1] in punc):             
                word = word.strip(punc)
            if word.islower() and len(str(word)) > 3:
                #print word
                if word in key_words.keys():
                    paradict[para]+=(key_words[word])
        for x in prop_nouns:
            paradict[para] += (key_words[x[0]])
        #print para + "\n~~~~~~~~~~~~~~~~~"
        print paradict[para]
    print paradict.values()



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
    #print minScore
    for x in dict.keys():
        if dict[x] >= minScore:
            #pass
            print x + "\n"

findNMostCommon(get_paragraph_points(open("communist.txt",'r').read()), 3)
