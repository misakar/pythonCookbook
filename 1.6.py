#!/usr/bin/env python
# encoding: utf-8
"""
    1.6.py
    ~~~~~~

       在字典中将键映射到多个值上
       我们现在想要一个能将键映射到多个值的字典
"""
"""
    分析：
        python collections模块
        借助collections模块中的字典方法--defaultdict
            defaultdict会自动初始化字典的第一个值
"""
pairs = []
# 如果不使用 defaultdict 方法
d = {}
for key , value in pairs:
    if key not in d:
        d[key] = [] # 程序员自己初始化
    d[key].append(value)

# 使用 defaultdict 会方便许多
from collections import defaultdict
d = defaultdict(list)
for key , value in pairs:
    d[key].append(value)


# 核心思想： 将字典的值用列表或集合表示，达到存放多个值的效果
#            但要注意字典第一个值的初始化.
