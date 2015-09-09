#!/usr/bin/env python
# encoding: utf-8
"""
    1.6.py
    ~~~~~~

       在字典中将键映射到多个值上
       我们现在想要一个能将键映射到多个值的字典

       分析：
            python collections模块
            借助collections模块中的字典类--defaultdict
            defaultdict会自动初始化字典的第一个值
"""

from collections import defaultdict


pairs = []

# 如果不使用 defaultdict 类
d = {}

for key , value in pairs:
    if key not in d:
        d[key] = []  # 程序员自己初始化
    d[key].append(value)


# 使用 defaultdict 类 会方便许多
d = defaultdict(list)  # defaultdict(<type 'list'>, {})

for key , value in pairs:
    d[key].append(value)
