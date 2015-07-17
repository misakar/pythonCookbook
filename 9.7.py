# -*- coding: utf-8 -*-

"""
    9.7.py
    ~~~~~~

        利用装饰器对函数参数进行强制类型检查
"""
# 函数签名对象的应用
from inspect import signature
from functools import wraps, partial

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            """如果不是调试模式，不进行参数检查"""
            return func

        sig = signature(func) # sig 返回函数有关参数返回值信息 --> 签名
        # 利用 bind_partial 函数将参数值与类型绑定
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # 强制类型检查
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate


# 使用这个装饰器
# 通过参数指定类型检查
@typeassert(int, int)
def add(x:int, y:int) -> int:
    print (x + y)


# test1
add(2, 4)
# test2
add('neo1218', 5)
# test3
add(3, y=6)
