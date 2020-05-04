# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:10:19 2018

@author: Dominic O'Kane
"""

from financepy.finutils.FinDate import FinDate
from financepy.finutils.FinDayCount import FinDayCount, FinDayCountTypes

print("DAY_COUNT_METHOD", "START", "END", "ALPHA")

for dayCountMethod in FinDayCountTypes:

    startDate = FinDate(2019, 1, 1)
    nextDate = startDate
    numDays = 10
    dayCount = FinDayCount(dayCountMethod)

    for i in range(0, numDays):
        nextDate = nextDate.addDays(7)
        alpha = dayCount.yearFrac(startDate, nextDate, nextDate)
        print(str(dayCountMethod), str(startDate), str(nextDate), alpha)
