#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys
import gzip

vocab_file1 = set(gzip.open(sys.argv[1]).read().split())
vocab_file2 = set(gzip.open(sys.argv[2]).read().split())
test_file = gzip.open(sys.argv[3])

print "{} word types different".format(len(vocab_file1.difference(vocab_file2)))

diff = vocab_file1.difference(vocab_file2)
total = 0
for line in test_file:
    line = line.split()
    for word in line:
        if word in diff:
            total += 1

print "{} tokens different".format(total)


    

