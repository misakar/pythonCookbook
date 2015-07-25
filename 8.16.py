#!/usr/bin/env python
# encoding: utf-8

"""
    8.16.py
    ~~~~~~~

        在类中实现多个构造函数
"""
# 使用类方法 @classmethod 即可


import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        """today会调用类的__init__方法，不过用classmethod实现了参数层的封装"""
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)
