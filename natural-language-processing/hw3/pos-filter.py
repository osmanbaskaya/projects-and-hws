#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
Filter the files according to the valid_pos_set
"""
import sys
import gzip
from itertools import izip

tok_file = sys.argv[1]
pos_file = sys.argv[2]
dataset = tok_file.split('.')[0]
valid_pos_set = set(sys.argv[3:][0].split())

files = map(lambda x: gzip.open(dataset + "." + x +'-filtered.gz', 'w'), 'tok pos'.split())

for t_line, p_line in izip(gzip.open(tok_file), gzip.open(pos_file)):
    lines = [[], []]
    t_line = t_line.split()
    p_line = p_line.split()
    for token, pos in izip(t_line, p_line):
        if pos in valid_pos_set:
            lines[0].append(token)
            lines[1].append(pos)
    if len(lines[0]) != 0:
        for i in xrange(len(lines)):
            files[i].write("{}\n".format(" ".join(lines[i])))
