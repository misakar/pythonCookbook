# -*- coding: utf-8 -*-

"""
    9.6.py
    ~~~~~~

        定义一个能接受可选参数的装饰器
"""
# 定义一个既可以 @decorator 修饰，也可以 @decorator(x, y, z) 修饰的装饰器


from functools import partial, wraps
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper


# 使用装饰器
@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name='neo1218')
def Goal():
    print "Goal!!!"
