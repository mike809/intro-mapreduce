#!/usr/bin/python
#Reducer
import sys

count = 0
old_word = None
old_nodes = set()

for line in sys.stdin:
    data = line.strip().split('\t')
    
    if len(data) != 2:
        continue
    
    new_word, node = data
    try:
        node = int(node)
    except:
        continue

    if old_word != new_word and old_word != None:
        print '{0}\t{1}\t{2}'.format(old_word, count, sorted(old_nodes))
        old_nodes = set()
        count = 0
        
    old_word = new_word
    old_nodes.add(int(node))
    count += 1
    
if old_word != None:
    print '{0}\t{1}\t{2}'.format(old_word, count, sorted(old_nodes))

