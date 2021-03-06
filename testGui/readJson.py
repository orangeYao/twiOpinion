import re
import json
import sys
from pprint import pprint
from random import randint
from nltk import PorterStemmer
from nltk import FreqDist
from nltk.corpus import stopwords
stop = stopwords.words('english')
from guess_language import guessLanguage  #in local

from optparse import OptionParser
parser = OptionParser()
wanted_keys = ['statuses_count', 'followers_count', 'friends_count', 'screen_name', 'created_at', 'location']

def is_ascii(text): #true means normal string, false needs handle
    if isinstance(text, unicode):
        try:
            text.encode('ascii')
        except UnicodeEncodeError:
            return False
    else:
        try:
            text.decode('ascii')
        except UnicodeDecodeError:
            return False
    return True

def filter(text):
    #get rid stop word, puctuation, number, turn to lower case and check spelling, also stemming
    return_list = []
    for i in re.split("[,. \-!?:_'%$/#@&;\n\d]+", text):
        j = i.lower()
        if not is_ascii(j):
            j = j.encode('ascii','ignore')
            #print j
        if len(j) > 1 and (j not in stop) and (len(j) > 3):
            k = PorterStemmer().stem_word(j)
            if isinstance(k, unicode):
                k = k.encode('ascii','ignore')
            if (not k.isdigit()):
                return_list.append(k)
    return return_list


def main(fileNameIn):
    count = 0;
    f = open(fileNameIn[0:-5] + "_Fetched.txt", 'w')
    f2 = open(fileNameIn[0:-5] + "_Fetched.json", 'w')

    for line in open(fileNameIn, 'r'):
        try:
            loaded = json.loads(line)
            tweet = loaded.get("text")
        except ValueError:
            #print "valueError cateched!"
            continue
        if type(tweet) is unicode: 
            tweet = re.sub(r'RT @.*?: ' ,'',tweet)
            tweet = re.sub(r'http\S+', '', tweet)
            tweet = re.sub(r'\n', '', tweet)
            if guessLanguage(tweet) == 'en':
                if is_ascii(tweet):
                    f.write(tweet + '\n')
                    count += 1

                    f2_dict = {}
                    f2_dict["text"] = tweet
                    for key in wanted_keys: 
                        f2_dict[key] = loaded["user"].get(key)
                    json.dump(f2_dict, f2)
                    f2.write('\n')
    return count
