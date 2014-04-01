#!/usr/bin/python

import sys

oldFile = None
count = 0

for line in sys.stdin:
    thisFile = line.strip()
    if oldFile and thisFile != oldFile:
        print "{0}\t{1}".format(oldFile, count)
        count = 0
    
    oldFile = thisFile
    count += 1
if oldFile != None:
    print"{0}\t{1}".format(oldFile, count)
