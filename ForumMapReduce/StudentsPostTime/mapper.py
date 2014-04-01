#!/usr/bin/python

#Mapper

import sys
import csv
import re

date_regex = re.compile(r'\W')
reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)

for line in reader:
    if len(line) != 19 or line[0] == 'id':
        continue
    
    date = re.split(date_regex, line[8])
    print "{0}-{1}".format(line[3], date[3])
