#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys
from collections import Counter
import numpy as np

train_file = sys.argv[1]
pos_data = open(sys.argv[2]).readlines()
neg_data = open(sys.argv[3]).readlines()


def calc_priors(train_tags):
    train_tags = [tag.strip() for tag in train_tags]
    d = Counter(train_tags)
    total = sum(d.values())
    for key, val in d.iteritems():
        d[key] = val / float(total)
    return d

def calc_scores(pos_data, neg_data):
    priors = calc_priors(open(train_file).readlines())
    pos_data = np.array(pos_data, dtype='float32')
    neg_data = np.array(neg_data, dtype='float32')
    pos_data *= priors['p']
    neg_data *= priors['n']
    
    test_gold = open(sys.argv[4]).readlines()
    
    test_gold = [tag.strip() for tag in test_gold]

    correct = 0
    for i in xrange(len(pos_data)):
        if pos_data[i] >= neg_data[i]:
            if 'p' == test_gold[i].strip():
                correct += 1
        else:
            if 'n' == test_gold[i].strip():
                correct += 1
    return correct / float(len(pos_data))


print calc_scores(pos_data, neg_data)
