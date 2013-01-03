#!/usr/bin/env python
# encoding: utf-8
"""
tag_clustering.py

Created by Hilary Mason on 2011-02-18.
Copyright (c) 2011 Hilary Mason. All rights reserved.
"""

import sys, os
import csv

import numpy
from Pycluster import *

class TagClustering(object):

    def __init__(self):
        tag_data = self.load_link_data()
        print tag_data
        all_tags = []
        all_urls = []
        for url,tags in tag_data.items():
            all_urls.append(url)
            all_tags.extend(tags)

        all_tags = list(set(all_tags)) # list of all tags in the space
        numerical_data = [] # create vectors for each item
        for url,tags in tag_data.items():
            v = []
            for t in all_tags:
                if t in tags:
                    v.append(1)
                else:
                    v.append(0)
            numerical_data.append(tuple(v))
        print numerical_data
        data = numpy.array(numerical_data)
        
        # cluster the items
        # labels, error, nfound = kcluster(data, nclusters=20, dist='e') # 20 clusters, euclidean distance
        # labels, error, nfound = kcluster(data, nclusters=20, dist='b',npass=10) # 20 clusters, city-block distance, iterate 10 times
        labels, error, nfound = kcluster(data, nclusters=2)
        
        # print out the clusters
        clustered_urls = {}
        clustered_tags = {}
        i = 0
        for url in all_urls:
            clustered_urls.setdefault(labels[i], []).append(url)
            clustered_tags.setdefault(labels[i], []).extend(tag_data[url])
            i += 1
            
        for cluster_id,urls in clustered_urls.items():
            print cluster_id
            print urls
        
        for cluster_id,tags in clustered_tags.items():
            print cluster_id
            print list(set(tags))
		
		
    def load_link_data(self,filename="links.csv"):
        data = {}

        r = csv.reader(open(filename, 'r'))
        for row in r:
            item = row[1:]
            temp_list=[]
            for x in item:
                temp_list.append(x.strip().strip('"'))
            data[row[0]] = temp_list
        return data
        

if __name__ == '__main__':
	t = TagClustering()

