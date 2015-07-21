#!/usr/bin/env python
# encoding: utf-8

"""
    8.11.2.py
    ~~~~~~~~~

        添加关键字参数
"""


class Structure:
    _fields = []  # 初始化变量名称列表

    def __init__(self, *args, **kwargs):
        if len(*args) > len(self._fields):
            raise TypeError('Expect {} arguments'.format(len(self._fields)))

        # 处理位置参数
        for name, value in zip(self._fields, *args):
            setattr(self, name, value)

        # 处理关键字参数
        for name in self._fields:
            setattr(self, name, kwargs.pop(name))  # 使用pop出栈操作，避免字典中的值重复

        # 处理多余参数
        if kwargs:
            # ','.join(dict): 返回字典键组成的字符串
            raise TypeError('Invalid argument(s) {}'.format(','.join(kwargs)))


# 示例使用
if __name__ == '__main__':

    class Stock(Structure):
        _fields = ['name', 'shares', 'price']
