#!/usr/bin/env python

import gzip
import sys

dataset = sys.argv[1]

files = map(lambda x: gzip.open(dataset + "." + x +'.gz', 'w'), 'tok pos'.split())
lines = [[], []]

n = len(lines)

sentence = False
for line in sys.stdin:
    if line.startswith('<s>'):
        sentence = True
    elif line.startswith('</s>'):
        sentence = False
        for i in xrange(n):
            files[i].write(' '.join(lines[i]) + "\n")
            lines[i] = []
    elif sentence:
        cols = line.strip().split("\t")
        for i in xrange(n):
            lines[i].append(cols[i])

# If input file does not finish with the "</s>", then comment out needed
#for i in xrange(len(files)):
    #files[i].write("{}\n".format(' '.join(lines[i])))

map(lambda f: f.close(), files)
