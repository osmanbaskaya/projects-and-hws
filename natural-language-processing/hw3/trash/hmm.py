#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
Hidden Markov Model is applied on Tagging Problem.

Second order markov model is used to model joint distribution
over word sequences and tag sequences p(x1, ..., xn | y1 ..., y(n+1))
(Note that y(n+1) is always STOP tag.)

"""

import sys
from collections import defaultdict as dd
import random
import gzip
#from pprint import pprint
#from decimal import Decimal
#import os

q_file = gzip.open(sys.argv[1]) # trigram tag file / trigrams probability file
e_file = gzip.open(sys.argv[2]) # word-tag file    / word-tags probability file
sentences = gzip.open(sys.argv[3]) # sentences to be tagged
valid_tags = tuple(sys.argv[4:][0].split())
START_SENT_TAG = ('<s>', '<s>')
STOP_SENT_TAG = "</s>"


def prepare_q_from_counts():
    tmp = dict()
    for line in q_file:
        tagseq, count = line.rsplit(None, 1)
        count = int(count)
        tagseq = tuple(tagseq.split())
        tmp[tagseq] = count

    q = dd(lambda: 0.00001)
    for tagseq, count in tmp.viewitems():
        # FIXME processing only trigrams
        if len(tagseq) == 3:
            q[tagseq] = tmp[tagseq] / float(tmp[tagseq[0:2]])
    return q

def prepare_e_from_counts():
    wpc = dd(lambda: dd(int)) # wpc[word][pos] = count 
    for line in e_file:
        line = line.split()
        word, pos, count = line[0], line[1], int(line[2])
        wpc[word][pos] += count
    
    e = dd(lambda: 0.00001)
    for word, psos in wpc.viewitems(): # word, parts of speech
        wc = float(sum(psos.viewvalues()))
        for p, c in psos.viewitems():
            e[(word, p)] = c / wc
    return e

#def laplace_smoothing():


#def prepare_q_from_probabilites():
    #"""Read the estimations from a file. This file should be ARPA
    #formatted. """
    #pass

#def prepare_e_from_probabilites():
    #"""Read the estimations from a file. This file should be ARPA
    #formatted. """
    #pass

def e(word, tag):
    """ It calculates the probability p(word|tag) """
    return e_dict[(word, tag)]

def q(v, w, u):
    """ It calculates the probability p(v|w, u) """
    return q_dict[(w, u, v)]

def init_tag_sets(k):
    if k == 0:
        U = ('<s>',)
        W = ('<s>', )
    elif k == 1:
        U = valid_tags
        W = ('<s>', )
    else:
        U = valid_tags
        W= valid_tags
    V = valid_tags
    return W, U, V

def decode(sentence):
    """ Viterbi algorithm is used for decoding. """
    sentence = sentence.split()
    pi = dd(dict)
    bp = dd(dict)
    pi[-1][START_SENT_TAG] = 1.0
    for k, word in enumerate(sentence):
        W, U, V = init_tag_sets(k)
        for v in V:
            for u in U:
                pi[k][(u, v)], bp[k][(u, v)]= max([(pi[k-1][(w, u)] * q(v, w, u) \
                            * e(word, v), w) for w in W])
    
    n = len(sentence) - 1
    W, U, V = init_tag_sets(n)
    s, tags = max([(pi[n][(u, v)] * q(STOP_SENT_TAG, u, v), (u, v)) \
                                                for u in U for v in V])
    u, v = tags
    y = [v, u]
    for i in xrange(n, 1, -1):
        w = bp[i][(u, v)]
        y.append(w)
        v, u = u, w
    return y[::-1] # reverse order

e_dict = prepare_e_from_counts()
q_dict = prepare_q_from_counts()
for sentence in sentences:
    print " ".join(decode(sentence))
