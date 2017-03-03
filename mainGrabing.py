#!/usr/bin/env python
import time
import os
import subprocess
import functions

def grabSetting():
    word_to_grab = raw_input("The tag or keyword you wish to grab from Twitter: ") or "China"
    #path = raw_input("The folder you wish to store information in (default as ./output): ") or "./output"

    path = "./output"
    if (path == "./output" and not os.path.exists("./output")):
        os.makedirs("./output")

    file_name = path + "/stream_" + word_to_grab + ".json"
    print "Started grabing, grabed information will be stored in " + file_name
    pw = subprocess.Popen(["python", "twitter_stream_download.py", "-q", word_to_grab, "-d", path]) 
    print ""
    return (file_name, pw)

if __name__ == "__main__":
    functions.startingInfo()
    file_name, pw = grabSetting()
    while (True):
        checkProgress = raw_input("Type in \"c\" to check number of tweets have been crawled\n"+
                                  "Type in \"f\" to fetch meaningful contents of tweets for training in next step\n"+
                                  "Type in \"s\" to fetch meaningful contents, stop current crawling process and quit: ")
        if (checkProgress == "c"):
            proc = subprocess.Popen(["wc", "-l", file_name], stdout=subprocess.PIPE)
            lines = proc.stdout.read()
            print "     " + lines.split()[0] + " tweets have been crawled"

        if (checkProgress == "f" or checkProgress == "s"):
            proc = subprocess.Popen(["python", "readJson.py", "-i", file_name], stdout=subprocess.PIPE)
            lines = proc.stdout.read()
            print "     " + lines + " lines of contents are fetched"
        print ""    

        if (checkProgress == "s"):
            pw.kill()
            break

