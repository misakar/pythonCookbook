#!/usr/bin/env python
# encoding: utf-8

"""
    1.10.py
    ~~~~~~~

        从序列中移除重复项且保持元素间的顺序不变

"""

# 1. 序列中的对象是可哈希的
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# 2. 序列中的对象是不可哈希的
def dedupe_2(items, key=None):
    """key是一个控制函数"""
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# 使用dedupe_2
"""
>> a = [{'x':1, 'y':2}, {'x':1, 'y':2}, {'x':4, 'y':4}]
>> list(dedupe_2(a, key=lambda d: (d['x'], d['y'])))

[{'x':1, 'y':2}, {'x':4, 'y':4}]
"""
