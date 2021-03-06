import functions
import sklearnClassify
import random

def learnfunction(path, pathTweet, numberUsedAll, numberUnlabeled, algorithm, removeWords): 
    numberForTraining = int (0.8 * numberUsedAll)
    numberForTesting = int (0.2 * numberUsedAll)
    input_list, input_score = functions.readTestComment(path, numberUsedAll) 

    tweets = functions.readManyStrings(pathTweet)

    randomSelect = random.sample(xrange(len(input_score)), numberUsedAll)
    input_list = [input_list[i] for i in randomSelect]
    input_score = [input_score[i] for i in randomSelect]

    filtered, freq_words = functions.useFilter(input_list, True, removeWords)
    f_tweets = functions.useFilter(tweets, False, removeWords)
    f_tweets = f_tweets[0:numberUnlabeled]

    accuracy = []
    support = []
    not_support = []
    const_repeat = 5
    for i in range(1,const_repeat):
        print i
    
        writeOut = False
        if algorithm == 4:
            if i == const_repeat-1:
                writeOut = True
            accur, suppor, not_suppor = sklearnClassify.learn(filtered, input_score, numberForTraining, 
                                    'decisionTree', f_tweets, writeOut, tweets[0:numberUnlabeled], path)
        elif algorithm == 3:
            if i == const_repeat-1:
                writeOut = True
            accur, suppor, not_suppor = sklearnClassify.learn(filtered, input_score, numberForTraining, 
                                    'BernoulliNB', f_tweets, writeOut, tweets[0:numberUnlabeled], path)

        elif algorithm == 2:
            if i == const_repeat-1:
                writeOut = True
            accur, suppor, not_suppor = sklearnClassify.learn(filtered, input_score, numberForTraining, 
                                    'MultinomialNB', f_tweets, writeOut, tweets[0:numberUnlabeled], path)

        elif algorithm == 1:
            if i == const_repeat-1:
                writeOut = True
            accur, suppor, not_suppor = sklearnClassify.learn(filtered, input_score, numberForTraining,
                                    "svm", f_tweets, writeOut, tweets[0:numberUnlabeled], path)

        accuracy.append(accur)
        support.append(suppor)
        not_support.append(not_suppor)
        print ""

    ac = str(sum(accuracy)/len(accuracy))
    sp = str(sum(support)/len(support))
    nsp = str(sum(not_support)/len(not_support))
    print ac + " " + sp + " " + nsp 
    return ac, sp, nsp 

