#!/usr/bin/env python
import itertools
import operator
import sys
import ast
import heapq

def parsePairs():
    for line in sys.stdin:
        count=line.strip('\n').translate(None,"()''").split(',')
	#count=line.tuple(line.strip('\n').split('\t').translate(None,"()''").split(','))
	yield(float(count[0]),float(count[1]))
def reducer():
    
    cumsum=0
    minutes={}
    totalsum=0
    for key, pairs in itertools.groupby(parsePairs(),
                                      operator.itemgetter(0)):
           
	minutes[int(key)]=[int(i[1]) for i in pairs][0]
	totalsum=sum(minutes.values()) 
	for i in sorted(minutes.keys()):
		cumsum+=minutes[i]
		if cumsum>=(totalsum/2.0):
			print i
			break

if __name__=='__main__':
    reducer()
