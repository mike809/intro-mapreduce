#!/usr/bin/python

import sys
import heapq

old_student = None
old_hour = None
count = 0
student_hours = []

for line in sys.stdin:
    student, hour = line.split('-')
    
    if old_student != student and old_student != None:
        if count != 0:
            heapq.heappush(student_hours, (-count, old_hour))

        print "{0}\t{1}".format(old_student, heapq.heappop(student_hours)[1])
        student_hours = []
        count = 0
        
    elif old_hour != hour and old_hour != None:
        heapq.heappush(student_hours, (-count, old_hour))
        count = 0
    
    count += 1
    old_hour = hour
    old_student = student
                      
