#!/usr/bin/env python
import time
import os
import subprocess
import functions
from logicalParser import nested_bool_eval

def mode1(tweets):
    result = []
    flag = "r"

    while flag == "r":
        condition_s = raw_input("Indicate the keywords (kA, kB, kC) restrictions with logic," 
                        + " for instance, kA or (kB and kC): ")
        condition_l = condition.replace("("," ").replace(")"," ").replace("and"," ").replace("or"," ").split()

        for tweet in tweets:
            for condition in condition_l:
                if condition in tweet:
                    condition_s.replace(condition, "True") 
                else:
                    condition_s.replace(condition, "False") 
            if nested_bool_eval(condition_s):
                result.append(tweet) 
        flag = raw_input(str(len(result)) + "tweets are selected, save(s) them or reselect(r)?: ") or "s" 
    functions.writeList(result1, "positive.txt")


def mode2(tweets):
    result1 = []
    result2 = []
    s = ""
    print ("Indicate how you want to deal with each tweet by typing \n"
        + "Class1(1), Class2(2), Discard(d, default), CheckProgress(c), SaveProgressAndQuit(sq), QuitWithoutSaving(q)\n") 

    count = 0
    for tweet in tweets:
        if (s == "sq" or s == "q"):
            break
        count += 1
        print "No." + str(count) + " " + tweet

        s = raw_input ("Indicate your choice among 1, 2, d, c, sq, q: ") or "d"
        if (s == "1"):
            result1.append(tweet)
        if (s == "2"):
            result2.append(tweet)

        while (s == "c"):
            print "In class1, " + str(len(result1)) + " tweets are selected."
            print "In class2: " + str(len(result2)) + " tweets are selected."
            s = raw_input ("Indicate your choice among 1, 2, d, c, sq, q: ") or "d"
            if (s == "1"):
                result1.append(tweet)
            if (s == "2"):
                result2.append(tweet)

        print ""

    if (s == "sq"):
        functions.writeList(result1, "positive.txt")
        functions.writeList(result2, "negative.txt")
        

if __name__ == "__main__":
    functions.startingInfo()
    path = "./output"
    word_to_grab = raw_input("Indicate file you want to build your category 1: " 
                            + "type the keyword you gave in previous (grabing) step.\n" 
                            + "Type \"Q\" if you wish to use your own file: ") or "China" 

    if (word_to_grab == "Q"):
        file_name = raw_input("You hope to give your own file, please indicate loaction of it: "
                    ) or (path + "/stream_" + "China" + ".txt") 
    else:
        file_name = path + "/stream_" + word_to_grab + ".txt"

    tweets = functions.readManyStrings(file_name)
    print "The file you choose is in: \"" + file_name + "\", it contains " + str(len(tweets)) + " tweets."
    print ""
    print "Now select the tweets you want in training set for catefory 1."
    mode = raw_input(
            "The two available classification mode you can select:\n"
            + "1. select by key words \n"
            + "2. select one by one manually \n"
            + "select the mode you want: "
            ) or "2" 
    print ""

    if mode == "1":
        mode1(tweets)
    if mode == "2":
        mode2(tweets)
