#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys
from collections import defaultdict as dd
from math import log


lines = open(sys.argv[1]).readlines()

huffman_coding = {'a': '00', ' ': '10', 'n': '010', ',': '110', 
                  'm': '0110', 'p': '0111', 'l': '1110', 'c': '1111'}

def entropy(d):
    total = float(sum(d.values()))
    e = 0
    for key, val in d.iteritems():
        p = val / total
        e += -p * log(p, 2)
    return e

for line in lines:
    line = line[:-1]
    d = dd(int)
    s = ""
    for c in line:
        s += huffman_coding[c]
        d[c] += 1
    print s, len(s), len(s) / (float(len(line)))
    print "Entropy: {}".format(entropy(d))
