import re
import json
import sys
from pprint import pprint
from random import randint
from nltk import PorterStemmer
from nltk import FreqDist
from nltk.corpus import stopwords
stop = stopwords.words('english')
#from guess_language import guess_language #in combo
from guess_language import guessLanguage  #in local

from optparse import OptionParser
parser = OptionParser()

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


if __name__ == '__main__':

    parser.add_option("-i", "--fileIn", dest="fileNameIn", help="name of crawled file", metavar="FILE")
    (options, args) = parser.parse_args()

    count = 0;
    f = open(options.fileNameIn[0:-4] + "txt", 'w')
    for line in open(options.fileNameIn, 'r'):
        try:
            tweet = json.loads(line).get("text")
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
                    #print tweet.encode('utf-8')
                    #print filter(tweet)
        #else:
        #    print "In read.py!!"
        #    print type(tweet)

    sys.stdout.write(str(count))
