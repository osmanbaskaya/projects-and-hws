#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys
import math

text_file = sys.argv[1]
proportion = float(sys.argv[2])
beta = float(sys.argv[3])

def calc_parameters(data):
    return len(data), len(set(data))

def calc_proportion(num_token, beta, proportion):
    print num_token, beta, proportion
    return math.pow(proportion * num_token**beta, 1/beta)

def main():
    text = open(text_file).read().split()
    num_token = len(text)
    #voc_size = len(set(text))
    print calc_proportion(num_token, beta, proportion)

if __name__ == '__main__':
    main()

