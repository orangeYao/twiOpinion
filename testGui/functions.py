import re
from nltk import PorterStemmer
from nltk import FreqDist
from nltk.corpus import stopwords
stop = stopwords.words('english')
import csv
import json

def startingInfo():
    with open ("startingInfo.txt", "r") as myfile:
        data=myfile.read()
    print data

    print "Welcome to twiOpinion 0.1.3!"
    print "This is interactive version"
    print ""

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

def concat(dct1, dct2):
	concat = dct1.copy()
	concat.update(dct2)
	return concat

def formRawDict(filtered, input_score):
	dct1 = {'comment': filtered}
	dct2 = {'score': input_score}
	return concat(dct1, dct2)	


def filter(text, removeWords):
    #get rid stop word, puctuation, number, turn to lower case and check length, also stemming
    return_list = []
    for i in re.split("[,. ()\- \\\\s =\n-\!?#:_'%$/@\"]+",text):
        j = i.lower()

        # remove words like 'votetrump', 'votehillary'
        removeList = removeWords.lower().replace(" ", "").split(",")
        for remove_element in removeList:
            j = j.replace(remove_element, '')

        if len(j) > 1 and is_ascii(j) and (j not in stop):
            k = PorterStemmer().stem_word(j)
            #k = PorterStemmer().stem(j) nltk3.2.2
            if isinstance(k, unicode):
                k = k.encode('ascii','ignore')
            if (not k.isdigit()):
                return_list.append(k)
    return return_list


def freqWord(word_list):
    all_words = FreqDist(word_list)
    return [i[0] for i in all_words.most_common(2000)]

def useFilter(string_list, need_freq, removeWords):
    #returns filtered as list of string, also return the most common words
    return_text = []
    return_list = []
    n = 0
    for string in string_list:
        filtered = filter(string, removeWords)
        return_text.append(' '.join(filtered))
        if need_freq is True:
            return_list = return_list + filtered
        n = n + 1
        if n % 3000 == 0:
            print n

    if need_freq is True:
        return return_text, freqWord(return_list)
    else:
        return return_text

	
def filterZeroScore(word_list):
    # filter (string, score) in which score == ' 0'
    filtered_list =  [x for x in word_list if (x[1].replace(' ','') != '0')]
    print "number of filtered comments"
    print len(word_list) -  len(filtered_list)
    return filtered_list 


def filterZeroSeperately(input_list, input_score):
    # filter score list with label ' 0' and corresponding string list
    index_list = [i for i,x in enumerate(input_score) if x.replace(' ','') == '0'] 
    input_score = [i for i in input_score if input_score.index(i) not in index_list]
    input_list = [i for i in input_list if input_list.index(i) not in index_list]
    return input_list, input_score

def readTestComment(path, numberForTraining):
    ## change here
    # used for reading a test set in nltk
    input_list = []
    score_list = []
    count = 0
    with open(path + 'positive.txt') as f:
        for line in f:
            if count < numberForTraining/2:
                input_list.append(line.rstrip())
                score_list.append('1')
                count += 1
    f.close()

    with open(path + 'negative.txt') as f1:
        for line in f1:
            if count < numberForTraining:
                input_list.append(line.rstrip())
                score_list.append('-1')
                count += 1
    f1.close()
    return input_list, score_list


def readManyStrings(path):
    input_list = []
    with open(path, 'r') as f:
        for line in f:
            input_list.append(line)
    return input_list


def readManyJsons(path):
    input_list = []
    with open(path, 'r') as f:
        for line in f:
            input_list.append(json.loads(line))
    return input_list

def writeList(listname, filename):
    f = open(filename, "w")
    count = 0;
    for line in listname:
        f.write(line + '\n')
        count += 1
    return count

def simpleWriteList(listname, filename):
    f = open(filename, "w")
    for line in listname:
        f.write(line)

def simpleWriteJson(listname, filename):
    outfile = open(filename, 'w')
    for query_dict in listname:
        json.dump(query_dict, outfile)
        outfile.write('\n')


def simpleWriteJsonText(listname, filename):
    outfile = open(filename, 'w')
    for query_dict in listname:
        outfile.write(query_dict["text"]+'\n')


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search



