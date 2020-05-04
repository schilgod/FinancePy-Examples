# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:51:05 2016

@author: Dominic O'Kane
"""

from financepy.models.FinProcessSimulator import FinVasicekNumericalScheme
from financepy.models.FinProcessSimulator import FinCIRNumericalScheme
from financepy.models.FinProcessSimulator import FinHestonNumericalScheme
from financepy.models.FinProcessSimulator import FinGBMNumericalScheme
from financepy.models.FinProcessSimulator import FinProcessTypes
from financepy.models.FinProcessSimulator import FinProcessSimulator

##########################################################################


def test_FinProcessSimulator():

    import time

    numPaths = 20000
    numAnnSteps = 100
    seed = 1919
    t = 1.0
    modelSim = FinProcessSimulator()
    printPaths = False

    print(
        "######################## GBM NORMAL ###############################")
    sigma = 0.10
    stockPrice = 100.0
    drift = 0.04
    scheme = FinGBMNumericalScheme.NORMAL
    modelParams = (stockPrice, drift, sigma, scheme)
    start = time.time()
    paths = modelSim.getProcess(
        FinProcessTypes.GBM,
        t,
        modelParams,
        numAnnSteps,
        numPaths,
        seed)
    end = time.time()
    elapsed = end - start
    print("PROCESS", "TIME")
    print("GBM NORMAL", elapsed)
    if printPaths:
        print(paths)

    print(
        "######################## GBM ANTITHETIC ###########################")
    sigma = 0.10
    stockPrice = 100.0
    drift = 0.04
    scheme = FinGBMNumericalScheme.ANTITHETIC
    modelParams = (stockPrice, drift, sigma, scheme)
    start = time.time()
    paths = modelSim.getProcess(
        FinProcessTypes.GBM,
        t,
        modelParams,
        numAnnSteps,
        numPaths,
        seed)
    end = time.time()
    elapsed = end - start
    print("GBM ANTITHETIC", elapsed)
    if printPaths:
        print(paths)

    print(
        "###################### HESTON EULER ###############################")
    stockPrice = 100.0
    v0 = 0.05
    kappa = 0.50
    theta = 0.05
    sigma = 0.90
    rho = -0.9
    scheme = FinHestonNumericalScheme.EULER
    modelParams = (stockPrice, drift, v0, kappa, theta, sigma, rho, scheme)
    start = time.time()
    paths = modelSim.getProcess(
        FinProcessTypes.HESTON,
        t,
        modelParams,
        numAnnSteps,
        numPaths,
        seed)
    end = time.time()
    elapsed = end - start
    print("HESTON EULER", elapsed)
    if printPaths:
        print(paths)

    print(
        "###################### HESTON EULERLOG ############################")
    stockPrice = 100.0
    v0 = 0.05
    kappa = 0.50
    theta = 0.05
    sigma = 0.90
    rho = -0.9
    scheme = FinHestonNumericalScheme.EULERLOG
    modelParams = (stockPrice, drift, v0, kappa, theta, sigma, rho, scheme)
    start = time.time()
    paths = modelSim.getProcess(
        FinProcessTypes.HESTON,
        t,
        modelParams,
        numAnnSteps,
        numPaths,
        seed)
    end = time.time()
    elapsed = end - start
    print("HESTON EULERLOG", elapsed)
    if printPaths:
        print(paths)

    print(
        "###################### HESTON QUADEXP #############################")
    stockPrice = 100.0
    v0 = 0.05
    kappa = 0.50
    theta = 0.05
    sigma = 0.90
    rho = -0.9
    scheme = FinHestonNumericalScheme.QUADEXP
    modelParams = (stockPrice, drift, v0, kappa, theta, sigma, rho, scheme)
    start = time.time()
    paths = modelSim.getProcess(
        FinProcessTypes.HESTON,
        t,
        modelParams,
        numAnnSteps,
        numPaths,
        seed)
    end = time.time()
    elapsed = end - start
    print("HESTON QUADEXP", elapsed)
    if printPaths:
        print(paths)

    print(
        "######################## VASICEK NORMAL ###########################")
    r0 = 0.05
    kappa = 0.50
    theta = 0.05
    sigma = 0.90
    scheme = FinVasicekNumericalScheme.NORMAL
    modelParams = (r0, kappa, theta, sigma, scheme)
    start = time.time()
    paths = modelSim.getProcess(
        FinProcessTypes.VASICEK,
        t,
        modelParams,
        numAnnSteps,
        numPaths,
        seed)
    end = time.time()
    elapsed = end - start
    print("VASICEK_NORMAL", elapsed)
    if printPaths:
        print(paths)

    print(
        "####################### VASICEK ANTITHETIC ########################")
    r0 = 0.05
    kappa = 0.50
    theta = 0.05
    sigma = 0.90
    scheme = FinVasicekNumericalScheme.ANTITHETIC
    modelParams = (r0, kappa, theta, sigma, scheme)
    start = time.time()
    paths = modelSim.getProcess(
        FinProcessTypes.VASICEK,
        t,
        modelParams,
        numAnnSteps,
        numPaths,
        seed)
    end = time.time()
    elapsed = end - start
    print("VASICEK_NORMAL ANTI", elapsed)
    if printPaths:
        print(paths)

    print(
        "############################# CIR #################################")
    r0 = 0.05
    kappa = 0.50
    theta = 0.05
    sigma = 0.90
    scheme = FinCIRNumericalScheme.MILSTEIN
    modelParams = (r0, kappa, theta, sigma, scheme)
    start = time.time()
    paths = modelSim.getProcess(
        FinProcessTypes.CIR,
        t,
        modelParams,
        numAnnSteps,
        numPaths,
        seed)
    end = time.time()
    elapsed = end - start
    print("CIR", elapsed)
    if printPaths:
        print(paths)


test_FinProcessSimulator()
