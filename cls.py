#!/usr/bin/env python
# encoding: utf-8
"""
    8.13.py
    ~~~~~~~

        实现一种数据模型或类型系统
"""
# 我们想定义各种各样的数据结构，但对某些特定的属性，
# 我们想对赋给他们的值强制添加一些限制。


# 1.用描述符实现基类，用于设置基本(key-value)属性
class Descriptor:
    """这是一个弱绑定描述符"""
    def __init__(self, name=None, **opts):
        self.name = name
        # 设置属性
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        """将属性写入实例字典"""
        instance.__dict__[self.name] = value


# 使用这个描述符的子类建立类型检查
class Typed(Descriptor):
    """类型检查类"""
    expected_type = type(None)  # 默认情况下是None类型

    def __set__(self, instance, value):
        """添加类型检查"""
        if not isinstance(value, self.expected_type):
            raise TypeError('Expect ' + str(self.expected_type))
        super(Typed, self).__set__(instance, value)


class Unsigned(Descriptor):
    """符号检查类"""
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expect value >= 0')
        super(Unsigned, self).__set__(instance, value)


class Maxsize(Descriptor):
    """字符串长度检查类"""
    def __init__(self, name=None, **opts):
        """添加属性存在检查"""
        if 'size' not in opts:
            raise TypeError('Missing size!')
        super().__init__(name, **opts)  # 父类的name已经默认设置 设置属性，可以调用

    def __set__(self, instance, value):
        """添加字符串大小检查"""
        if len(value) > self.size:
            raise TypeError('Expect len value <= size')
        super().__set__(instance, value)


# 将这些检查类添加进数据构造类中
class Integer(Typed):
    """整型类"""
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    """无符号整型类"""
    pass


class Float(Typed):
    """浮点数类"""
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    """无符号浮点数类"""
    pass


class String(Typed):
    """字符串类"""
    expected_type = str


class SizedStr(String, Maxsize):
    """无符号字符串类"""
    pass


# 接下来就可以用这些数据结构类构造一个类啦
class Stock:
    """股票类"""
    # 类变量定义
    name = SizedStr('name', size=8)  # 参数是传递Descriptor类的参数
    shares = UnsignedInteger('shares')
    prices = UnsignedFloat('prices')

    def __init__(self, name, shares, prices):
        self.name = name
        self.shares = shares
        self.prices = prices
