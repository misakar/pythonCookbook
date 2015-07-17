# -*- coding: utf-8 -*-

# 单个变量的类
class ResultHandler:
    def __init__(self):
        """保留sequence变量"""
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print ("[{}] Got: {}".format(self.sequence, result))

# 闭包函数替代
def result_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print ("[{}] Got: {}".format(sequence, result))
    return handler


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def add(x, y):
    return x + y


apply_async(add, (2, 4), callback=result_handler())
