# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:04:57 2019

@author: Dominic
"""

import numpy as np
import time

from financepy.products.equity.FinEquityBinomialTree import FinEquityBinomialTree
from financepy.products.equity.FinEquityBinomialTree import FinEquityTreeExerciseTypes
from financepy.products.equity.FinEquityBinomialTree import FinEquityTreePayoffTypes
from financepy.products.equity.FinEquityVanillaOption import FinEquityVanillaOption
from financepy.products.FinOptionTypes import FinOptionTypes
from financepy.finutils.FinDate import FinDate
from financepy.products.equity.FinEquityModelTypes import FinEquityModelBlackScholes
from financepy.market.curves.FinFlatCurve import FinFlatCurve


def test_FinBinomialTree():

    stockPrice = 50.0
    riskFreeRate = 0.06
    dividendYield = 0.04
    volatility = 0.40

    valueDate = FinDate(2016, 1, 1)
    expiryDate = FinDate(2017, 1, 1)

    model = FinEquityModelBlackScholes(volatility)
    discountCurve = FinFlatCurve(valueDate, riskFreeRate)

    numStepsList = [100, 500, 1000, 2000, 5000]

    strikePrice = 50.0

    print("================== EUROPEAN PUT =======================")

    putOption = FinEquityVanillaOption(
        expiryDate,
        strikePrice,
        FinOptionTypes.EUROPEAN_PUT)
    value = putOption.value(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    delta = putOption.delta(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    gamma = putOption.gamma(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    theta = putOption.theta(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    print("BS Value", "BS Delta", "BS Gamma", "BS Theta")
    print(value, delta, gamma, theta)

    payoff = FinEquityTreePayoffTypes.VANILLA_OPTION
    exercise = FinEquityTreeExerciseTypes.EUROPEAN
    params = np.array([-1, strikePrice])

    print("NumSteps", "Results", "TIME")

    for numSteps in numStepsList:
        start = time.time()
        tree = FinEquityBinomialTree()
        results = tree.value(
            stockPrice,
            discountCurve,
            dividendYield,
            volatility,
            numSteps,
            valueDate,
            payoff,
            expiryDate,
            payoff,
            exercise,
            params)
        end = time.time()
        duration = end - start
        print(numSteps, results, duration)

    print("================== AMERICAN PUT =======================")

    payoff = FinEquityTreePayoffTypes.VANILLA_OPTION
    exercise = FinEquityTreeExerciseTypes.AMERICAN
    params = np.array([-1, strikePrice])

    print("NumSteps", "Results", "TIME")

    for numSteps in numStepsList:
        start = time.time()
        tree = FinEquityBinomialTree()
        results = tree.value(
            stockPrice,
            discountCurve,
            dividendYield,
            volatility,
            numSteps,
            valueDate,
            payoff,
            expiryDate,
            payoff,
            exercise,
            params)
        end = time.time()
        duration = end - start
        print(numSteps, results, duration)

    print(
        "================== EUROPEAN CALL =======================")

    callOption = FinEquityVanillaOption(
        expiryDate,
        strikePrice,
        FinOptionTypes.EUROPEAN_CALL)
    value = callOption.value(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    delta = callOption.delta(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    gamma = callOption.gamma(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    theta = callOption.theta(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    print("BS Value", "BS Delta", "BS Gamma", "BS Theta")
    print(value, delta, gamma, theta)

    payoff = FinEquityTreePayoffTypes.VANILLA_OPTION
    exercise = FinEquityTreeExerciseTypes.EUROPEAN
    params = np.array([1.0, strikePrice])

    print("NumSteps", "Results", "TIME")
    for numSteps in numStepsList:
        start = time.time()
        tree = FinEquityBinomialTree()

        results = tree.value(
            stockPrice,
            discountCurve,
            dividendYield,
            volatility,
            numSteps,
            valueDate,
            payoff,
            expiryDate,
            payoff,
            exercise,
            params)

        end = time.time()
        duration = end - start
        print(numSteps, results, duration)

    print(
        "================== AMERICAN CALL =======================")

    payoff = FinEquityTreePayoffTypes.VANILLA_OPTION
    exercise = FinEquityTreeExerciseTypes.AMERICAN
    params = np.array([1.0, strikePrice])

    print("NumSteps", "Results", "TIME")
    for numSteps in numStepsList:
        start = time.time()
        tree = FinEquityBinomialTree()

        results = tree.value(
            stockPrice,
            discountCurve,
            dividendYield,
            volatility,
            numSteps,
            valueDate,
            payoff,
            expiryDate,
            payoff,
            exercise,
            params)

        end = time.time()
        duration = end - start
        print(numSteps, results, duration)


test_FinBinomialTree()
