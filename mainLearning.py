#!/usr/bin/env python
#copied from zhiyao@combo: /home/zhiyao/FYPstart/largeTestData
#only library in sklearnClassify included currently
import functions
import sklearnClassify
import pandas as pd
import random
import datetime

numberForTraining = 4000
numberForTesting = 400
numberUsedAll = numberForTraining + numberForTesting

path = './output/' 
input_list, input_score = functions.readTestComment(path, numberUsedAll) 

pathTweet = './output/unknownHead.csv'
tweets = functions.readManyStrings(pathTweet)
tweets = tweets[0: 2000]


randomSelect = random.sample(xrange(len(input_score)), numberUsedAll)
input_list = [input_list[i] for i in randomSelect]
input_score = [input_score[i] for i in randomSelect]

print "Size of positive training set:"
print input_score.count("1")
print "Size of negative training set:"
print input_score.count("-1")


print "in filtering process..."
filtered, freq_words = functions.useFilter(input_list, True)
f_tweets = functions.useFilter(tweets, False)

print f_tweets[0:5]

raw = functions.formRawDict(filtered, input_score)
df = pd.DataFrame(raw)
wordList = list(df.itertuples(index = False, name = None))
wordList = functions.filterZeroScore(wordList)


accuracy0 = []
accuracy1 = []
accuracy2 = []
for i in range(1,5):
    print i
    random.shuffle(wordList)
    wordList = wordList[0:numberUsedAll]
    trainingList = wordList[:numberForTraining]     #before index
    #trainingList2 = wordList[numberUnlabeled:numberForTraining] 
    testList = wordList[numberForTraining:]

    accuracy0.append(sklearnClassify.bayes(filtered, input_score, numberForTraining, 'BernoulliNB', f_tweets))
    print ""
    accuracy1.append(sklearnClassify.bayes(filtered, input_score, numberForTraining, 'MultinomialNB', f_tweets))
    print ""
    accuracy2.append(sklearnClassify.svm(filtered, input_score, numberForTraining, f_tweets))
    print "end test"
    print ""

print sum(accuracy0)/len(accuracy0)
print sum(accuracy1)/len(accuracy1)
print sum(accuracy2)/len(accuracy2)
