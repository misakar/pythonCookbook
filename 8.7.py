# -*- coding: utf-8 -*-
"""
    8.7.py
    ~~~~~~

        调用父类中的方法
"""
# 采用 super() 函数调用父类中的方法


class A:
    def spam(self):
        print ('A.spam')


class B(A):
    """继承自A"""
    def spam(self):
        super().spam  # 调用父类的ｓｐａｍ方法
        print ('B.spam')


# 关于python继承的实现：
# python会对每一个类进行计算，求出方法解析元组　MRO,
# 所以可能完全无关的两个类也会因为第三个类产生关联
# A, B, C(A,B), A中使用super函数会调用B中的方法


# super(type, obj) -> bound super object
