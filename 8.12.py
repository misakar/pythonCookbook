#!/usr/bin/env python
# encoding: utf-8

"""
    8.12.py
    ~~~~~~~

        定义一个接口和抽象基类
"""
# 什么是接口？：接口就是暴露给代码使用者的操作集合
# 我们想定义一个类作为接口或者是抽象基类，这样可以在此之上执行类型检查并确保在子类中实现特定的方法
# 抽象基类（abc）(abstruct base class)，抽象基类是唯一一个不能被实例化的类，他的存在意义是子类的继承


from abc import ABCMeta, abstructmethod


class IStream(ABCMeta):
    @abstructmethod
    def read(self, maxbytes=-1):
        pass

    @abstructmethod
    def write(self, data):
        pass


# 抽象基类是给其他类当基类使用的，这些子类需要实现abc定义的方法


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


# 可以理解为抽象基类是一种信仰，如果你信奉abc，那么就照着abc定义的那样做!


# 抽象基类强制定义了一些接口，我们可以检查这些接口
def serialize(obj, stream):
    """分析抽象基类的接口"""
    if not isinstance(stream, IStream):
        raise TypeError('Expect an IStream!')
    pass


# 抽象基类的接口不仅仅可以在子类中实现，我们还可以用抽象基类注册其他类，
# 从而使其他类也具有这样的接口
import io


IStream.register(io.IOBase)  # 向io的基类注册IStream接口
f = open('foo.txt')  # f是一个io对象
isinstance(f, IStream)  # return True !
