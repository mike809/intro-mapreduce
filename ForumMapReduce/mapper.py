#!/usr/bin/python

#Mapper

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)

for line in reader:
    if len(line) == 5:
        output = "{0}-A\t".format(line[0]) + "\t".join(line[1:])
        print output.strip()
    elif len(line) == 19:
        output = "{0}-B\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}".format(line[3], line[0], line[1], line[2], *line[5:10]).replace("\n", '\N').strip()
        if output:
            print output
    else:
        continue


