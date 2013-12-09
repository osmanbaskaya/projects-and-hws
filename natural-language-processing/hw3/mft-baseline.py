#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
"""
import sys
import gzip

most_freq_tag = "NNP"

word_tags_file = sys.argv[1] # (word most_freq_tag count) 3-tuple
test_lines = gzip.open(sys.argv[2])

def get_word_tags(fn=word_tags_file):
    L = gzip.open(word_tags_file).read().split()
    return dict(zip(*([iter(L)] * 2)))

word_tags = get_word_tags()

for line in test_lines:
    line = line.split()
    predictions = []
    for word in line:
        # get word's most frequent tag if possible. If not get most_freq_tag
        if word in word_tags:
            t = word_tags[word]
        else:
            t = most_freq_tag
        predictions.append(t)
        #predictions.append(word_tags.setdefault(word, most_freq_tag))
    print " ".join(predictions)
