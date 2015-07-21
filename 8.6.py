# -*- coding: utf-8 -*－
"""
    8.6.py
    ~~~~~~

        创建便于操作的属性
        把函数转变为属性进行操作
        把对属性的存取操作函数直接转化为对属性的操作
"""


# 使用@property装饰器
class Persion:
    """class Persion"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        """name属性的get函数"""
        return self.name

    @name.setter
    def set_name(self, value):
        """name属性的set函数，添加了类型检查
        重写了set函数"""
        if not isinstance(value, str):
            raise TypeError("expect a string!")
        self.name = value

    @name.deletter
    def del_name(self):
        """name属性的del函数"""
        raise AttributeError('Can not delete a attritube!')

    def __repr__(self):
        """自定义 对象的官方表示"""
        return '<{0!r} is a instance of class Persion>'.format(self)


# 以上等价与使用property函数
class Persion2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("expect a string!")
        self.name = value

    def del_name(self):
        raise AttributeError('Can not delete a attritube!')

    def __repr__(self):
        return '<{0!r} is a instance of class Persion>'.format(self)

    # 设置属性
    name = property(get_name, set_name, del_name)
    del get_name, set_name, del_name


# 那么这样写有什么作用呢？
# 这样最显著的变化就是我们可以像调用属性那样调用函数
# obj.name, obj.get_name, obj.set_name
# 这样调用接口就会统一，优雅的编程接口
# 还可以重写属性存取函数，从而增加一些高级功能
