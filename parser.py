# -*- coding: utf-8 -*-
"""
    A simple parser to understand sentence for trello.
    
    Copyright: (c) 2014 by Zhu Xiaoen.
"""

import time
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

NOT_EXIST = -999
days_dt = {
            "今天": 0, "明天": 1, "后天": 2, "大后天": 3,
            "昨天": -1, "前天": -2 }
week_dt = {
            "上周日": -7, "上周一": -6, "上周二": -5, "上周三": -4,
            "上周四": -3, "上周五": -2, "上周六": -1,
            "周日": 0, "周一": 1, "周二": 2, "周三": 3,
            "周四": 4, "周五": 5, "周六": 6,
            "下周日": 7, "下周一": 8, "下周二": 9, "下周三": 10,
            "下周四": 11, "下周五": 12, "下周六": 13 }
week_order = [
            "上周日", "上周一", "上周二", "上周三", "上周四", "上周五", "上周六",
            "下周日", "下周一", "下周二", "下周三", "下周四", "下周五", "下周六",
            "周日", "周一", "周二", "周三", "周四", "周五", "周六" ]

moment_dt = {
        "早上": 7, "上午": 10, "中午": 12, "下午": 14, "晚上": 20, "睡前": 23}

class Parser():

    def __init__(self, t):
        """
            t: time.time() or time object
        """
        self.curr_dt = datetime.datetime.fromtimestamp(t)

    def parse_week_offset(self, sentence):
        week = self.curr_dt.isocalendar()[2]

        for order in week_order:
            if order in sentence:
                return week_dt[order] - week

        return NOT_EXIST

    def parse_day_offset(self, sentence):
        for day in days_dt:
            if day in sentence:
                return days_dt[day]

        return NOT_EXIST

    def parser_moment(self, sentence):
        for moment in moment_dt:
            if moment in sentence:
                return moment_dt[moment]

        return NOT_EXIST

    def parser_clock(self, sentence):
        index = sentence.find(u"点")

        if index == -1 or index == 0:
            return NOT_EXIST

        if not sentence[index-1].isdigit():
            return NOT_EXIST
        c1 = int(sentence[index-1])

        if index == 1:
            c2 = 0
        elif not sentence[index-2].isdigit():
            c2 = 0
        else:
            c2 = int(sentence[index-2])
        
        cl = c2*10 + c1
        if cl >= 24:
            return NOT_EXIST

        return cl

    def parse_clock_and_moment(self, sentence):
        clock = self.parser_clock(sentence)
        if clock == NOT_EXIST:
            clock = self.parser_moment(sentence)

        return clock

    def parse_day_and_week(self, sentence):
        day_off = self.parse_day_offset(sentence)
        if day_off == NOT_EXIST:
            day_off = self.parse_week_offset(sentence)

        return day_off

    def parse(self, sentence):
        """ Return a datetime object"""
        clock = self.parse_clock_and_moment(sentence)
        day_off = self.parse_day_and_week(sentence)

        parse_dt = self.curr_dt
        if clock is NOT_EXIST and day_off is NOT_EXIST:
            # Return curr time
            return parse_dt
        else:
            if clock is not NOT_EXIST:
                parse_dt = parse_dt.replace(hour=clock)
            if day_off is not NOT_EXIST:
                parse_dt = parse_dt + datetime.timedelta(days=day_off)

            return parse_dt
