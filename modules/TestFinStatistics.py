# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 14:31:53 2019

@author: Dominic O'Kane
"""

import numpy as np
import time

from financepy.finutils.FinStatistics import mean, stdev, correlation
from math import sqrt


def test_FinStatistics():
    seed = 1972
    np.random.seed(seed)

    numTrials = 1000000
    x = np.random.normal(0.0, 1.0, size=(numTrials))
    y = np.random.normal(0.0, 1.0, size=(numTrials))

    ##########################################################################
    # DO NUMPY TIMINGS
    ##########################################################################

    start = time.time()

    print("l", "Mean", "SD")

    for l in range(0, 10):
        meanx1 = x.mean()
        sd1 = x.std()
        print(l, meanx1, sd1)

    end = time.time()
    elapsed = end - start

    start = time.time()

    print("Corr", "Measured")

    for beta in np.linspace(0.0, 1.0, num=11):
        z = x * beta + y * sqrt(1.0 - beta * beta)
        c = np.corrcoef(x, z)[0, 1]
        print(beta, c)

    end = time.time()
    elapsed = end - start
    print("TIME")
    print(elapsed)

    ##########################################################################
    # DO STATS TIMINGS

    print("l", "Mean", "SD")

    start = time.time()

    for l in range(0, 10):
        mean2 = mean(x)
        sd2 = stdev(x)
        print(l, mean2, sd2)

    end = time.time()
    elapsed = end - start
    print("TIME")
    print(elapsed)

    start = time.time()

    print("Corr", "Measured")

    for beta in np.linspace(0.0, 1.0, num=11):
        z = x * beta + y * sqrt(1.0 - beta * beta)
        c = correlation(x, z)
        print(beta, c)

    end = time.time()
    elapsed = end - start
    print("TIME")
    print(elapsed)

    ##########################################################################


test_FinStatistics()
