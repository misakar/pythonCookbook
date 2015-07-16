# -*- coding: utf-8 -*-

"""
    9.4.py
    ~~~~~~

        定义一个可接收参数的装饰器
"""
from functools import wraps
import logging


def logged(level, name=None, message=None):
    """
    向函数添加日志，level就是日志记录的等级，name就是日志名，message就是日志信息
    默认情况下，name是函数的模块，message是函数的信息
    添加了接收外界参数层
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


# 使用装饰器
@logged(logging.DEBUG)
def test(x, y):
    return x + y


"""
@decorator(x, y, z)
def func(a, b):
    pass

实际执行顺序:
def func(a, b):
    pass

func = decorator(a, b, c)(func)
可见，decorator函数返回的对象是一个可调用对象，并接收func作为参数
"""
