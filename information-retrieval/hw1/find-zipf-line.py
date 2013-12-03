#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

from itertools import count
from math import log
import matplotlib.pyplot as plt
import numpy as np


c = count(3)

y = [log(float(line)) for line in open('songfreqencies.txt')]
x = [log(i) for i in range(1, len(y)+1)]

y = np.array(y)
x = np.array(x)

x_mean = x.mean()
y_mean = y.mean()

n = len(x)
b = (y_mean * np.dot(x,x) - (x_mean * np.dot(x, y))) / (np.dot(x, x) - (n * x_mean**2))
m = (np.dot(x, y) - (n * x_mean * y_mean)) / (np.dot(x, x) - (n * x_mean**2))
print m, b

lin_x = np.linspace(0, 10, 100)
lin_y = (m * lin_x) + b
plt.plot(lin_x, lin_y, '-')
plt.plot(x, y, "o")
plt.show()




