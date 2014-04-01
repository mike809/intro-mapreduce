#!/usr/bin/python
#Reducer

import sys

old_weekday = None
total_per_weekday = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    
    weekday, cost = data
    
    if old_weekday != weekday and old_weekday != None:
        print "{0}\t{1}".format(old_weekday, total_per_weekday)
        total_per_weekday = 0
    
    old_weekday = weekday
    total_per_weekday += float(cost)

if old_weekday != None:
    print "{0}\t{1}".format(old_weekday, total_per_weekday)

    
