# -*- coding: utf-8 -*-

"""
    9.5.py
    ~~~~~~

        定义一个属性可由用户修改的装饰器
"""
# 引入访问函数（access function）
# 使用nonlocal关键字声明变量来修改装饰器内部属性
# 把访问器函数作为函数属性附加到包装函数上
# python2.x系列没有nonlocal关键字，所以只有使用全局global关键字
from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):
    """向函数func添加obj属性"""
    if fanc is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """
    装饰器函数，向函数添加日志记录并允许用户自己设置日志
    的等级，和希望输出的信息（以便记录）
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # 设置属性 -- level
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            # nonlocal level # 使用nonlocal关键字可以让解释器在外层查找变量，从而可以修改变量
            global level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            # nonlocal logmsg
            global logmsg
            logmsg = newmsg

        return wrapper
    return decorate


# 使用装饰器
@logged
def test(x, y):
    return x + y
