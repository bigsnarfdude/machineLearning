#! /usr/bin/env python

'''
this classfier finds a specific voting ring when presented with data. For example 
4 IP addresses can be voting in as voting ring. This classifier can detect them
on different articles or clumps.

This can also be used for finding IP address patterns like group of students hitting 
specific website.

This can also be used to find specific plagerised text amongst chunks of text
'''


import sys, os
import re, string
from random import randrange
from nltk import FreqDist


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
    
def get_features(document):
    all_words = document.split()
    all_words_freq = FreqDist(all_words)         
    print sorted(all_words_freq.items(), key=lambda(w,c):(-c, w))
    return all_words_freq
    
def get_feature_count(feature, category):
    if feature in feature_count and category in feature_count[feature]:
        return float(feature_count[feature][category])
    else:
        return 0.0
        
def feature_prob(f, category):
    if get_category_count(category) == 0:
        return 0
    return (get_feature_count(f, category) / get_category_count(category))
    
def weighted_prob(f, category, weight=1.0, ap=0.5):
    basic_prob = feature_prob(f, category)
    totals = sum([get_feature_count(f, category) for category in category_count.keys()])
    w_prob = ((weight*ap) + (totals * basic_prob)) / (weight + totals)
    return w_prob

# list all the attacks or voting rings below are 
data = {"1.1.1.1":"2.2.2.2 3.3.3.3 4.4.4.4",
       }

locations = { 
            }

# sliding window sampling magic
times = {
        }

account_names = {}

 
def generate_ip():
    b1 = randrange(0, 255, 1)
    b2 = randrange(0, 255, 1)
    b3 = randrange(0, 255, 1)
    b4 = randrange(0, 255, 1)
    octets = b1, b2, b3, b4
    return ".".join([str(i) for i in octets])

def make_list(number):
    ip_list = " "
    for i in range(number):
        ip_list += generate_ip() + " "
    return ip_list

# other features like time, location,  
voting_ring = "1.1.1.1 2.2.2.2 3.3.3.3 4.4.4.4"
good_ring   = make_list(10)
normal_ring = "1.1.1.1 2.2.2.2" + make_list(8) 

train_from_data(data)

bad_guy_score = probability(voting_ring, "1.1.1.1")
good_guy_score = probability(good_ring, "10.10.10.10")
normal_score = probability(normal_ring, "1.1.1.1")

print "Any score greater than zero is a probability of a voting ring"
print "*" * 50
print "I have identified voting ring", bad_guy_score
print "I know these votes are not a voting ring", good_guy_score
print "I believe these votes look normal", normal_score

