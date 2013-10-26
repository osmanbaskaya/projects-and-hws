#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

from sklearn.linear_model import LogisticRegression
import numpy as np



### Feature Calculation Functions ###

def get_length():
    pass


def create_features(func_list, reviews):
    
    m = len(reviews)   # number of instances (reviews)
    n = len(func_list) # number of feature
    X = np.zeros([m,n])
    for func in func_list:
        feature_column = func()

    #TODO Concatenation
    return X


X_train, y_train = create_features() # format all training instance features

clf = LogisticRegression() # creation
clf.fit(X_train, y_train)  # training 

X_test, y_test = create_features() 
score = clf.score() # get the score

print score
