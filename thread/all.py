# -*- coding: utf-8 -*-

"""
    all.py
    ~~~~~~

        线程的综合应用
"""
import threading


alist = None # 创建了一个空列表 一个资源
condition = threading.Condition() # 创建了一个条件变量, 用于通知


def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in range(len(alist))[::-1]:
            alist[i] = 1
        condition.release()


def doPrint():
    if condition.acquire():
        while alist is None:
            condition.wait
        for i in alist:
            print i
        print
        condition.release()


def doCreate():
    global alist # 又声明了一个与主线程同名的全局alist
    if condition.acquire():
        if alist is None:
            alist = [0 for i in range(10)]
            condition.notifyAll() # 通知所有线程
        condition.release()


tset = threading.Thread(target=doSet, name='tset')
tprint = threading.Thread(target=doPrint, name='tprint')
tcreate = threading.Thread(target=doCreate, name='tcreate')


tset.start()
tprint.start()
tcreate.start()
