#!/usr/bin/python

import sys
import re

regexp = r'([\d\.]+) (-) (-) (\[\d{2}/\w{3}/\d{4}:(?:\d{2}:){2}\d{2} -\d{4}\]) (\"[-\w/\. ]+\") (\d{3}) ([\d-]+)'

for line in sys.stdin:
    data = re.match(regexp, line)
    if data == None:
        continue
    
    data = data.groups()
    if len(data) != 7:
        continue

    ip, identity, username, time, request, status, size = data
    print "{0}".format(ip)
    
