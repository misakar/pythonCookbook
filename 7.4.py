# -*- coding: utf-8 -*-

"""
    7.4.py
    ~~~~~~

            从函数中返回多个值
"""
def haha():
    return 1, 2, 3


def ahaha(*args):
    return args


# main
a, b, c = haha()
print (a,b,c)

print(ahaha(1,2,3,4,5))


# 只需要通过return返回一个元组即可返回多个值
# 还有一种魔法方法：生成器
def haha2():
    return (x+1 for x in range(3))
