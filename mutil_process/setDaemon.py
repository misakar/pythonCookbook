# coding: utf-8

"""
    setDaemon.py
    ~~~~~~~~~~~~

        守护进程
        multiprocessing.setDaemon(True)，设置守护进程，会使进程一直运行
        不受time,join等阻塞影响。
"""
import multiprocessing
import time


def daemon():
    """设置守护进程"""
    name = multiprocessing.current_process().name
    print(name, 'start!')
    time.sleep(2)
    print(name, 'stop!')


def non_daemon():
    """不设置守护进程"""
    name = multiprocessing.current_process().name
    print(name, 'start!')
    time.sleep(1)
    print(name, 'stop!')


if __name__ == '__main__':
    d = multiprocessing.Process(name='deamon', target=daemon)
    n = multiprocessing.Process(name='non_deamon', target=non_daemon)

    d.daemon = True  # 开启守护进程模式
    n.daemon = False  # 关闭守护进程模式

    d.start()
    n.start()

    d.join(1)
    print('d.is_alive(): ', d.is_alive)
    n.join()
    print('n.is_alive(): ', n.is_alive)
