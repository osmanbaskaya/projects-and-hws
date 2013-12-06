#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys
import gzip

vocab_file1 = set(gzip.open(sys.argv[1]).read().split())
vocab_file2 = set(gzip.open(sys.argv[2]).read().split())

print "{} tokens different".format(len(vocab_file1.difference(vocab_file2)))
