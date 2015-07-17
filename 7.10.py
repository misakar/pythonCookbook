# -*- coding: utf-8 -*-

"""
    7.10.py
    ~~~~~~~

        在回调函数中携带额外的状态
"""
# 一个回调函数
# callback 指定关键字
def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)

# 使用这个回调函数
def add(x, y):
    return x + y


def get_result(result):
    print ("Got:", result)


apply_async(add, (1, 3), callback=get_result)
