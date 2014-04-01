#!/usr/bin/python

import sys

student = None

for line in sys.stdin:
    if line.strip() == '':
        continue

    data = line.strip().split('\t')
    id, type =  data[0].split('-')
    
    if type == 'A':
        student = data[1:]
        continue
    
    print "{0}\t".format(id) + "\t".join(data[1:] + student)

