#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""

import sys
import gzip
from collections import defaultdict as dd

ngram_file1 = gzip.open(sys.argv[1])
ngram_file2 = gzip.open(sys.argv[2])

def process_ngram_file(ff):
    d = dd(lambda : dd(int))
    for line in ff:
        line = line.split()
        n = len(line) - 1
        ngram = " ".join(line[:n])
        d[n][ngram] += 1

    return d
    
ng_dict1 = process_ngram_file(ngram_file1)
ng_dict2 = process_ngram_file(ngram_file2)

total = 0
for i in xrange(1, 4):
    difference = set(ng_dict2[i].keys()).difference(set(ng_dict1[i].keys()))
    t = len(difference)
    print difference
    print "{}-gram difference is {}".format(i, t)
    total += t

print "Total ngram difference is {}".format(total)

