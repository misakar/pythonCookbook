# -*- coding: utf-8 -*-
"""
    8.3.py
    ~~~~~~

        处理百万级别的数据减少内存消耗
"""
# 这里使用槽属性，相比于一般的属性字典创建，使用槽会围绕这一个小型数组建立映射
# 消耗更少的内存


class ClassName(object):
    """docstring for """
    __slot__ = ['', '', '']

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


class Date:
    """处理大量日期的类"""
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


# 使用槽的好处是，类将不会围绕字典创建变量，而是依据一个小型数组
