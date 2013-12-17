#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""

import sys
import pickle
from collections import defaultdict as dd
from itertools import count
import math

TOTAL_DOC = 84678

database_info = {"0": {"avg": 493, "num_terms": 41802513, "num_uniq": 207615},
                 "1": {"avg": 493, "num_terms": 41802513, "num_uniq": 166242},
                 "2": {"avg": 288, "num_terms": 24401877, "num_uniq": 207224},
                 "3": {"avg": 288, "num_terms": 24401877, "num_uniq": 166054}}

DOC_WEIGHT = 0.8 # from the project file.
RETRIEVE = 1000


def get_doc_dict():
    L = open(doc_list).read().split()
    return dict(zip(*([iter(L)] * 2)))

def load_pkl(filename):
    return pickle.load(open(filename))

def get_idf(word):
    #return math.log(10, TOTAL_DOC / float(len(term_data[word])))
    L = len(term_data[word])
    if L == 0:
        idf = 0
    else:
        idf = math.log(TOTAL_DOC / float(L), 10)
    return idf

def bm25_score(word, tf, qtf, doclen, avgdl, k1=1.2, k3=100, b=0.75):
    
    L = len(term_data[word])
    part1 = (k1 + 1) * tf / (k1 * (1 - b + b * doclen / float(avgdl)) + tf)
    part2 = (k3 + 1) * qtf / (k3 + qtf)
    part3 = math.log( (TOTAL_DOC - L) / float(L), 10)

    return  part1 * part2 * part3

def create_doc_dict(query):

    docs_tf  = dd(lambda: dd(int))
    docs_doclen = dict()
    for word in query:
        for t in term_data.get(word, []):
            docid, doclen, tf = t
            docs_tf[docid][word] = tf
            if docid not in docs_doclen:
                docs_doclen[docid] = doclen

    return docs_tf, docs_doclen

def score(query, score_func, N):
    """ Calculates the score for already processed query (or raw) """

    docs_tf, docs_doclen = create_doc_dict(query)
    print >> sys.stderr, query
    ranking = dd(lambda: 0)
    for word in query:
        if ctf_dict[word] != 0: # corpus has it? (i.e. No for "Document")
            for docid in docs_tf.viewkeys():
                #if docid != "79315":
                    #continue
                # Simulates a dot product
                qtf = 1
                tf = docs_tf[docid][word]
                doclen = docs_doclen[docid]
                s = score_func(word, tf, qtf, doclen, database_info[database]['avg'])
                ranking[docid] += s
                #ranking[docid] += math.log(s, 10)
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

term_file = sys.argv[1]
query_file = sys.argv[2]
doc_list = sys.argv[3]
ctf_file = sys.argv[4]

queries = load_pkl(query_file)
ctf_dict = load_pkl(ctf_file)
term_data = load_pkl(term_file)
doc_dict = get_doc_dict()
score_func = globals()[sys.argv[5]]
database = term_file[-5] # database type
print >> sys.stderr, "Data Loading Done."

#score_func = okapi_tf

#print >> sys.stderr, score_func.func_name
def get_system_score():
    print >> sys.stderr, "Score funct: {}".format(score_func.func_name)
    for key in sorted(queries.keys(), key=lambda x: int(x)):
        query = queries[key]
        query = " ".join(query).lower().split()
        #print >> sys.stderr, key, query
        ranking = score(query, score_func, RETRIEVE)
        output_scores(key, ranking, database)

def test():
    key = "54"
    query = queries[key]
    query = "cite sign preliminary".split()
    #print >> sys.stderr, query
    ranking = score(query, score_func, 5)
    print >> sys.stderr, ranking
    output_scores(key, ranking, database)

get_system_score()
#test()
