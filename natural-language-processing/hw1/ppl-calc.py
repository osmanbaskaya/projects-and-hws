#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import re
import sys
import gzip
import numpy as np

fn = sys.argv[1]
ppl_file = gzip.open(fn).read()


regex = re.compile(r'\[ (-\d+\.\d+) \]\n')
logprobs =  np.array(regex.findall(ppl_file), dtype='float64')
total_lp = logprobs.sum()
ppl =  np.power(10, -total_lp / logprobs.shape[0])

regex_sent = re.compile(r'1 sentences, ')
total_sent = len(regex_sent.findall(ppl_file))
x = -total_lp / (logprobs.shape[0] - total_sent)
ppl1 = np.power(10, x)
print "logprobs= {}, ppl= {}, ppl1= {}".format(total_lp, ppl, ppl1)



