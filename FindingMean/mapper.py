#!/usr/bin/python
#Mapper

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 6:
        continue
    
    date, time, store, category, cost, paymanet = data
    date = datetime.strptime(date, "%Y-%m-%d")
    print "{0}\t{1}".format(date.weekday(), cost)
