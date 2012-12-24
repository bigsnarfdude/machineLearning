#! /usr/bin/env python
# coding: utf-8


import csv
import json
import os


f = open('/Users/antigen/dev/DFTP/dataDNS.csv', 'rb')
reader = csv.DictReader( f, delimiter = ',', fieldnames = ('time','ip','port','type','answer','number') )
count = 0


for row in reader:
    out = json.dumps(row)
    os.system ("curl -XPUT http://localhost:9200/dns/nyc/" + str(count) + " -d '" + out + " '")
    count += 1
f.close()
