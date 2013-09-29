#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import numpy as np
import sys

ppls = []
ppls1 = []

for line in sys.stdin:
    ppl, ppl1 = line.split()
    ppls.append(float(ppl))
    ppls1.append(float(ppl1))

ppls = np.array(ppls)
ppls1 = np.array(ppls1)

print "ppl:", ppls.mean(), ppls.std()
print "ppl1:", ppls1.mean(), ppls1.std()
