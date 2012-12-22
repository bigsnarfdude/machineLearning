#! /usr/bin/env python
# encoding: utf-8

import sys, os
import re, string

from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer


############################################################
#
# this is the section that takes the data and process the
# incoming data in a selection of features and category
#
############################################################

feature_count = {}
category_count = {}
    

def train_from_data(data):
    for category, documents in data.items():
        for doc in documents.split():
            train(doc, category)
    #print feature_count

def train(item, category):
    features = get_features(item)
    for f in features:
        increment_feature(f, category)
    increment_cat(category)

def increment_feature(feature, category):
    feature_count.setdefault(feature,{})
    feature_count[feature].setdefault(category, 0)
    feature_count[feature][category] += 1

def increment_cat(category):
    category_count.setdefault(category, 0)
    category_count[category] += 1
    


############################################################
#
# calculating scores functions below
#
############################################################

def probability(item, category):
    """
    probability: prob that an item is in a category
    """
    category_prob = get_category_count(category) / sum(category_count.values())
    return document_probability(item, category) * category_prob

def get_category_count(category):
    if category in category_count:
        return float(category_count[category])
    else:
        return 0.0

def document_probability(item, category):
    features = get_features(item)
    p = 1
    for feature in features:
        print "%s - %s - %s" % (feature, category, weighted_prob(feature, category))
        p *= weighted_prob(feature, category)
    return p
    
#def get_features(document):
 #   all_words = word_tokenize(document)
  #  all_words_freq = FreqDist(all_words)         
  #  print sorted(all_words_freq.items(), key=lambda(w,c):(-c, w))
  #  return all_words_freq

def get_features(document):
    document = re.sub('[%s]' % re.escape(string.punctuation), '', document) # removes punctuation
    document = document.lower() # make everything lowercase
    all_words = [w for w in word_tokenize(document) if len(w) > 3 and len(w) < 16]
    p = PorterStemmer()
    all_words = [p.stem(w) for w in all_words]
    all_words_freq = FreqDist(all_words)
    print sorted(all_words_freq.items(), key=lambda(w,c):(-c, w))
    return all_words_freq
    
def get_feature_count(feature, category):
    if feature in feature_count and category in feature_count[feature]:
        return float(feature_count[feature][category])
    else:
        return 0.0
        
def feature_prob(f, category): # Pr(A|B)
    if get_category_count(category) == 0:
        return 0
    return (get_feature_count(f, category) / get_category_count(category))
    
def weighted_prob(f, category, weight=1.0, ap=0.5):
    basic_prob = feature_prob(f, category)
    totals = sum([get_feature_count(f, category) for category in category_count.keys()])
    w_prob = ((weight*ap) + (totals * basic_prob)) / (weight + totals)
    return w_prob
        
data={"shakespeare":"Anon good nurse Speak Thou art dead no physician art can save you Dost thou know the time We must leave ere daybreak I fain would bake Mr Love cookies if I could get you cheated Fie upon it fie Are you mad Hark to the owl Hark The herald angels sing Get thee hence beggar We must hence before the army arrives Hie thee hence or lose your life Come hither young lad Look to the east thither doth the sun arise He hath killed many a man He hath a horse Lucius ho Mark my words He says I should respond quickly marry I want to I prithee answer the question Hence thou saucy boy Sirrah bring the letter over here When will I see thee next Thou art a villain Thy name is more hateful than thy face Whence came that news Return to whence you came Wherefore dost thou leave Romeo Romeo wherefore art thou Romeo why cant you be someone else whomy","attwood":"We reach the first barrier which is like the barriers blocking off roadworks or dug up sewers a wooden crisscross painted in yellow and black stripes a red hexagon which means Stop Near the gateway there are some lanterns not lit because it isnt night Above us I know there are floodlights attached to the telephone poles for use in emergencies and there are men with machine guns in the pillboxes on either side of the road I dont see the floodlights and the pillboxes because of the wings around my face I just know they are there Behind the barrier waiting for us at the narrow gateway there are two men in the green uniforms of the Guardians of the Faith with the crests on their shoulders and berets two swords crossed above a white triangle The Guardians arent real soldiers They are used for routine policing and other menial functions digging up the Commander  Wife  garden for instance and they are either stupid or older or disabled or very young apart from the ones that are Eyes incognito"}

your_words = "I got into trouble a while ago for saying that I thought the internet led to increased literacy people scolded me about the shocking grammar to be found online but I was talking about fundamentals quite simply you can not use the net unless you can read"

train_from_data(data)

shakespeare_score = probability(your_words, "shakespeare")
attwood_score = probability(your_words, "attwood")

print "This is your words scored against Shakespeare", shakespeare_score
print "This is your words scored against Margaret Attwood", attwood_score

