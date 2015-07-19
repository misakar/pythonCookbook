# -*- coding: utf-8 -*-
"""
    8.3.py
    ~~~~~~

        处理百万级别的数据减少内存消耗
"""
#　这里使用槽属性，相比于一般的属性字典创建，使用槽会围绕这一个小型数组建立映射
# 消耗更少的内存
class ClassName(object):
    """docstring for """
    __slot__ = ['','','']
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
