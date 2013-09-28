#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import numpy as np
import sys
import os
import gzip
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input_file", dest="input_file", default=None,
                  help="Input file for bootstrapping", metavar="Input File")
parser.add_option("-s", "--seed", dest="seed", default=1,
        help="SEED Value", metavar="SEED")

mandatories = ['input_file']

def input_check(opts, mandatories):
    """ Making sure all mandatory options appeared. """ 
    run = True
    for m in mandatories:
        if not opts.__dict__[m]: 
            print >> sys.stderr, "mandatory option is missing: %s" % m
            run = False
    if not run:
        print >> sys.stderr
        parser.print_help()
        exit(-1)

(opts, args) = parser.parse_args() 
input_check(opts, mandatories)

input_file = opts.input_file
s = int(opts.seed)

if input_file.endswith('gz'): 
    func = gzip.open
else:
    func = open

#np.random.seed(s)

lines = func(input_file).readlines()
lines = np.random.choice(lines, len(lines))
for line in lines:
    print line,
