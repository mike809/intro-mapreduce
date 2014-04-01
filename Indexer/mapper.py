#!/usr/bin/python
#Mapper

import sys
import csv
import re

separators = re.compile(r'[ \.!,\?:;\"\(\)<>\[\]#\$\-/]')
reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)

for line in reader:
    if len(line) != 19:
        continue
    
    words = re.split(separators, line[4])
    
    for word in words:
        word = word.strip()
        if not word:
            continue

        print "{0}\t{1}".format(word.lower(), line[0])
