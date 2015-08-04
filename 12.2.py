# coding: utf-8
# !/usr/bin/python

"""
    12.2.py
    ~~~~~~~

        判断线程是否已经启动
"""
# 判断线程是否已经启动可以使用 Event(事件) 同步线程
from threading import Thread, Event
import time


def countdown(n, start_env):
    """start_env 利用事件同步线程"""
    print("countdown starting!")
    start_env.set()  # 设置事件 获取线程的运行状态
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(2)


start_env = Event()


print('Launching Thread-countdown')
t = Thread(target=countdown, args=(10, start_env))
t.start()


start_env.wait()  # 等待线程开始设置事件
print("countdown Running..............")
t.join()


# 初始参数传递并不是运行线程!
# 有意思但是不知道是为什么。。
