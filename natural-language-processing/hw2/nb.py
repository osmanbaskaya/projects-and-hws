#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import sys
from hw2_utils import fetch_fnames, sample_data, create_data, write_filenames
from collections import defaultdict as dd
from math import log
from itertools import izip


__author__ = "Osman Baskaya"


if len(sys.argv) != 2:
    print >> sys.stderr, "Usage: {} seed".format(sys.argv[0])


UNK = "<unk>" # unknown word label

class NaiveBayesClassifier(object):
    
    def __init__(self, alpha=1, stoplist=set()):
        # alpha -> smoothing value, default 1
        
        self.name = "Naive Bayes Classifier"
        self.alpha = alpha
        self.word_param = dd(lambda: dd(lambda: alpha))
        self.class_param = dd(int)
        self.stoplist = stoplist
        self.unseen = {}

    def fit(self, X, y):
        # X -> training data, y -> labels (gold tags)
        print >> sys.stderr, "Training started"
        for x, cls in izip(X, y):
            self.class_param[cls] += 1
            for w in x:
                if w not in self.stoplist:
                    self.word_param[cls][w] += 1

            self.word_param[cls][UNK] = 1
        
        self._transform_to_prob()
        self._transform_to_logprob()

        print >> sys.stderr, "Training finished"

    def _transform_to_prob(self):
        
        for c in self.word_param:
            denominator = sum(self.word_param[c].values())
            # Unseen word prob assignment
            for word, count in self.word_param[c].iteritems():
                try: 
                    self.word_param[c][word] = count / denominator
                except ValueError:
                    print >> sys.stderr, count, self.class_param[c]


        denominator = sum(self.class_param.values())
        for c in self.class_param:
            self.class_param[c] = self.class_param[c] / denominator

    def _transform_to_logprob(self):

        for c in self.word_param:
            self.class_param[c] = log(self.class_param[c])
            for word, prob in self.word_param[c].iteritems():
                self.word_param[c][word] = log(prob)


    def predict(self, x):
        result = dd(int)
        for c in (self.class_param):
            result[c] += self.class_param[c] # class prior
            for w in x:
                if w not in self.stoplist:
                    if w in self.word_param[c]: 
                        result[c] += self.word_param[c][w]
                    else:
                        result[c] += self.word_param[c][UNK] # w is OOV word
        max_cls, max_val = max(result.iteritems(), key=lambda x: x[1])
        return max_cls, max_val

    def score(self, X, y):
        # X -> test data, y -> labels (gold tags)
        correct = 0
        for x, gold_label in izip(X, y):
            cls, val = self.predict(x)
            if cls == gold_label:
                correct += 1
        return float(correct) / len(y)

def main():
    seed = sys.argv[1] 
    data_path = "reviews/"

    split_percentage = 0.20
    test_files, train_files = sample_data(fetch_fnames(data_path, 'pos') +
                                          fetch_fnames(data_path, 'neg'), 
                                          seed, split_percentage)

    write_filenames(test_files, seed, "test")
    write_filenames(train_files, seed, "train")
    
    X_train, y_train = create_data(train_files)
    X_test, y_test = create_data(test_files)


    clf = NaiveBayesClassifier()
    clf.fit(X_train, y_train)
    print clf.score(X_test, y_test)

if __name__ == '__main__':
    main()


