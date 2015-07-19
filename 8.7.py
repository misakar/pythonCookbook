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
        super().spam # 调用父类的ｓｐａｍ方法
        print ('B.spam')


# 关于python继承的实现：
# python会对每一个类进行计算，求出方法解析元组　MRO,
# 所以可能完全无关的两个类也会因为第三个类产生关联
# A, B, C(A,B), A中使用super函数会调用B中的方法


# 感觉很多python的用法比较难懂，不知道是书的问题（翻译）,还是作者故意搞这些小技巧
# 还是python内部的实现问题
