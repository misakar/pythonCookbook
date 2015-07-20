# -*- coding: utf-8 -*-
"""
    corutine.py
    ~~~~~~~~~~~

        python 协程
"""
def apply_async(func, args, *, callback): # 这是一个逆向的过程，args是一个元组, callback是回调函数
    """一个异步函数,他会调用一个回调函数
       将func函数的结果传递给回调函数"""
    result = func(*args) # 将args解析为参数
    callback = result


def print_result(result):
    print('Got', result)


def add(x:str, y:str):
    return x+y


print_info = apply_async(add, ('neo1218', 'python'), callback=print_result)


# 1.类
class ResultHandler:
    def __init__(self):
        self.seq = 0
    def handler(self, result):
        self.seq += 1
        print('[{}] Got: {}'.format(self.seq, result))


# 2.闭包
def result_handler():
    seq = 0
    def handler(result):
        nonlocal seq
        seq += 1
        print('[{}] Got: {}'.format(seq, result))


# 3.协程
def make_handler():
    seq = 0
    while True:
        result = yield # 生成器的使用
        seq += 1
        print('[{}] Got: {}'.format(seq, result))


# 使用
# 1. 类
r = ResultHandler()
print_info_class = apply_async(add, ('neo1218', 'python'), callback=r.handler)


# 2.闭包
handler = result_handler()
print_info_close = apply_async(add, ('neo1218', 'python'), callback=handler)


# 3.协程
handler = make_handler()
next(handler) # Advance to yield
# 协程使用send函数作为回调函数
print_info_corutine = apply_async(add, ('neo1218', 'python'), callback=handler.send)
