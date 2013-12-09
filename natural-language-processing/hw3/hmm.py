#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
Hidden Markov Model is applied on Tagging Problem.

Second order markov model is used to model joint distribution
over word sequences and tag sequences p(x1, ..., xn | y1 ..., y(n+1))
(Note that y(n+1) is always STOP tag.)

"""

import sys
import os

def read_probability_estimations():
    pass

def read_counts():
    pass

def read_parameters():
    """Read the estimations from a file. This file should be ARPA
    formatted. """
    pass

def decode():
    """ Viterbi algorithm is used for decoding. """
    pass
