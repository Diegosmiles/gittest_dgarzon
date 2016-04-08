#!/usr/bin/env python
import itertools, operator, sys

def parsePairs():
    for line in sys.stdin:
        var1= tuple(line.strip('\n').split('\t'))
	yield(float(var1[0]),float(var1[1]))

def reducer():
    for key, pairs in itertools.groupby(parsePairs(),
                                        operator.itemgetter(0)):
        count = sum(int(i[1]) for i in pairs)
        print '%i\t%i' % (key, count)

if __name__=='__main__':
    reducer()
