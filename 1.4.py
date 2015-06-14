# -*- coding:utf-8 -*-
# !/usr/bin/python

"""
    1.4.py
    ~~~~~~
        在一个集合中查找最大最小到N个元素
"""
"""
    heapq 模块
        heapq模块中有两个函数可以帮助我们完成这个任务
        nlargest && nsmallest
"""
import heapq

nums = [1, 45, 2, 67, 8, 9]
print (heapq.nlargest(2, nums))
print (heapq.nsmallest(2, nums))

# 这两个函数都可以接受一个参数key
portfolio=[
    {'name': 'IBM', 'share': 100, 'price': 90},
    {'name': 'Apple', 'share': 100, 'price': 80},
    {'name': 'Google', 'share': 100, 'price': 70}
]
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print expensive
print cheap
"""
补充: 堆数据结构的python实现
    详见:<a href="http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/"></a>
"""
