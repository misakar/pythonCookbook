# -*- coding: utf-8 -*-

import threading
import time


def context(t_join):
    print "In thread context !"
    t_join.start() # 开启线程

    t_join.join() # 阻塞context线程

    print "out thread context!" #


def join():
    print "In thread join !"
    time.sleep(1) # 其他阻塞
    print "out thread join!"


t_join = threading.Thread(target=join)
t_context = threading.Thread(target=context, args=(t_join,))


# 启动context线程
t_context.start()
