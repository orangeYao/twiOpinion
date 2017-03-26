# Named info_twitter_get_id.py
import twitter
import time
import os

def writeList(thelist, fileName):
    thefile = open(fileName, 'w')
    for item in thelist:
      thefile.write("%s\n" % item)

def getFollower(username, path, followFriend, outputtingName): 
    config = {}
    execfile("config.py", config)
    twitterLocal = twitter.Twitter(auth = twitter.OAuth(config["access_token"], 
              config["access_secret"], config["consumer_key"], config["consumer_secret"]))

    if followFriend == "net":
        query = twitterLocal.friends.ids(screen_name = username)
        friends_list = query["ids"]
        id_name_dict = {}

        for n in range(0, len(friends_list), 100):
            ids = friends_list[n:n+100]
            subquery = twitterLocal.users.lookup(user_id = ids)
            for user in subquery:
                id_name_dict.update({user['id']: user['screen_name']})
        print id_name_dict

        id_list = []
        for friend in friends_list:
            time.sleep(61)
            friends_list2 = twitterLocal.friends.ids(user_id = friend)["ids"]
            intersect = list(set(friends_list) .intersection(friends_list2))
            print intersect
            for friend2 in intersect:
                if friend in id_name_dict and friend2 in id_name_dict:
                    id_list.append(str(id_name_dict[friend]) + " pp " + str (id_name_dict[friend2]))
            writeList(id_list, outputtingName)

    else:
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

            if followFriend == "followers":
                writeList(id_list, outputtingName)
            elif followFriend == "friends":
                writeList(id_list, outputtingName)

            cursor = query["next_cursor"]
            time.sleep(61)
