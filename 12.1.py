# coding: utf-8
# !/usr/bin/python

"""
    12.1.py
    ~~~~~~~

        启动和停止线程
"""
# 在独立线程中执行的代码
import time


def countdown(n):
    while n>0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)  # 线程进入阻塞状态


# 创造一个线程并加载进代码
from threading import Thread
t = Thread(target=countdown, args=(10,))  # args 是一个元组
t.start()  # 只有调用 start 方法后，才会执行线程; start 方法则是由系统级（posix）
           # 线程调用
t.join()

if t.is_alive():
    print("Stilling Running!")
else:
    print("I am Finish!")
