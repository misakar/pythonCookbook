# -*- coding: utf-8 -*-

"""
    7.6.py
    ~~~~~~

        定义匿名和内联函数
"""
# 对于只有一行的胶水式的函数，没必要专门写一个def语句
# 于是，lambda函数诞生啦！

add = lambda x, y: x + y


# lambda 更多的是应用于上下文环境中
names = [
    'Neo Haha',
    'Lily Tom',
    'Jack Atom'
]
new_names = sorted(names, key = lambda name: name.split()[-1].lower())
print (names)
print (new_names)
