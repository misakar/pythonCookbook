#!/usr/bin/env python
# encoding: utf-8

"""
    8.15.py
    ~~~~~~~

        实现在一个类中，将方法调用委托(delegate)给一个内部实例
"""


class A:
    def spam(self, x):
        print(x)

    def foo(self):
        pass


class B:
    """并未使用继承"""
    def __init__(self):
        self.a = A()  # 实现了一个 internal instance (被委托对象)

    def bar(self):
        pass

    def __getattr__(self, name):
        """将方法调用委托个内部实例"""
        return getattr(self.a, name)


# 注意B实例可以调用A中的spam方法
# call B.__getattr__('spam') -> a.getattr(spam') -> 返回值
