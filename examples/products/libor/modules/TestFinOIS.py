# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 14:23:13 2016

@author: Dominic O'Kane
"""

from financepy.finutils.FinMath import ONE_MILLION
from financepy.products.libor.FinOIS import FinOIS
from financepy.market.curves.FinFlatCurve import FinFlatCurve
from financepy.finutils.FinFrequency import FinFrequencyTypes
from financepy.finutils.FinDayCount import FinDayCountTypes
from financepy.finutils.FinDate import FinDate







def test_OIS():

    startDate = FinDate(2018, 11, 30)
    endDate = FinDate(2028, 6, 20)

    endDate = startDate.addMonths(60)
    oisRate = 0.04
    isPayer = True
    fixedFreq = FinFrequencyTypes.ANNUAL
    fixedDayCount = FinDayCountTypes.ACT_ACT_ISDA
    floatFreq = FinFrequencyTypes.ANNUAL
    floatDayCount = FinDayCountTypes.ACT_ACT_ISDA
    notional = ONE_MILLION

    ois = FinOIS(startDate,
                 endDate,
                 oisRate,
                 fixedFreq,
                 fixedDayCount,
                 floatFreq,
                 floatDayCount,
                 isPayer,
                 notional)

    valueDate = FinDate(2018, 11, 30)
    marketRate = 0.05
    indexCurve = FinFlatCurve(valueDate, marketRate, 1)
    ois.print(valueDate, indexCurve)

    v = ois.value(startDate, indexCurve)
    print("LABEL", "VALUE")
    print("SWAP_VALUE", v)


test_OIS()
# 
