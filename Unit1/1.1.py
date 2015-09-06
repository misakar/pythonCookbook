#!/usr/bin/env python
# encoding: utf-8
"""
    1.1.py
    ~~~~~~
        将序列分解为单独的变量
        现在,我们有一个包含N个元素的元组或序列,现在想将他分解为N个单独的变量

    分析:
        1.列表、元组、字符串都是序列
        2.序列是可索引和可切片的
        3.序列是可访问的
"""
# 解决方案(以列表为例)
# 样例列表
lit1 = [1, 2, 3, 4]
data = ['neo1218', 'neo1218@github.io', 19]


def solve1_1(lit):
    """任何可迭代到python对象,都可以通过赋值操作分解为单独的变量"""
    a, b, c, d = lit
    print a
    print b
    print c
    print d


def solve_2(data):
    """语义化"""
    name, blog, age = data
    print "name: %s" % name
    print "blog: %s" % blog
    print "age: %d" % age

# main 主程序
solve1_1(lit1)
solve_2(data)

"""其实不仅仅是序列,任何可迭代的对象都可以赋值分解"""
