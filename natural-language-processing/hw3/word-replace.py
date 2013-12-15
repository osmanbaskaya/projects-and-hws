#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""

import sys
import gzip

vocab = set(gzip.open(sys.argv[1]).read().split())

for line in sys.stdin:
    line = line.split()
    newline = []
    for word in line:
        if word in vocab:
            newline.append(word)
        else:
            newline.append('<unk>')
    print " ".join(newline)
