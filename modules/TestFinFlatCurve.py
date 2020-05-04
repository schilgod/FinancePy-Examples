# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 09:26:27 2016

@author: Dominic O'Kane
"""


from financepy.market.curves.FinFlatCurve import FinFlatCurve
from financepy.finutils.FinDate import FinDate
import numpy as np






def test_FinFlatCurve():

    curveDate = FinDate(2019, 2, 2)
    times = np.linspace(0.0, 1.0, 5)

    print("COMPOUNDING", "DFS")
    compounding = -1
    flatCurve = FinFlatCurve(curveDate, 0.05, compounding)
    dfs = flatCurve.df(times)
    print(compounding, dfs)

    compounding = 1
    flatCurve = FinFlatCurve(curveDate, 0.05, compounding)
    dfs = flatCurve.df(times)
    print(compounding, dfs)

    compounding = 2
    flatCurve = FinFlatCurve(curveDate, 0.05, compounding)
    dfs = flatCurve.df(times)
    print(compounding, dfs)

    compounding = 4
    flatCurve = FinFlatCurve(curveDate, 0.05, compounding)
    dfs = flatCurve.df(times)
    print(compounding, dfs)

    compounding = 12
    flatCurve = FinFlatCurve(curveDate, 0.05, compounding)
    dfs = flatCurve.df(times)
    print(compounding, dfs)

    compounding = 0
    flatCurve = FinFlatCurve(curveDate, 0.05, compounding)
    dfs = flatCurve.df(times)
    print(compounding, dfs)


test_FinFlatCurve()
