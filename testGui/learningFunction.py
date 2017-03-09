import functions
import sklearnClassify
import pandas as pd
import random

def learnfunction(path, pathTweet, numberUsedAll, numberUnlabeled, algorithm): 
    numberForTraining = int (0.8 * numberUsedAll)
    numberForTesting = int (0.2 * numberUsedAll)
    input_list, input_score = functions.readTestComment(path, numberUsedAll) 

    tweets = functions.readManyStrings(pathTweet)

    randomSelect = random.sample(xrange(len(input_score)), numberUsedAll)
    input_list = [input_list[i] for i in randomSelect]
    input_score = [input_score[i] for i in randomSelect]

    filtered, freq_words = functions.useFilter(input_list, True)
    f_tweets = functions.useFilter(tweets, False)
    f_tweets = f_tweets[0:numberUnlabeled]

    raw = functions.formRawDict(filtered, input_score)
    df = pd.DataFrame(raw)
    wordList = list(df.itertuples(index = False, name = None))
    wordList = functions.filterZeroScore(wordList)

    accuracy = []
    support = []
    not_support = []
    for i in range(1,5):
        print i
        random.shuffle(wordList)
        wordList = wordList[0:numberUsedAll]
        trainingList = wordList[:numberForTraining]
        testList = wordList[numberForTraining:]

        if algorithm == 3:
            accur, suppor, not_suppor = sklearnClassify.bayes(filtered, input_score, numberForTraining, 'BernoulliNB', f_tweets)
        elif algorithm == 2:
            accur, suppor, not_suppor = sklearnClassify.bayes(filtered, input_score, numberForTraining, 'MultinomialNB', f_tweets)
        elif algorithm == 1:
            accur, suppor, not_suppor = sklearnClassify.svm(filtered, input_score, numberForTraining, f_tweets)

        accuracy.append(accur)
        support.append(suppor)
        not_support.append(not_suppor)
        print ""

    ac = str(sum(accuracy)/len(accuracy))
    sp = str(sum(support)/len(support))
    nsp = str(sum(not_support)/len(not_support))
    print ac + " " + sp + " " + nsp 
    return ac, sp, nsp 

