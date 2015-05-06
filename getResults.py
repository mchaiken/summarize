#import re, google, urllib
import re, operator

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
<<<<<<< HEAD
def get_paragraph_points(paras):
    paradict={}
    #key_phrases= get_key_phrases(text)
    key_words= get_key_words(" ".join(paras))
    print key_words
=======
def get_paragraph_points(text):
    paras = text.split("\n\n")
    paralist = []
    #key_phrases= get_key_phrases(text)
    key_words= get_key_words(text)
    #print key_words
    pos = 0
>>>>>>> 7827dd3fe4aaa46561d55cfbdc97654cd0f4c8d5
    for para in paras:
        l=para.split(" ")
<<<<<<< HEAD
        prop_nouns = re.findall(EXP,para)
=======
        exp = '''[^\s.\"?] ([A-Z]\w+( [A-Z]\w+)?)'''
        prop_nouns = re.findall(exp,para)
        count = 0
>>>>>>> 07c85f3a8f4d8dd73aac2607971cc286846b4a91
        for x in range(0,len(l)-1):
            #phrase = l[x].strip("()!,?.\n:")+" "+l[x+1].strip("()!,?.\n:")
            punc = '''()!,?.\n:\"'''
            word = l[x]
            while (word[0] in punc) or (word[len(word)-1] in punc):             
                word = word.strip(punc)
            if word.islower() and len(str(word)) > 3:
                #print word
                if word in key_words.keys():
                    count += key_words[word]
        for x in prop_nouns:
            count += key_words[x[0]]
        pos += 1
        paralist.append( (count,para,pos))
     #print para + "\n~~~~~~~~~~~~~~~~~"
    print paralist
    return sorted( paralist, reverse = True)    



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

<<<<<<< HEAD
#findNMostCommon(get_paragraph_points(open("communist.txt",'r').read().split("\n\n")), 3)
=======
<<<<<<< HEAD
findNMostCommon(get_paragraph_points(open("communist.txt",'r').read()), 3)
=======
#findNMostCommon(get_paragraph_points(open("communist.txt",'r').read()), 3)
>>>>>>> 7827dd3fe4aaa46561d55cfbdc97654cd0f4c8d5


>>>>>>> 07c85f3a8f4d8dd73aac2607971cc286846b4a91
