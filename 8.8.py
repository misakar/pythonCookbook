# -*- coding: utf-8 -*-
"""
    8.8.py
    ~~~~~~

        在子类中扩展属性
"""
# 使用@porperty装饰器可以管理属性，使用super可以调用父类属性
# 从而我们可以在子类扩展父类的属性
# super 调用父类属性，porperty 重写属性方法


class Persion:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name  # 使用了模块的私有变量

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expect a string!')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('Can not del a attribute!')


class SubPersion(Persion):
    @property
    def name(self):
        print ('Geting a name!')
        super(SubPersion, self).name

    @name.setter
    def name(self, value):
        print ('Setting a name to ', value)
        super(SubPersion, SubPersion).name.__set__(self, value)

    @name.deleter
    def name(self):
        print ('Deleting name!')
        super(SubPersion, SubPersion).name.__delete__(self)


# Use this class
# 可以把函数当成属性使用，直接进行赋值操作
s = SubPersion('neo1218')
s
s.name = 'jack'
s
s.name
