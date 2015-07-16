# -*- coding: utf-8 -*-

"""
    9.1.py
    ~~~~~~
    给函数添加一个包装
    1. 元编程： 用美妙的函数或类来处理重复性的代码和工作
"""
import time
from functools import wraps # 导入装饰器模块


def time_func(func):
    """一个装饰器，添加计算函数执行时间的功能"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper 被修饰函数"""
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print ("The time of %s : %d") % (func.__name__, end - start)
        return result
    return wrapper


@time_func  # @语法糖
def test(n):
    """测试函数"""
    while n > 0 :
        n -= 1


# 使用这个装饰器1
test(1000000)


# 使用这个装饰器2
test = time_func(test)
test(1000000) # 为什么会有两个输出？ 难道是个 bug ?
print test.__name__
print test.__doc__
