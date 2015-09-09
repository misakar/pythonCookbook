# -*- coding: utf-8 -*-
# !/usr/bin/python
"""
    1.7.py
    ~~~~~~

        让字典保持有序
        当我们进行迭代时，如何构造一个有序的映射对象呢？
        分析：
        可以使用 collections 模块的 OrderedDict 类
"""

from collections import OrderedDict


dict = {}  # 普通字典

order_dict = OrderedDict(dict)  # 有序字典

# 有序字典会严格依据初始化的顺序对字典进行排序.
order_dict['a'] = "A"
order_dict['b'] = "B"
order_dict['c'] = "C"

# 输出--见证奇迹的时刻！
for key in order_dict:
    print (key, order_dict[key])

# 利用：
# 当我们想严格控制 JSON 数据时，OrderedDict 就是一个很好的选择
import json
print json.dumps(order_dict)
