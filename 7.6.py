# -*- coding: utf-8 -*-

"""
    7.6.py
    ~~~~~~

        定义匿名和内联函数
        lambda 单语句函数，他可以定义一个单独的函数
        也可以作为内联函数嵌入到复杂的语句中
"""
# 对于只有一行的胶水式的函数，没必要专门写一个def语句
# 于是，lambda函数诞生啦！
sx = lambda x: [x*x for x in range(2)] # lambda 与列表推导结合

add = lambda x, y: x + y


# lambda 更多的是应用于上下文环境中
names = [
    'Neo Haha',
    'Lily Tom',
    'Jack Atom'
]
# sorted(iterable, cmp=None, key=None, reverse=False)->new sorted iterable
new_names = sorted(names, key = lambda name: name.split()[-1].lower()) # spilt()默认是' '
print (names)
print (new_names)
