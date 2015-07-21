#!/usr/bin/env python
# encoding: utf-8
"""
    8.10.py
    ~~~~~~~

        让属性具有惰性求值的能力
"""
# 描述符和@property装饰器让属性具有惰性求值的能力，惰性求值－希望将
# 一个只读的属性定义为property方法，并只有在访问时才参与计算，一旦
# 访问了该属性，我们希望把值缓存起来，不必每次都重新计算


class lazyproperty:
    """惰性属性装饰器"""
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            # instance.self.func.__name__ = value
            # __name__ 返回对象的名字
            # 原理就是把函数名和返回值作为属性存储在类变量字典中
            # 达到缓存的目的
            return value


# 使用
import math


class Circle:
    def __init__(self, r):
        self.r = r

    @lazyproperty
    def area(self):
        print("计算面积")
        return math.pi * self.r**2

    @lazyproperty
    def perimeter(self):
        print("计算周长")
        return 2*math.pi*self.r
