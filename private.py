#!/usr/bin/env python
# encoding: utf-8
# 测试子类能否继承父类的私有方法和属性


class Father:
    def __init__(self, name, age):
        self._name = name  # name 是私有属性
        self.age = age  # age 是公有属性


class Son(Father):
    def __init__(self, name, age, school):
        super(Son, self).__init__(name, age)
        self.school = school


son = Son('neo1218', 19, 'CCNU')
print(son.school)  # CCNU
print(son._name)  # neo1218


# 可见python的子类是可以调用父类的私有方法的，但是，你要有道德！私有方法就不要去碰了!
