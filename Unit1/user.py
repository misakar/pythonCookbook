# coding: utf-8

"""
    1.14.py
    ~~~~~~~

        对不原生支持比较操作的对象排序

        比如我们想对某个类的实例排序
"""

# 内置的sorted函数可以通过key参数传递可调用对象
# 可调用对象会返回待排序对象中的某些值
# sorted函数则利用这些值来比较对象


class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User %r' % self.user_id
