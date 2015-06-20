#!/usr/bin/env python
# encoding: utf-8

"""
    1.2.py
    ~~~~~~
        从任意长的可迭代对象中分解元素
"""
"""
    分析:
        赋值分解法虽然简单,但是必须已知可迭代对象所含的元素个数,才能用对应的变量进行分解
        我们可以用python *表达式解决这个问题
        * 表达式可以存储多余到变量到列表中
"""
# 案例1:
grades = [1,23,34,56,78,90]
def drop_first_last(grades):
    """去掉最低分和最高分"""
    first, *middle, high = grades # middle是变量名
    print middle # middle = [23,34,56,78]
    print avg(middle)

# 案例2:
records = [
    ('jack',19),
    ('neo',20,'hust'),
    ('jack','highschool')
]
def about_jack(x):
    """关于jack的信息"""
    print ('jack:',x)

def about_neo(x,y):
    """关于neo的信息"""
    print ('neo:',y)

# 开始迭代
def getInfo():
    for tag, *info in records:
        if tag == 'jack':
            about_jack(*info)
        if tag == 'neo'
            about_neo(*info)

# 案例3:
# 丢弃值
# 如果我们只想获得我们需要到变量呢？
# 你只有给变量取一个用不到到名字比如: lalala,hahaha

# 案例4:
# 用*表达式实现递归(递归:自己调用自己,初始条件)
lit = [1,2,3,4,5]
def sumItem(lit):
    """求列表中所有元素的和"""
    head, *tail = lit
    return head + sumItem(*tail) if tail else head # 防止溢出

# main
# 案例1:
#drop_first_last(grades)
# 案例2:
getInfo()
# 案例3:
pass
# 案例4:
sumItem(lit)
