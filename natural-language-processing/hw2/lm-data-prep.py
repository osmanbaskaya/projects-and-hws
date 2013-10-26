#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys

if len(sys.argv) != 4:
    msg = "Usage: {} data_type sample_no label"
    print >> sys.stderr, msg.format(sys.argv[0])
    exit(1)

data_type = sys.argv[1] # test/train
sample_no = sys.argv[2] # 1 2 3 4 5
label = sys.argv[3] # p/n/np

fn = "{}.sample{}.txt".format(data_type, sample_no)

#def get_doc_content(doc):
    #doc_lines = ""
    #for line in open(doc):
        #line = line.strip()
        #if line != "":
            #doc_lines += line
    #return doc_lines.replace('\n', ' ')

for line in open(fn):
    doc, rev_type = line.split()
    if rev_type == label:
        print doc

