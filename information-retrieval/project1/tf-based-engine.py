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
RETRIEVE = 1000

database_info = {"0": {"avg": 493},
                 "1": {"avg": 493},
                 "2": {"avg": 288},
                 "3": {"avg": 288}}

AVG_QUERY_LENGTH = 16.64

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
    """ Answer 1: Implementation of Robertson's Score """
    return _tf_func(tf, 0.5, 1.5, doc_length, avg_length)

def get_idf(word):
    #return math.log(10, TOTAL_DOC / float(len(term_data[word])))
    L = len(term_data[word])
    if L == 0:
        idf = 0
    else:
        idf = math.log(TOTAL_DOC / float(L))
    return idf

def okapi_score(word, tf, doc_length, avg_length):
    #idf_sc = get_idf(word)
    return okapi_tf(tf, doc_length, avg_length)

def load_pkl(filename):
    return pickle.load(open(filename))

def vsm(word, tf, doc_length, avg_length):
    """
        Answer 2: Implementation of the Vector Space Model
    """
    tf = okapi_tf(tf, doc_length, avg_length)
    idf = get_idf(word)
    return  tf * idf # term product.

def score(query, score_func, N):
    """ Calculates the score for already processed query (or raw) """

    ranking = dd(int)
    for word in query:
        # Simulates a dot product
        #qtf = okapi_score(word, 1, len(set(query)), AVG_QUERY_LENGTH)
        qtf = okapi_score(word, 1, len(set(query)), AVG_QUERY_LENGTH)
        for t in term_data.get(word, []):
            docid, doclen, tf = t
            #print >> sys.stderr, docid, doclen, tf
            s = score_func(word, tf, doclen, database_info[database]['avg']) 
            ranking[docid] += (s * qtf)
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
queries = load_pkl(query_file)
database = term_file[-5] # database type
term_data = load_pkl(term_file)
doc_dict = get_doc_dict()
score_func = globals()[sys.argv[4]]
#score_func = okapi_tf

def get_system_score():
    for key in sorted(queries.keys(), key= lambda x: int(x)):
        query = queries[key]
        query = " ".join(query).lower().split()
        print >> sys.stderr, key, query
        ranking = score(query, score_func, RETRIEVE)
        if len(ranking) < RETRIEVE:
            m = "Less than {} documents retrieved for {}".format(RETRIEVE, key)
            print >> sys.stderr, m
        output_scores(key, ranking, database)

def test():
    query = queries['85']
    print query
    print score(query, score_func, 5)

def get_fetchset(queryies):
    fetchset = set()
    for key in sorted(queries.keys(), key= lambda x: int(x)):
        query = queries[key]
        for word in query:
            # Simulates a dot product
            for t in term_data.get(word, []):
                docid, doclen, tf = t
                fetchset.add(docid)
    return fetchset

#test()
get_system_score()
#query = queries['54']
#print score(query, score_func, RETRIEVE)[:10]

