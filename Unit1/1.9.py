#!/usr/bin/env python
# encoding: utf-8

"""
    1.9.py
    ~~~~~~

        在两个字典中寻找相同点

        操作符在字典中的使用
"""

a = {'x':1, 'y':2, 'z':3}
b = {'w':3, 'x':10, 'b':4}


# 找寻a，b字典中相同的键
a.keys() & b.keys()


# 找寻a，b字典中相同的键值对
a.items() & b.items()


# 从a字典中创建一个新的字典c
c = {key : a[key] for key in a.keys() - {'x'}}
