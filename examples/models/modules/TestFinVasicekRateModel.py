# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:10:12 2019

@author: Dominic
"""

import numpy as np
import time
from financepy.models.FinModelRatesVasicek import zeroPrice, zeroPrice_MC


def test_FinModelRatesVasicek():

    r0 = 0.05
    a = 0.10
    b = 0.05
    sigma = 0.05
    t = 5.0

    p = zeroPrice(r0, a, b, sigma, t)

    numPaths = 1000
    dt = 0.02
    seed = 1968

    print("TIME", "T", "P", "P_MC", "P_MC2")

    for t in np.linspace(0, 10, 21):
        start = time.time()
        p_MC = zeroPrice_MC(r0, a, b, sigma, t, dt, numPaths, seed)
        p_MC2 = zeroPrice_MC(r0, a, b, sigma, t, dt, 10 * numPaths, seed)
        p = zeroPrice(r0, a, b, sigma, t)
        end = time.time()
        elapsed = end - start
        print(elapsed, t, p, p_MC, p_MC2)


test_FinModelRatesVasicek()
