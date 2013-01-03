#!/usr/bin/env python
# encoding: utf-8
"""
rec.py

Created by Hilary Mason on 2011-02-18.
Modified to find linkedin profiles that are similar. @bigsnarfdude
"""

import sys
import os
import csv
import numpy
from hcluster import *

class TagClustering(object):

    def __init__(self):
        tag_data = self.load_link_data()
        all_tags = []
        all_urls = []
        for url,tags in tag_data.items():
            all_urls.append(url)
            all_tags.extend(tags)

        all_tags = list(set(all_tags)) # list of all tags in the space
        
        numerical_data = {} # create vectors for each item
        for url,tags in tag_data.items():
            v = []
            for t in all_tags:
                if t in tags:
                    v.append(1)
                else:
                    v.append(0)
            numerical_data[url] = v
        print numerical_data
        recommend_url = 'linkedin_profile_1'
        results = {}
        for url,vector in numerical_data.items():
            d = euclidean(numerical_data[recommend_url],numerical_data[url])
            results[url] = d

        for item in sorted(results.items(), key=lambda(u,s):(s, u))[0:10]:
            print item
		
		
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

