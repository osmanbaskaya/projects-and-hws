#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import MinMaxScaler
from itertools import izip
from hw2_utils import create_X_data
from subprocess import Popen, PIPE
import sys
import gzip


lm_file1 = sys.argv[1]
lm_file2 = sys.argv[2]
train_file = sys.argv[3]
test_file = sys.argv[4]
#vocab_file = sys.argv[4]

def get_ngram_counts(fn, order):
    command = ["ngram-count", "-order", str(order), "-text", fn]
    return Popen(command, stdout=PIPE).communicate()[0]

def get_vocab(lm_file, order=3):
    vocab = set()
    count = 0
    start = "\{}-grams:".format(order)
    not_started = True
    for line in gzip.open(lm_file):
        line = line.strip()
        if not_started:
            if line == start:
                not_started = False
        else:
            line = line.split()
            n = len(line)
            if n == 0: # ngrams are finished
                #print "Total {}-grams: {}".format(order, count)
                return vocab
            assert n == 4
            count += 1
            vocab.add(" ".join(line[1:]))

### Feature Calculation Functions ###

def get_keywords_features(reviews, labels, set_typ, rev_typ, keywords):
    X = create_X_data(reviews)
    features = []
    if set_typ == 'train':
        for review, label in izip(X, labels):
            count = 0
            if label == rev_typ:
                review = set(review)
                for k in keywords:
                    if k in review:
                        count += 1
            features.append({rev_typ + 'keywords_feature': count})
    elif set_typ == 'test':
        for review in X:
            count = 0
            review = set(review)
            for k in keywords:
                if k in review:
                    count += 1
            features.append({rev_typ + 'keywords_feature': count})

    return features
    

def get_review_length(reviews):
    X = create_X_data(reviews)
    features = []
    for review in X:
        features.append({'length': len(review)})

    return features

def get_trigrams(reviews):
    order = 3
    pos_v = get_vocab(lm_file1, 3)
    neg_v = get_vocab(lm_file2, 3)
    all_v = pos_v.union(neg_v)
    ngram_features = []
    for fn in reviews:
        ngrams = get_ngram_counts(fn, order).split('\n')
        inst_d = {}
        for line in ngrams:
            line = line.split()
            if len(line) == (order + 1):
                ngram, count = " ".join(line[:order]), int(line[-1])
                if ngram in all_v:
                    inst_d[ngram] = count
        ngram_features.append(inst_d)
    return ngram_features


def create_features(func_list):
    X = []
    for func, args in func_list:
        #print "Feature func: {} called".format(func)
        features = func(*args)
        if len(X) == 0:
            X = features
        else:
            for Xd, fd in izip(X, features):
                for fd_keys in fd:
                    Xd[fd_keys] = fd[fd_keys]
    return X

def skale(X):
    skaler = MinMaxScaler()
    return skaler.fit_transform(X.toarray())

def get_reviews_labels(review_files):
    reviews = []
    labels = []
    for line in open(review_files):
        fn, label = line.split()
        labels.append(label)
        reviews.append(fn)
    return reviews, labels


pos_kw = ['oscar', 'winner', 'excellent', 'perfect', 'best']
neg_kw = ['shit', 'hate', 'disaster', 'awful', 'mess', 'stinks']
train_reviews, y_train = get_reviews_labels(train_file)
feature_list = [
                (get_trigrams, (train_reviews,)), 
                (get_review_length, (train_reviews,)),
                (get_keywords_features, (train_reviews, y_train, 'train', 'p', pos_kw)),
                #(get_keywords_features, (train_reviews, y_train, 'train', 'n', neg_kw)),
              ]
#feature_list = [get_keywords_positive_features, get_review_length]
train_features = create_features(feature_list)
vectorizer = DictVectorizer()
X_train = vectorizer.fit_transform(train_features)
#print "training features are created"
#print "X_train shape", X_train.shape
X_train = skale(X_train)
#print "Training - Scaling done"

clf = LogisticRegression(C=1) # creation
clf.fit(X_train, y_train)  # training 
#print "Fitting done"

test_reviews, y_test = get_reviews_labels(test_file)
feature_list = [
                (get_trigrams, (test_reviews,)), 
                (get_review_length, (test_reviews,)),
                (get_keywords_features, (test_reviews, y_test, 'test', 'p', pos_kw)),
                #(get_keywords_features, (test_reviews, y_test, 'test', 'n', neg_kw)),
              ]
test_features = create_features(feature_list)
X_test = vectorizer.transform(test_features)
#print "test features are created"
X_test = skale(X_test)
#print "Test - Skaling Done"

score = clf.score(X_test, y_test)
print score, ","

#X_test, y_test = create_features() 
#score = clf.score() # get the score

#print score
