# -*- coding: utf-8 -*-

import threading
import time


data = 0
lock = threading.Lock()


def func():
    global data # 全局变量，所有线程可以共享的资源, 只有锁定线程可以访问
    print ('%s acquire lock...' % threading.currentThread().getName())

    if lock.acquire():
        print '%s get the lock.' % threading.currentThread().getName()
        data += 1 # global
        time.sleep(2) # 其他阻塞线程
        print '%s release lock...' % threading.currentThread().getName()

        lock.release()


# 绑定线程
t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)



# 开启线程 
t1.start()
t2.start()
t3.start()
