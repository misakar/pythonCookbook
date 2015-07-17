# -*- coding: utf-8 -*-

"""
    7.2.py
    ~~~~~~

        编写只接受关键字参数的函数
"""
# 只需把 key-only 放在*后
def minfunc(*values, clip=None):
    m = min(values) # values 是一个元组
    if clip is not None:
        m = clip if clip < m else m
    print (m)


def maxfunc(value, *, clip):
    """key-only放置于*后"""
    print (clip)


# main
minfunc(1,2,3,4,5)              # 1
minfunc(1,2,3,4, clip=0)        # 0
maxfunc(1, clip=8)              # 8
