# -*- coding: utf-8 -*-
"""
    7.11.py
    ~~~~~~~

        内联回调函数
        任何一段框架都应该有一个控制流，也就是主线程，但是过多的函数或许会导致
        控制流的丢失。
        当回调函数过多时也会如此
        因此可以通过生成器和协程将回调函数内联到一个函数中。
"""
# 一个普通的函数 aysnc 异步
def apply_aysnc(func, args, *, callback):
    result = func(*args)
    callback(result)


"""
        --------------------------------------
        |                                    |
        |         /                \         |
        |                                    |
        |                                    |
        |                                    |
        |                口                  |
        |                                    |
        |                                    |
        |     暂时看不懂～～～　先看后面的吧!    |
        |____________________________________|
"""
from queue import Queue
from functools import wraps


class Async:
    """一个异步类"""
    def __init__(self, func, args):
        self.func = func
        self.args - args


def inlined_async(func):
    """内联装饰器"""
    @wraps(func)
    def wrapper(*args):
        func_result = func(*args) # 装饰器的道德 func_result是一个生成器，至少我是把他那样看的！
        result_queue = Queue() # 实例化一个结果队列
        result_queue.put(None) # 初始化队列为None
        while True:
            result = result_queue.get() # 从队列中获取结果
            try:
                a = func_result.send(result) # a 是生成器的下一个值
                apply_aysnc(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


def add(x, y):
    """add函数作为结果函数"""
    return x + y


#　内联回调函数
@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'neo1218'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print("google !")


# 生成器：含有yield的函数就是生成器
# 生成器可以挂起(随停随用)，所以将生成器置于无限循环中并无影响
