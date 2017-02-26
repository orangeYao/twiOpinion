from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB #naive bayes
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier #svm
from sklearn.datasets import fetch_20newsgroups
import random
import numpy as np

def svm(data, score, numberForTraining, f_tweets):
    print "svm in sklearn: "
    c = list(zip(data, score))
    random.shuffle(c)
    data, score = zip(*c)
    train_list_data = data[:numberForTraining] #before index
    train_list_target = score[:numberForTraining]

    test_list_data = data[numberForTraining:] 
    test_list_target = score[numberForTraining:]

    text_clf = Pipeline([('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2',
            alpha=1e-3, n_iter=5, random_state=42)),
        ])

    text_clf = text_clf.fit(train_list_data, train_list_target)
    predicted = text_clf.predict(test_list_data)
    accur = np.mean(predicted == test_list_target)
    print "to predict:"
    application(text_clf, f_tweets) 
    print ''
    print "in test set:"
    application(text_clf, test_list_data)
    print ''

    print accur
    return accur


def bayes(data, score, numberForTraining, c_type, f_tweets):
    print "naive bayes in sklearn:"
    c = list(zip(data, score))
    random.shuffle(c)
    data, score = zip(*c)
    train_list_data = data[:numberForTraining] #before index
    train_list_target = score[:numberForTraining]

    test_list_data = data[numberForTraining:]
    test_list_target = score[numberForTraining:]
#### seperate pipeline
    #count
    if c_type == 'BernoulliNB':
        print "BernoulliNB naive bayes in sklearn:"
        text_clf = Pipeline([('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', BernoulliNB()),
            ])
    elif c_type == 'MultinomialNB':
        print "MultinomialNB naive bayes in sklearn:"
        text_clf = Pipeline([('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
            ])
    else:
        print "####################select type of bayes filter"    
    text_clf = text_clf.fit(train_list_data, train_list_target)
    predicted = text_clf.predict(test_list_data)
    accur = np.mean(predicted == test_list_target)    

    print "to predict:"
    application(text_clf, f_tweets)
    print ''
    print "in test set:"
    application(text_clf, test_list_data)

    print "computing accurancy: " + str(accur)
    return accur


def application(text_clf,f_tweets):
    predicted = text_clf.predict(f_tweets)
    #np.savetxt("foo2.csv", predicted, delimiter="\n", fmt="%s")
    print "supporting: " + str(sum(predicted == '1'))
    print "not supporting: " + str(sum(predicted == '-1'))
    print "unlabeled: " + str(sum(predicted == '*1'))


