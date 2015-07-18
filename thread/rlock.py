# -*- coding: utf-8 -*-

import threading
import time


rlock = threading.RLock()


def func(): # func 就是一个线程
    # first acquire
    print "%s acquire lock..." % threading.currentThread().getName()
    if rlock.acquire():
        print "%s get the lock!" % threading.currentThread().getName()
        time.sleep(2)

        print "%s acquire lock again..." % threading.currentThread().getName()
        if rlock.acquire():
            print "%s get the lock!" % threading.currentThread().getName()
            time.sleep(2)
            
        print "%s release lock!" % threading.currentThread().getName()
        rlock.release()
        time.sleep(2)

        print "%s release lock!" % threading.currentThread().getName()
        rlock.release()


# 利用 func 创造线程
t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)


t1.start()
t2.start()
t3.start()
