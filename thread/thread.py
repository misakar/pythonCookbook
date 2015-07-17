# -*- coding: utf-8 -*-

import thread
import time


# 一个用于在线程中执行的函数
def func():
    for i in range(5):
        print 'func'
        time.sleep(1) # 线程进入其他阻塞状态

    # 结束当前线程
    thread.exit()


# 启动一个线程(线程立即开始运行)
thread.start_new(func, ()) # func 没有参数时，需要传递一个空元组


# 创建一个锁(LockType, 不能直接实例化)
lock = thread.allocate()


# 判断锁是锁定状态还是释放状态
print lock.locked()


# 锁被用来处理线程间资源的分配问题
count = 0 # 定义了一个资源变量
# 如果线程获得锁定则可以访问变量
if lock.acquire():
    count += 1
    # 释放锁(结束对资源的访问)
    lock.release() 

# thread 模块提供的线程都将在主线程结束后同时结束
time.sleep(6)
# 编程　＝　写作　＋　弹琴
