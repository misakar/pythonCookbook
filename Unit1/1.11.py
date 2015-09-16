#!/usr/bin/env python
# encoding: utf-8

"""
    1.11.py
    ~~~~~~~

        对切片进行命名
"""

# 将特定的切片进行命名可以更好的管理代码
record = "......jack......19"
name = record[6:10]
age = int(record[-1:-3])


print "his name is %s, his age is %d" % (name, age)
# 这样显然比下面的代码要易于理解
# print "his name is %s, his age is %d" % (record[6:10], int(record[-1:-3]))


# 此外，python内置了slice类方便我们进行切片管理
"""
>> s = slice(2, 4)  # [2:4]
>> s.start
2
>> s.stop
4
"""

# 还可以使用slice对象的indices方法，将切片映射到特定
# 大小的序列上,返回信息元组
"""
>> a = "hello python"
>> s.indices(len(a))
(2,4,1)
"""
