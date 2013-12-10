#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"


import sys
import gzip
from itertools import izip
from collections import defaultdict as dd

tok_file = gzip.open(sys.argv[1])
pos_file = gzip.open(sys.argv[2])

d = dd(lambda: dd(int))

for tok_line, pos_line in izip(tok_file, pos_file):
    for t, p in izip(tok_line.split(), pos_line.split()):
        d[t][p] += 1

for t, psos in d.viewitems():
    for p, c in psos.viewitems():
        print t, p, c
