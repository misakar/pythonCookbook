# -*- coding: utf-8 -*-
"""
    8.1.py
    ~~~~~~

        修改实例的字符串表示
"""
class Example:
    """一个类"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """repr是一个对象的代码表示：obj=eval(repr(obj))"""
        return Example('{0.x!r}, {0.y!r}').format(self)


# Use this class
"""
>> ex = Example(1, 2)
>> ex
Example(1, 2)
"""


# repr方法
# repr实例的官方表示（官方：包含一些信息，而不是单纯的输出）,方便
# 调试 obj = eval(repr(obj))
