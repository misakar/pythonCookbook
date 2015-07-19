# -*- coding: utf-8 -*-
"""
    7.11.py
    ~~~~~~~

        内联回调函数
        任何一段框架都应该有一个控制流，也就是主线程，但是过多的函数或许会导致
        控制流的丢失。
        当回调函数过多时也会如此
        因此可以通过生成器和协程将回调函数内联到一个函数中。
"""
# 一个普通的回调函数 aysnc 异步
def apply_aysnc(func, args, *, callback):
    result = func(*args)
    callback(result)


"""
        --------------------------------------
        |                                    |
        |         /                \         |
        |                                    |
        |                                    |
        |                                    |
        |                口                  |
        |                                    |
        |                                    |
        |     暂时看不懂～～～　先看后面的吧!    |
        |____________________________________|
"""