#!/usr/bin/env python
# encoding: utf-8

import sys, os
import csv
import time
import numpy
from Pycluster import *

data = {}
all_tags = []
all_urls = []
numerical_data = []
filename = "/Users/antigen/dev/ml_class/intro_web_data/links.csv"
clustered_urls = {}
clustered_tags = {}
i = 0


def load_data(filename):
    fh = csv.reader(open(filename, 'r'))
    for row in fh:
        data[row[0]] = row[1].split(',')
    return data

def process_urls_tags(data, all_urls, all_tags):
    for url, tags in data.items():
        all_urls.append(url)
        all_tags.extend(tags)
    all_tags = list(set(all_tags))
    return all_tags

def create_vectors(data, all_tags):
    for url, tags in data.items():
        v = []
        for t in all_tags:
            if t in tags:
                v.append(1)
            else:
                v.append(0)
        numerical_data.append(tuple(v))
    vectors = numpy.array(numerical_data)
    return vectors

def cluster_items(vectors):
    # kcluster(data, nclusters=20, dist='e') # euclidean distance
    # kcluster(data, nclusters=20, dist='b',npass=10) #city-block distance
    labels, error, nfound = kcluster(vectors, nclusters=30, dist='a', npass=10)
    print "just before the return"
    return labels

def print_data(labels, all_urls, clustered_urls, i):
    for url in all_urls:
        clustered_urls.setdefault(labels[i], []).append(url)
        clustered_tags.setdefault(labels[i], []).extend(data[url])
        i += 1
        
    for cluster_id, urls in clustered_urls.items():
        print cluster_id
        print urls

    # for cluster_id,tags in clustered_tags.items():
    #     print cluster_id
    #     print list(set(tags))


data        = load_data(filename)
processed   = process_urls_tags(data, all_urls, all_tags)
vectors     = create_vectors(data, all_tags)
labels      = cluster_items(vectors)
printed     = print_data(labels, all_urls, clustered_urls, i)




    
    

