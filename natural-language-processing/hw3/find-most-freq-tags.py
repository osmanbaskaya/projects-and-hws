#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""
import sys
import gzip
from itertools import izip
from collections import defaultdict as dd

files = map(gzip.open, sys.argv[1:])
#dataset = sys.argv[1].split('.')[0]

d = dd(lambda: dd(int))

for tok_line, pos_line in izip(*files):
   for tok, pos in izip(tok_line.split(), pos_line.split()):
       d[tok][pos] += 1

for key, val in d.iteritems():
    most_freq_tag = max(val, key=lambda x: val[x])
    print "{}\t{}".format(key, most_freq_tag)
    #print "{}\t{}\t{}".format(key, most_freq_tag, val[most_freq_tag])
    #print "\n".join(map(str, val.values()))

print >> sys.stderr, "-" * 10
pos_dict = dd(int)
for tok, val in d.iteritems():
    for pos, c in val.iteritems():
        if c == 1:
            pos_dict[pos] += 1

for tok, val in pos_dict.iteritems():
    print >> sys.stderr, "{}\t{}".format(tok, val)

