# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 07:26:46 2016

@author: Dominic O'Kane
"""

from financepy.finutils.FinDate import FinDate

startDate = FinDate(2018, 2, 23)

print("StartDate:", startDate)

tenor = "0m"
print(tenor, startDate.addTenor(tenor))

tenor = "5d"
print(tenor, startDate.addTenor(tenor))

tenor = "7D"
print(tenor, startDate.addTenor(tenor))

tenor = "1W"
print(tenor, startDate.addTenor(tenor))

tenor = "4W"
print(tenor, startDate.addTenor(tenor))

tenor = "1M"
print(tenor, startDate.addTenor(tenor))

tenor = "24M"
print(tenor, startDate.addTenor(tenor))

tenor = "2Y"
print(tenor, startDate.addTenor(tenor))

tenor = "10y"
print(tenor, startDate.addTenor(tenor))

tenor = "20Y"
print(tenor, startDate.addTenor(tenor))
