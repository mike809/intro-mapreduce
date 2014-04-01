#!/usr/bin/python

import sys

oldFile = None
count = 0
max_count = 0
max_file = None

for line in sys.stdin:
    thisFile = line.strip().split('/')[-1]
    if oldFile and thisFile != oldFile:
        if count > max_count:
            max_count, max_file = count, oldFile
        count = 0
    
    oldFile = thisFile
    count += 1 

if count > max_count:
    print "{0}\t{1}".format(oldFile, count)
else:
    print"{0}\t{1}".format(max_file, max_count)
