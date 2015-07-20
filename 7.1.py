# -*- coding: utf-8 -*-

"""
    7.1.py
    ~~~~~~

        编写可接受任意数量参数的函数
"""
# 任意数量－意味着需要存储,元组、列表、字典
# signature；函数签名－储存函数参数信息（参数名，如果有注解的话还包括注解）
from inspect import signature


def test(*args, **kwargs):
    """
    *args: 接受任意数量的位置参数，存储到元组(元组是不可变的)
    **kwargs: 接受任意数量的关键字参数，存储到字典(关键字：映射关系)
    """
    sig = signature(test)
    # sig: *args, **kwargs
    print (sig)


# main
test(1, 2)
test(1, a=2)
