# Named info_twitter_get_id.py
import twitter
import time
import os

def writeList(thelist, fileName):
    thefile = open(fileName, 'w')
    for item in thelist:
      thefile.write("%s\n" % item)

def getFollower(username, path, followFriend): 
    config = {}
    execfile("config.py", config)
    twitterLocal = twitter.Twitter(auth = twitter.OAuth(config["access_token"], 
              config["access_secret"], config["consumer_key"], config["consumer_secret"]))
    cursor = -1
    id_list = []
    while(cursor != 0):
        if followFriend == "followers":
            query = twitterLocal.followers.ids(screen_name = username, cursor = cursor) 
        elif followFriend == "friends":
            query = twitterLocal.friends.ids(screen_name = username, cursor = cursor) 
        else:
            print "Error: neither followers and friends"

        print query["ids"][0]
        print "found %d followers/friends" % (len(query["ids"]))

        if not os.path.exists(path):
            os.makedirs(path)

        id_list.extend(query["ids"])
        writeList(id_list, path + "/" + username + ".txt")
        cursor = query["next_cursor"]
        time.sleep(61)
