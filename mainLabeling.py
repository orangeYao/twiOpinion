#!/usr/bin/env python
import time
import os
import subprocess
import functions

def mode1(tweets):
    trainingSet = []

def mode2(tweets):

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
            ) or 1

    if mode == 1:
        mode1(tweets)
    if mode == 2:
        mode2(tweets)


