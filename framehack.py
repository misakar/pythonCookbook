#!/usr/bin/env python
# encoding: utf-8

"""
    framehack.py
    ~~~~~~~~~~~~

        自动化实例变量初始化处理
        ------- 仅供欣赏 -------
"""


def init_fromlocals(self):
    import sys
    locs = sys._getframe(1).f_locals
    for key, value in locs.items():
        if key != 'self':
            setattr(self, key, value)


class Stock:
    def __init__(self, name, share, price):
        init_fromlocals(self)
