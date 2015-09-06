#!/usr/bin/env python
# encoding: utf-8

"""
    1.2.py
    ~~~~~~

        从任意长的可迭代对象中分解元素

        分析:

            赋值分解法虽然简单,但是必须已知可迭代对象所含的元素个数,才能用对应的变量进行分解
            我们可以用python *表达式解决这个问题
            * 表达式可以存储多余的变量到[列表]中
"""

# 案例1:
grades = [1,23,34,56,78,90]


def drop_first_last(grades):
    """去掉最低分和最高分"""
    first, *middle, high = grades
    print middle # middle = [23,34,56,78]
    print avg(middle)


# 案例2:
records = [
    ('jack',19),
    ('neo',20,'hust'),
    ('jack','highschool')
]


def about_jack(x):
    """关于jack的信息"""
    print ('jack:',x)


def about_neo(x,y):
    """关于neo的信息"""
    print ('neo:',y)


# 迭代
def getInfo():
    for tag, *info in records:
        if tag == 'jack':
            about_jack(*info)
        if tag == 'neo'
            about_neo(*info)
