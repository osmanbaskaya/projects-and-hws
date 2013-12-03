#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = "Osman Baskaya"

import sys

stopword_file = sys.argv[1]
query_file = sys.argv[2]


def _tf_func(tf, k, c, doc_length=1, avg_length=1):
    """
        This function provides various TF calculation for 
            - Robertsons (k=1, c=0), 
            - Okapi (k = 0.5, c=1.5)
    """

    return tf / (tf + k + c * (doc_length / avg_length))

def robertsons_tf(tf):
    
    return _tf_func(tf, 1, 0)

def okapi_tf(tf, doc_length, avg_length):
    
    return _tf_func(tf, 0.5, 1.5, doc_length, avg_length)
