import tweetstream

# query twitter stream for specific people
with tweetstream.FilterStream(username, password, follow=people) as stream:
    for tweet in stream:
        print tweet

# query for screen names of friends
for friend in tweepy.api.friends("some_twitter_user"):
        print friend.screen_name

# queery for ID number for each friend
for friend in tweepy.api.friends("some_twitter_user"):
        print friend.id

# put it to a list
friend_list=[]
for friend in tweepy.api.friends("some_twitter_user"):
        friend_list.append(friend.id)

# all locations not NoneType
for follower in tweepy.api.followers("some_twitter_user"): 
    if isinstance(follower.location, types.NoneType):
        pass
    else:
        print follower.name, repr(follower.location)

# printing homophobic tweets
with tweetstream.FilterStream(username, password, track=["faggot","homo", "fag"]) as stream:
    for tweet in stream:
        print tweet['text']

# counter for homophobic tweets per minute?
with tweetstream.FilterStream(username, password, track=["faggot","homo", "fag"]) as stream:
    for tweet in stream:
        print tweet['text']
        print 20*"*", count
        count +=1


import codecs
with tweetstream.FilterStream(username, password, track=["didn't get"]) as stream:
    for tweet in stream:
        print 20*"*", count
        count +=1
        print tweet['text']
        #document = re.sub('[%s]' % re.escape(string.punctuation), '', tweet['text'])
        #print document
        with codecs.open('tweet_christmas3', mode='at', encoding='utf-8') as f:
            f.write(tweet['text']+'|')


# same version above with tweetstream
#!/usr/bin/env python

import tweetstream
import pymongo

connection = pymongo.Connection("localhost", 27017)
db = connection.election

username = "hahaha_nice_try"
password = "************"
words = ["iPhone", "iPad", "MacBook"]
with tweetstream.FilterStream(username, password, track=words) as stream:
    for tweet in stream:
        db.tweets.save(tweet)


