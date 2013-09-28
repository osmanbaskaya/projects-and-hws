#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import numpy as np
import pylab as pl
import sys

plots = []
ppls = []
ppls1 = []

for line in sys.stdin:
    ppl, ppl1 = line.split()
    ppls.append(float(ppl))
    ppls1.append(float(ppl1))


ppls = np.array(ppls)
ppls1 = np.array(ppls1)

plots.append(pl.errorbar(len(ppls), np.median(ppls), ppls.std())[0])

pl.title("Clustering measures for 2 random uniform labelings\n"
         "with equal number of clusters")
pl.xlabel('Number of clusters (Number of samples is fixed to %d)' % len(ppls))
pl.ylabel('Score value')
pl.legend(plots, "PPL")
#pl.ylim(ymin=-0.05, ymax=1.05)
