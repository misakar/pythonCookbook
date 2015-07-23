# -*- coding: utf-8 -*-

"""threading模块提供的方法"""
# threading.currentThread(): 返回当前的线程变量
# threading.enumerate(): 返回一个包含启动后、结束前的线程列表
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate)的结果相同
"""threading模块提供的类"""
# Thread, Lock, Rlock, Condition, Event, Timer, Local


# Thread 线程类
import threading


# 1: 将要执行的方法作为参数传给Thread的构造方法
def func():
    print ('func() passed to Thread')


thr = threading.Thread(target=func)
thr.start()  # 函数线程


# 2: 从Thread类继承，并重写run()
class MyThread(threading.Thread): # 类继承
    def run(self):
        """重写 run 方法"""
        print ('MyThread extended from Thread')


thre = MyThread()
thre.start()  # 类线程


# Thread 类的构造方法:
# Thread(group=None, target=None, name=None, args=(), kwargs={})
# group: 线程组
# target: 要执行的函数（方法） oop一点的就是行为
# name: 线程名
# args/kwargs: 要传入的方法的参数


# Thread 类的实例方法
# isAlive(): 返回线程是否正在运行
# get/setName(name): 获取/设置线程名
# is/setDaemon(bool): 获取/设置是否守护线程
# start(): 启动线程
# join([timeout]): 阻塞当前上下文环境中运行的线程，直到调用此方法的线程终止或达到指定的timeout


# 使用join的例子(当前上下文环境)
# 见 join.py
