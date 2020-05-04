# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 07:26:46 2016

@author: Dominic O'Kane
"""

from financepy.finutils.FinDate import FinDate

startDate = FinDate(2018, 1, 1)

# Testing adjustment using CDS date adjustment
print("DATE", "MONTHS", "CDS DATE")

for numMonths in range(0, 10):
    nextCDSDate = startDate.nextCDSDate(numMonths)
    print(str(startDate), numMonths, str(nextCDSDate))

startDate = FinDate(2018, 1, 1)

# Testing adjustment using IMM date adjustment
print("STARTDATE", "MONTHS", "CDS DATE")
for numMonths in range(0, 10):
    startDate = startDate.addDays(1)
    nextIMMDate = startDate.nextIMMDate()
    print(numMonths, str(startDate), str(nextIMMDate))
