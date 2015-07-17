# -*- coding: utf-8 -*-

"""
    7.7.py
    ~~~~~~

        在匿名函数中绑定变量的值
"""
# 注意lambda函数中的变量在函数调用时才开始绑定，定义时的
# 变量值没有实际意义！
# 可以采用默认参数的形式在lambda函数定义是绑定自由变量
funcs = [lambda x, n: x + n for n in range(5)]
for func in funcs:
    print (func(0))
# 4 4 4 4 4


funcs2 = [lambda x, n = n: x + n for n in range(5)]
for func in funcs2:
    print (func(0))
# 0 1 2 3 4
