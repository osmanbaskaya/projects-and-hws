#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import os
#importc sys
from random import seed, shuffle


def fetch_fnames(path, folder):
    files = os.listdir(os.path.join(path, folder))
    return [(os.path.join(path, folder, f), folder[0]) for f in files]

def sample_data(data, seed_val=1, percentage=0.2):
    seed(seed_val)
    m = int(len(data) * percentage)
    shuffle(data)
    return data[:m], data[m:]

def create_data(files):
    """ files 2 X, y """
    X = []
    y = []
    for f, label in files:
        words = open(f).read().split()
        X.append(words)
        y.append(label)

    assert len(X) == len(y)

    return X, y

def create_X_data(files):
    """ files X """
    X = []
    for f in files:
        words = open(f).read().split()
        X.append(words)

    return X
    
    
def write_filenames(files, seed, typ):
    with open('{}.sample{}.txt'.format(typ, seed), 'w') as f:
        for fn in files:
            f.write("{}\t{}\n".format(fn[0], fn[1]))
