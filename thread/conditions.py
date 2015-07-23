# -*- coding: utf-8 -*-
# 使用条件变量 -- 生产消费者模型

import threading
import time


# 商品
product = None
# 条件变量
con = threading.Condition()


# con条件变量在通知者和消费者之间双向传递
# con.acquire(): 调用关联锁的acquire方法，使线程进入同步锁定，尝试获取锁定。
# con.notify(): 从等待池中挑选一个线程进入锁定池，该锁定会自动获取acquire方法。
# con.wait(): 使线程进入条件变量包含的等待池等待通知，并释放锁。使用前线程必须已经锁定。


# 生产者方法
def producer():
    global product

    if con.acquire():
        while True:
            if product is None:
                print "produce..."
                product = 'lolcat!'

                # 通知消费者 lolcat 已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


# 消费者方法
def consumer():
    global product
    if con.acquire():
        while True:
            if product is not None:
                print 'consume...'
                product = None

                # 通知消费者，商品已经卖完了
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


# 创建线程
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)


# 启动线程
t1.start()
t2.start()
