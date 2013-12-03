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
database = int(sys.argv[3])
is_only_alpha_numeric = bool(sys.argv[4])

BASE = "http://fiji4.ccs.neu.edu/~zerg/lemurcgi/lemur.cgi?d={}&g=p&v={}"

def preprocess_query(line):

    #TODO ayni kelimeleri tekrar fetch etme!
    
    if is_only_alpha_numeric:
        # removes all non-alphanumeric characters except whitespace
        line = re.sub("[^a-zA-Z0-9\w]", "", line)

    line = line.split()
    query_id, line = line[0], line[1:]

    if database == 1:
        pass
    elif database == 2:
        pass
    else:
        pass
    return 

def fetch_details_from_lemur(word):
    page = urlopen(BASE.format(database, word))

def create_pkl_file(data):
    pass

def process_queries():
    for line in open(query_file):
         query_id, words = preprocess_query(line)


process_queries()

