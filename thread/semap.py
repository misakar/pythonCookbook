# -*- coding: utf-8 -*-

import threading
import time


# 计数器的初始值定为 2
semaphore = threading.Semaphore(2)


def func():

    # 请求 semaphore，成功后计数器会-1
    print "%s acquire semaphore..." % threading.currentThread().getName()
    if semaphore.acquire():
        print "%s get semaphore..." % threading.currentThread().getName()
        time.sleep(4)

        # 释放 semaphore 计数器+1
        print "%s release semaphore" % threading.currentThread().getName()
        semaphore.release()


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t4 = threading.Thread(target=func)


t1.start()
t2.start()
t3.start()
t4.start()
