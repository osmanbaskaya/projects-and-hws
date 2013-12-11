#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = "Osman Baskaya"

import sys
import pickle
from collections import defaultdict as dd
from itertools import count
import math

TOTAL_DOC = 84678

database_info = {"0": {"avg": 493},
                 "1": {"avg": 493},
                 "2": {"avg": 288},
                 "3": {"avg": 288}}

def get_doc_dict():
    L = open(doc_list).read().split()
    return dict(zip(*([iter(L)] * 2)))

def _tf_func(tf, k, c, doc_length=1, avg_length=1):
    """
        This function provides various TF calculation for 
            - Robertsons (k=1, c=0), 
            - Okapi (k = 0.5, c=1.5)
    """
    return tf / (tf + k + c * (doc_length / avg_length))

def robertsons_tf(tf, doc_length, avg_length):
    
    return _tf_func(tf, 1, 0)

def robertson_score(word, tf, doc_length, avg_length):
    return robertsons_tf(tf, doc_length, avg_length)

def okapi_tf(tf, doc_length, avg_length):
    return _tf_func(tf, 0.5, 1.5, doc_length, avg_length)

def get_idf(word):
    return math.log(10, TOTAL_DOC / len(term_data[word]))

def okapi_score(word, tf, doc_length, avg_length):
    return okapi_tf(tf, doc_length, avg_length) * get_idf(word)

def load_pkl(filename):
    return pickle.load(open(filename))

def score(query, score_func, N):
    """ Calculates the score for already processed query (or raw) """

    ranking = dd(int)
    for word in query:
        for t in term_data.get(word, []):
            docid, doclen, tf = t
            s = score_func(word, tf, doclen, database_info[database]['avg'])
            ranking[docid] += s
    try:
        rr = sorted(ranking, key=lambda x: ranking[x], reverse=True)[:N]
        return [(key, ranking[key]) for key in rr]
    except ValueError:
        print >> sys.stderr, "No documents retrieved for ranking query {}".format(query)
        return []

def output_scores(query_no, ranking, database):
    c = count(1)
    for doc_id, score in ranking:
        o = "{} Q0 {} {} {} Exp"
        #print o.format(query_no, doc_dict[doc_id], c.next(), score, database)
        print o.format(query_no, doc_dict[doc_id], c.next(), score)

#doc_list = "project-files/doclist.txt"
#query_file = "queries-tf-database-3.pkl"
#term_file = "tf-database-3.pkl"
term_file = sys.argv[1]
query_file = sys.argv[2]
doc_list = sys.argv[3]
database = term_file[-5] # database type
queries = load_pkl(query_file)
term_data = load_pkl(term_file)
doc_dict = get_doc_dict()
score_func = globals()[sys.argv[4]]
#score_func = okapi_tf

for key in sorted(queries.keys(), key= lambda x: int(x)):
    query = queries[key]
    ranking = score(query, score_func, 1000)
    output_scores(key, ranking, database)
