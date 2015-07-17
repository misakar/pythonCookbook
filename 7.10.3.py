# -*- coding: utf-8 -*-

# coroutine 协程
# 回调函数
# 协程在生产者消费者模型中的应用
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print ('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'


def producer(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print ('[PROCEDURE] Procesing %s...' % n)
        r = c.send(n)
        print ('[PROCEDURE] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    producer(c)
