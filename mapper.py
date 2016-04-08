#!/usr/bin/env python
import sys, time

def parseRecords():
    for line in sys.stdin:
	line=line.strip('\n').split(',')
        yield line[2]

def mapper():
    for words in parseRecords():
	w=float(words)/60.0
        print '%s\t%s' % (w,1)

if __name__=='__main__':
    mapper()
