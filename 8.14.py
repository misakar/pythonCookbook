# coding: utf-8

"""
    8.14.py
    ~~~~~~~

        实现自定义容器
"""
# 自定义容器可以通过从 collections 模块继承，用以实现特定的方法


import collections
import bisect


class Sortedseq(collections.Sequence):
    """一个任意情况下保持排序的容器，继承了Sequence类
    还需实现 __getitem__, __len__　方法，才是一个真正
    的序列"""

    def __init__(self, initial=None):
        """实现初始排序"""
        self._items = sorted(initial) if initial is not None else []  # 实现一个新排序后的私有序列

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, value):
        """自定义排序添加项"""
        bisect.insort(self._items, value)  # 依据原先排序进行插入，不会影响排序结果
