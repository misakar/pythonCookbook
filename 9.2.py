# -*- coding: utf-8 -*-

"""
        9.2.py
        ~~~~~~

        编写装饰器时如何保存函数的元数据(文档字符串、函数名)
        只要使用 @wraps(func) 装饰器即可
"""
# 使用 @wraps 装饰器可以帮助我们拷贝被装饰函数的元数据
# 私用 @wraps 装饰器可以通过 __wrapped__ 属性直接访问被装饰函数
# 使用 __wrapped__ 属性可以方便的将函数的底层签名暴露出来
from inspect import signature
print signature(func)

# test : (n:int)
