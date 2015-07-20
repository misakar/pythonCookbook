# -*- coding: utf-8 -*-

"""
    7.2.py
    ~~~~~~

        编写只接受关键字参数的函数
"""
# 关键字参数与位置参数的区别：位置参数不能
# 随便移动位置，而关键字参数与位置无关
# 关键字参数的可读性比较好
# 我们不知道位置参数有多少！不过　*  搞定
# 只需把 key-only 放在*后
def minfunc(*values, flag=None):
    # m是位置参数的最小值
    m = min(values) # values 是一个元组
    if flag is not None:
        m = flag if flag < m else m
    print (m)


def maxfunc(value, *, clip):
    """key-only放置于*后"""
    print (clip)


# main
# 当位置参数个数不定，但须指定关键字参数时
minfunc(1,2,3,4,5)                # 1
minfunc(1,2,3,4, clip=0)          # 0
maxfunc(1, clip=8)                # 8
