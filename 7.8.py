# -*- coding: utf-8 -*-

"""
    7.8.py
    ~~~~~~

        让带有N个参数的可调用对象以较少的参数形式调用
"""
from functools import partial
from math import hypot  # 计算sqrt(x2 + y2)函数 -- 好贴心呀!!


def spam(a,b,c,d,e):
    print (a,b,c,d,e)


# use partial
# partial 返回的是一个全新的对象
# 对于可以确定的参数可以通过partial减少调用时的赋值
new_spam = partial(spam, b=2, c=3, d=4)
new_spam(1, e=5)


# partial经常用在参数的一致性上
def func1(x):
    pass
def func2(x, y):
    pass
func1(partial(func2, y=1))
