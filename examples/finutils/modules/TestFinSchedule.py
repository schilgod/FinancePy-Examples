# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 14:31:53 2016

@author: Dominic O'Kane
"""

from financepy.finutils.FinCalendar import FinDayAdjustTypes, FinDateGenRuleTypes
from financepy.finutils.FinSchedule import FinSchedule
from financepy.finutils.FinFrequency import FinFrequencyTypes
from financepy.finutils.FinCalendar import FinCalendarTypes
from financepy.finutils.FinDate import FinDate

###############################################################################


def test_FinSchedule():

    d1 = FinDate(2018, 6, 20)
    d2 = FinDate(2018, 6, 20)
    frequencyType = FinFrequencyTypes.SEMI_ANNUAL
    calendarType = FinCalendarTypes.WEEKEND
    busDayAdjustType = FinDayAdjustTypes.FOLLOWING
    dateGenRuleType = FinDateGenRuleTypes.BACKWARD

    schedule = FinSchedule(
        d1,
        d2,
        frequencyType,
        calendarType,
        busDayAdjustType,
        dateGenRuleType)

    print("SEMI-ANNUAL FREQUENCY")
    for dt in schedule._adjustedDates:
        print(str(dt))

    d1 = FinDate(2018, 6, 20)
    d2 = FinDate(2028, 6, 20)
    frequencyType = FinFrequencyTypes.SEMI_ANNUAL
    calendarType = FinCalendarTypes.WEEKEND
    busDayAdjustType = FinDayAdjustTypes.FOLLOWING
    dateGenRuleType = FinDateGenRuleTypes.BACKWARD

    schedule = FinSchedule(
        d1,
        d2,
        frequencyType,
        calendarType,
        busDayAdjustType,
        dateGenRuleType)

    print("QUARTERLY FREQUENCY")
    for dt in schedule._adjustedDates:
        print(str(dt))

    d1 = FinDate(2018, 6, 20)
    d2 = FinDate(2028, 6, 20)
    frequencyType = FinFrequencyTypes.MONTHLY
    calendarType = FinCalendarTypes.WEEKEND
    busDayAdjustType = FinDayAdjustTypes.FOLLOWING
    dateGenRuleType = FinDateGenRuleTypes.BACKWARD

    schedule = FinSchedule(
        d1,
        d2,
        frequencyType,
        calendarType,
        busDayAdjustType,
        dateGenRuleType)

    print("MONTHLY FREQUENCY")
    for dt in schedule._adjustedDates:
        print(str(dt))

    d1 = FinDate(2018, 6, 20)
    d2 = FinDate(2028, 6, 20)
    frequencyType = FinFrequencyTypes.ANNUAL
    calendarType = FinCalendarTypes.WEEKEND
    busDayAdjustType = FinDayAdjustTypes.FOLLOWING
    dateGenRuleType = FinDateGenRuleTypes.FORWARD

    schedule = FinSchedule(
        d1,
        d2,
        frequencyType,
        calendarType,
        busDayAdjustType,
        dateGenRuleType)

    print("FORWARD GEN")
    for dt in schedule._adjustedDates:
        print(str(dt))

    d1 = FinDate(2018, 6, 20)
    d2 = FinDate(2028, 6, 20)
    frequencyType = FinFrequencyTypes.ANNUAL
    calendarType = FinCalendarTypes.WEEKEND
    busDayAdjustType = FinDayAdjustTypes.FOLLOWING
    dateGenRuleType = FinDateGenRuleTypes.BACKWARD

    schedule = FinSchedule(
        d1,
        d2,
        frequencyType,
        calendarType,
        busDayAdjustType,
        dateGenRuleType)

    print("BACKWARD GEN")
    for dt in schedule._adjustedDates:
        print(str(dt))

    d1 = FinDate(2018, 6, 20)
    d2 = FinDate(2028, 6, 20)
    frequencyType = FinFrequencyTypes.SEMI_ANNUAL
    calendarType = FinCalendarTypes.WEEKEND
    busDayAdjustType = FinDayAdjustTypes.FOLLOWING
    dateGenRuleType = FinDateGenRuleTypes.BACKWARD

    schedule = FinSchedule(
        d1,
        d2,
        frequencyType,
        calendarType,
        busDayAdjustType,
        dateGenRuleType)

    print("BACKWARD GEN WITH SHORT END STUB")
    for dt in schedule._adjustedDates:
        print(str(dt))

    d1 = FinDate(2018, 6, 20)
    d2 = FinDate(2028, 6, 20)
    frequencyType = FinFrequencyTypes.SEMI_ANNUAL
    calendarType = FinCalendarTypes.WEEKEND
    busDayAdjustType = FinDayAdjustTypes.FOLLOWING
    dateGenRuleType = FinDateGenRuleTypes.FORWARD

    schedule = FinSchedule(
        d1,
        d2,
        frequencyType,
        calendarType,
        busDayAdjustType,
        dateGenRuleType)

    print("FORWARD GEN WITH LONG END STUB")
    for dt in schedule._adjustedDates:
        print(str(dt))

    print("BACKWARD GEN WITH TARGET CALENDAR")

    d1 = FinDate(2018, 6, 20)
    d2 = FinDate(2028, 6, 20)
    frequencyType = FinFrequencyTypes.SEMI_ANNUAL
    calendarType = FinCalendarTypes.TARGET
    busDayAdjustType = FinDayAdjustTypes.FOLLOWING
    dateGenRuleType = FinDateGenRuleTypes.BACKWARD

    schedule = FinSchedule(
        d1,
        d2,
        frequencyType,
        calendarType,
        busDayAdjustType,
        dateGenRuleType)
    for dt in schedule._adjustedDates:
        print(str(dt))


test_FinSchedule()
