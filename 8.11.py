#!/usr/bin/env python
# encoding: utf-8
"""
    8.11.py
    ~~~~~~~

        简化数据结构的初始化过程
"""
# zip(seq1, seq2) -> [(seq1[0], seq2[0]),...,(seq1[len-1],seq2[len-1])
# zip函数建立了一个列表元组，元组的项是两个列表的对应项。
# 返回一个列表元组，建立相同项之间的映射关系
# 简化__init__中变量的重复定义


class Structure:
    """基类：定义了初始化的步骤，可以接受任意数量的初始化参数"""
    _fields = []  # 初始化一个名称列表(私有变量)

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expect {} arguments'.format(len(self._fields)))

        # set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)  # 设置属性


# 数据结构实例
if __name__ == '__main__':
    """主进程"""

    class Stock(Structure):
        """Stock:一个可爱的股票类"""
        # 参数的初始化过程就很简单了
        # 继承了超类的__init__方法
        # super(Stock, self).__init__()
        _fields = ['name', 'shares', 'price']
