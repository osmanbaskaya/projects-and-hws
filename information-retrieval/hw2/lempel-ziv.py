#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys

initials = "oba"
for c in initials:
    print bin(ord(c)),

print

for line in sys.stdin:
    s = ""
    for c in line:
        if len(s) != 8:
            s += c
        else:
            ordi = int(s, 2)
            print chr(ordi),
            s = c


