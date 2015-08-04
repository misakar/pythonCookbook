# coding: utf-8
# !/usr/bin/python

"""
    12.1.2.py
    ~~~~~~~~~

        更多对线程的操作
"""
from threading import Thread
import time


class CountdownTask:
    """对加载进线程的代码进行了封装，实现更多功能"""
    def __init__(self):
        self._running = True

    def terminate(self):
        """轮询线程的退出状态"""
        self._running = False

    def run(self, n):
        while  self._running and n > 0:
            print("T-minus", n)
            n -= 1
            time.sleep(2)


countdown = CountdownTask()
t = Thread(target=countdown.run, args=(5,))


t.start()
countdown.terminate()  # 设置线程关闭
t.join()  # 设置线程连接、等待线程结束``


# 对直接加载进线程的代码的初始操作是不多的（start, join）
# 更复杂的线程操作需要自定义
# 比如通过类的形式给线程函数添加代码
# 增加关闭操作之类
