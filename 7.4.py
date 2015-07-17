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
