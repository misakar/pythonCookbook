# -*- coding: utf-8 -*-
# 使用条件变量 -- 生产消费者模型

import threading
import time


# 商品
product = None
# 条件变量
con = threading.Condition()


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
