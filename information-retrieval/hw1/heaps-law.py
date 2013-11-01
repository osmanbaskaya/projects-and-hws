#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys
import math
from math import e
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) == 5:
    question_part = sys.argv[1]
    text_file = sys.argv[2]
    proportion = float(sys.argv[3])
    beta = float(sys.argv[4])
elif len(sys.argv) == 3:
    question_part = sys.argv[1]
    text_file = sys.argv[2]
else:
    print "Usage: {} a/b parsed_input_file proportion beta".format(sys.argv[0])
    exit(1)

def calc_parameters(data):
    return len(data), len(set(data))

def calc_proportion(num_token, beta, proportion):
    return math.pow(proportion * num_token**beta, 1/beta)

def main():
    text = open(text_file).read().split()
    num_token = len(text)
    if question_part == 'a':
        #voc_size = len(set(text))
        result = calc_proportion(num_token, beta, proportion)
        print result / float(num_token), result
    elif question_part == 'b':
        sample_size = 100
        x = []
        y = []
        for i in range(sample_size, num_token+sample_size, 100):
            xi, yi = calc_parameters(text[0:i])
            x.append(xi)
            y.append(yi)
        x = np.array(x)
        y = np.array(y)
        x = np.log(x)
        y = np.log(y)
        n = len(x)
        x_mean = x.mean()
        y_mean = y.mean()
        b = (y_mean * np.dot(x,x) - (x_mean * np.dot(x, y))) \
                                / (np.dot(x, x) - (n * x_mean**2))
        m = (np.dot(x, y) - (n * x_mean * y_mean)) / (np.dot(x, x) - (n * x_mean**2))
        lin_x = np.linspace(4, 11, 100)
        lin_y = (m * lin_x) + b
        plt.plot(lin_x, lin_y, '-')
        plt.xlabel("number of words")
        plt.ylabel("number of unique words")
        plt.title("Heaps' Law")
        plt.plot(x, y, "o")
        plt.legend(["line with the least squared error", "actual data points"], loc=2)
        print "beta: {}, k: {}".format(m, e**b)
        plt.show()
    else:
        print "Usage: {} a/b parsed_input_file proportion beta".format(sys.argv[0])
        exit(1)

if __name__ == '__main__':
    main()

