#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
This script evaluates the pos tagging accuracy.
"""

import sys
import gzip
from itertools import izip

files = map(lambda x: gzip.open(x), sys.argv[1:])

tp = 0
total = 0
for s_line, g_line in izip(*files):
    s_line = s_line.split()
    g_line = g_line.split()
    total += len(g_line)
    for pred, gold in izip(s_line, g_line):
        if pred == gold:
            tp += 1

print "Accuracy: {}%; tp={}, total={}".format(tp / float(total) * 100, tp, total)
