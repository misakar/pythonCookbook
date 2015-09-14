#!/usr/bin/env python
# encoding: utf-8

"""
    1.8.py
    ~~~~~~

        与字典有关的计算问题

        我们想在字典上对数据执行各种各样的计算(比如:求最大值、最小值、排序)
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


# 可以通过zip将字典的值和键反转
# zip(prices.values(), prices.keys())

# 求字典中值最小的项
min_price = min(zip(prices.values(), prices.keys()))

# 求字典中值最大的项
max_price = max(zip(prices.values(), prices.keys()))

# 依据值从小到大排序
sort_price = sorted(zip(prices.values(), prices.keys()))

# zip
# zip创建了一个迭代器，它的内容最多只能被消费一次
lit = zip(prices.values(), prices.keys())  # [(), ()]
