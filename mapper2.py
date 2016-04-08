#!/usr/bin/env python
import sys
import heapq

def mapper(k):
    for w in sys.stdin:
	new_line=w.strip().split()
	print (new_line[0],new_line[1])

if __name__=='__main__':
    mapper(3)
