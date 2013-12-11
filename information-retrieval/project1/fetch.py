#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"


"""
Database information:

0: AP vol1 NOSTOP NOSTEMM
1: AP vol1 NOSTOP STEMM
2: AP vol1 STOP NOSTEMM
3: AP vol1 STOP STEMM

"""

import sys
from urllib2 import urlopen
import pickle
import re

query_file = sys.argv[1]
stoplist_file = sys.argv[2]
stem_file = sys.argv[3]
database = int(sys.argv[4])
is_only_alpha_numeric = bool(sys.argv[5])
out_file_name = sys.argv[6]

BASE = "http://fiji4.ccs.neu.edu/~zerg/lemurcgi/lemur.cgi?d={}&g=p&v={}"

def get_stopset():
    return set([line.strip() for line in open(stoplist_file)])

def get_stem_dict():
    stem_dict = {}
    for line in open(stem_file).readlines()[1:]:
        line = line.replace(" | ", "").split()
        stemmed = line[0]
        for word in line[1:]:
            stem_dict[word] = stemmed

    return stem_dict

def fetch_details_from_lemur(word):
    url  = BASE.format(database, word)
    page = urlopen(url)
    page = page.read().split('\n')

    ctf, df = map(int, page[8].split())
    tt = [line.split() for line in page[9:9+df]]
    return [(docid, int(doclen), int(tf)) for docid, doclen, tf in tt]

def create_pkl_file(data, fn):
    
    pickle.dump(data, open(fn, 'w'))

def preprocess_query(line, stemdict, stopset):

    if is_only_alpha_numeric:
        # removes all non-alphanumeric characters except whitespace
        line = re.sub("[^a-zA-Z0-9\s]", "", line)

    line = line.split()
    query_id, line = line[0], line[1:]
    print >> sys.stderr, "Processing: {}".format(query_id)

    preprocessed_words = []
    for word in line:
        if stopset is not None:
            if word in stopset:
                continue
        if stemdict is not None:
            word = stemdict.get(word, word)
        preprocessed_words.append(word)

    return query_id, preprocessed_words

def process_queries(stemdict, stopset):
    queries = {}
    d = {}
    for line in open(query_file):
        query_id, words = preprocess_query(line, stemdict, stopset)
        queries[query_id] = words
        for word in words:
             if word not in d:
                 d[word] = fetch_details_from_lemur(word)

    return d, queries

def main():
    stopset = None
    stemdict =  None
    if database == 1:
        stemdict = get_stem_dict()
    elif database == 2:
        stopset = get_stopset()
    elif database == 3:
        stemdict = get_stem_dict()
        stopset = get_stopset()

    d, queries = process_queries(stemdict, stopset)
    create_pkl_file(d, out_file_name)
    create_pkl_file(queries, "queries-" + out_file_name)

main()
