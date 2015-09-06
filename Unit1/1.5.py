#!/usr/bin/env python
# encoding: utf-8
"""
    1.5 实现优先级队列

        我们想实现一个队列，它会按给定的优先级来对元素排序，且每次 pop 操作时都返回优先级最高的那个元素
"""
"""
    解决方案
        继续求助于 heapq 模块
            heapq 模块函数： -------
                                < | >
                heappush(heap, item) # 将item添加到heap中（heap是一个列表）
                heappop(heap) # 将堆顶元素弹出（返回的就是堆顶）
                heappushpop(heap, item) # 先将item添加到heap中再弹出heap的堆顶元素
                                        # 这比两次用heappush 和 heappop函数快的多
                heapreplace(heap,item) # 先pop再把item添加到heap中， 比用两次函数快的多
                heapify(x) # 对列表x进行堆排序，默认是小顶堆
                merge(*iterables) # 将多个列表进行合并，然后进行堆调整，返回的是列表的可迭代对象。
                nlargest # 1.4中用过，返回最大的n个元素
                nsmallest # 1.4中用过，返回最小的n个元素
"""
# 利用heap模块实现一个简单的优先级队列类
import heapq


class PriorityQueue:
    """优先级队列类"""

    def __init__(self):
        """初始化，属性"""
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """"""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item():
    """插入元素"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

# main
q = PriorityQueue()  # 实例化对象

q.push(Item('neo'), 1)  # 传值过程中实例化对象
q.push(Item('jack'), 2)
q.push(Item('sister'), 4)
q.push(Item('me'), 4)

print q.pop()
