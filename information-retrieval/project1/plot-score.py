#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""

import sys
from matplotlib import pyplot as plt
#from pprint import pprint
from itertools import cycle

files = map(open, sys.argv[1:])


def get_precisions(lines):
    MAP = float(lines[19].strip()) # Mean Average Precision
    ll = [line.split() for line in lines[7:18]]
    ll = [(float(line[1]), float(line[2])) for line in ll]
    return MAP, ll

scores = {}
for f in files:
    exp = f.name.split('.')[0]
    lines = f.readlines()
    MAP, ll = get_precisions(lines)
    scores[exp] = (MAP, ll)

color = cycle("bgrcmykw")

for exp, val in scores.viewitems():
    x = [v[0] for v in val]
    y = [v[1] for v in val]
    plt.plot(x, y, '%s-' % color.next(), label=exp)

plt.legend()
plt.show()

