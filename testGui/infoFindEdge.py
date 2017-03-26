# findEdge.py: ~/python/tweets/followerNetwork
import twitter 
import time
import json
import csv
import sys
reload(sys)

sys.setdefaultencoding('utf-8')
csv_has_head = False 
#wanted_keys = ['statuses_count', 'followers_count', 'friends_count', 'screen_name', 'created_at', 'location', 'lang'] 
wanted_keys = ['statuses_count', 'followers_count', 'friends_count', 'screen_name', 'created_at', 'location', 'lang', 'profile_image_url_https'] 

def readList(fileName):
    with open (fileName, 'r') as readfile:
        lineAll = readfile.read()
        lineList = lineAll.split('\n')
    del lineList[-1]
    return lineList

def writeJson(query_dict, fileName):
    global csv_has_head
    if not csv_has_head:
        outfile = csv.writer(open(fileName, 'w'))
        outfile.writerow(wanted_keys)
        csv_has_head = True
        with open(fileName, 'w') as outfile:
            json.dump(query_dict, outfile)
            outfile.write('\n')
    else:
        with open(fileName, 'a') as outfile:
            json.dump(query_dict, outfile)
            outfile.write('\n')

def writeCsv(query_dict, fileName):
    global csv_has_head
    if not csv_has_head:
        outfile = csv.writer(open(fileName, 'w'))
        outfile.writerow(wanted_keys)
        csv_has_head = True
    else:
        outfile = csv.writer(open(fileName, 'a'))
    outfile.writerow([str(query_dict[x]) for x in wanted_keys])

    
def followerInfo(usernamePath, outFormat):
    config = {}
    execfile("config.py", config)
    twitterLocal = twitter.Twitter(auth = twitter.OAuth(config["access_token"], 
                config["access_secret"], config["consumer_key"], config["consumer_secret"]))

    all_followers = readList(usernamePath)
    all_followers = map(int, all_followers)
    print "Number of lists: " + str(len(all_followers))

    for n in range(0, len(all_followers), 100):
        ids = all_followers[n:n+100]
        subquery = twitterLocal.users.lookup(user_id = ids)
        for user in subquery:
            user = dict((k, user[k]) for k in wanted_keys if k in user)
            if outFormat == ".json":
                writeJson(user, usernamePath[0:-4] + outFormat)
            elif outFormat == ".csv":
                writeCsv(user, usernamePath[0:-4] + outFormat)
            else:
                print "Error: wrong data type!"
        print user
        time.sleep(1)
