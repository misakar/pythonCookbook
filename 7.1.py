# -*- coding: utf-8 -*-

"""
    7.1.py
    ~~~~~~

        编写可接受任意数量参数的函数
"""
from inspect import signature


def test(*args, **kwargs):
    """
    *args: 接受任意数量的位置参数，存储到元组
    **kwargs: 接受任意数量的关键字参数，存储到字典
    """
    sig = signature(test)
    print (sig)


# main
test(1, 2)
test(1, a=2)
