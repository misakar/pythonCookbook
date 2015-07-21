#!/usr/bin/env python
# encoding: utf-8
"""
    8.9.py
    ~~~~~~

        类描述符的使用
        描述符是具有对属性字典存取函数(set, get, del)的类
        使用描述符在类变量的层面初始化属性
        从而可以添加属性操作，实现更复杂的功能
        描述符还可以代码复用，广泛应用于大型框架中
"""


class Integer:
    """一个描述符类"""
    def __init__(self, x):
        """定义变量操作"""
        self.x = x

    def __get__(self, instance, cls):
        """有两种访问方式
        １实例访问: Class.__get__(instance, Class)
        ２类访问  : Class.__get__(None, Class)"""
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.x)  # self.x 为键

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expect a int')
        instance.__dict__[self.x] = value  # get只是访问字典中的值

    def __delete__(self, instance):
        del instance.__dict__[self.x]


# 使用这个描述符类
class Value:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# main
v = Value
v.x = 1
v.y = 1.2
Value.x
