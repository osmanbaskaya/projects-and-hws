#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
Hidden Markov Model is applied on the tagging problem.

Second order markov model is used to model joint distribution
over word sequences and tag sequences p(x1, ..., xn | y1 ..., y(n+1))
(Note that y(n+1) is always STOP tag.)

"""

import sys
from collections import defaultdict as dd
import gzip
from itertools import product
#from pprint import pprint
#from decimal import Decimal
#import os

q_file = gzip.open(sys.argv[1]) # trigram tag file / trigrams probability file
e_file = gzip.open(sys.argv[2]) # word-tag file    / word-tags probability file
sentences = gzip.open(sys.argv[3]) # sentences to be tagged
valid_tags = tuple(sys.argv[4:][0].split())
START_SENT_TAG = ('<s>', '<s>')
STOP_SENT_TAG = "</s>"
NGRAM = 3


def is_valid_prob_dist(d, words, tags, eps=0.001):
    total_error = 0
    for word in words:
        t = sum([d[(word, tag)] for tag in tags])
        total_error += abs(t - 1)

    return True if total_error <= eps else False

def laplace(count_dict, ss, eps=1000):
    """ Laplace smoothing on the count_dict """
    for trigram in product(ss, repeat=NGRAM):
        count_dict[trigram] += eps
        count_dict[trigram[0:2]] += eps
    return count_dict

def prepare_q_from_counts(smoothing_method=None):
    tmp = dd(int)
    for line in q_file:
        tagseq, count = line.rsplit(None, 1)
        count = int(count)
        tagseq = tuple(tagseq.split())
        tmp[tagseq] = count

    q = dd(int)
    unigrams = sum([tmp[u] for u in tmp.keys() if len(u) == 1])
    # TODO: unigram test should be done
    #print unigrams
    if smoothing_method is not None:
        all_tags = list(valid_tags)
        all_tags.extend(["<s>", "</s>"])
        tmp = smoothing_method(tmp, all_tags) 
    for tagseq, count in tmp.viewitems():
        if len(tagseq) == 3:
            q[tagseq] = tmp[tagseq] / float(tmp[tagseq[0:2]])
        elif len(tagseq) == 2:
            q[tagseq] = tmp[tagseq] / float(tmp[tagseq[0:1]])
        elif len(tagseq) == 1:
            q[tagseq] = tmp[tagseq] / float(unigrams)
        else:
            m =  "Houston, I have a bad feeling about this mission."
            print >> sys.stderr, m
            exit(-1)

    
    return q


def jelinek_mercer(e, words, w, tags=valid_tags):
    # w is the lambda parameter for jelinek mercer smoothing
    num_tokens = float(sum(words.values()))
    #print >> sys.stderr, words.keys()[0:5]
    #print >> sys.stderr, words.values()[0:5]
    #print >> sys.stderr, num_tokens, w
    for word in words:
        for tag in tags:
            key = (word, tag)
            e[key] = w * e[key] + (1 - w) * (words[word] / num_tokens) # unigram MLE

    return e

def prepare_e_from_counts(smoothing_method = None):
    all_tags = list(valid_tags)
    all_tags.extend(["<s>", "</s>"])
    wpc = dd(lambda: dd(int)) # wpc[word][pos] = count 
    tags = dd(int)
    words = dd(int)
    for line in e_file:
        line = line.split()
        word, pos, count = line[0], line[1], int(line[2])
        wpc[word][pos] += count
        words[word] += count
        tags[pos] += count

    e = dd(lambda: 0)
    for word, psos in wpc.viewitems(): # word, parts of speech
        for p, c in psos.viewitems():
            e[(word, p)] = c / float(tags[p])
    
    if smoothing_method is not None:
        e = smoothing_method(e, words, 0.99, all_tags)

    #assert is_valid_prob_dist(e, words, all_tags), "Not a valid probability distribution!"
    return e

def e(word, tag):
    """ It calculates the probability p(word|tag) """
    return e_dict[(word, tag)]

def q(v, w, u):
    """ It calculates the probability p(v|w, u) """
    score = q_dict[(w, u, v)]
    if score == 0:
        print >> sys.stderr, w, u, v, score
    return score

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

e_dict = prepare_e_from_counts(jelinek_mercer)
q_dict = prepare_q_from_counts(laplace)

for sentence in sentences:
    print " ".join(decode(sentence))

