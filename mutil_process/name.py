#!/usr/bin/env python
# encoding: utf-8

"""
    name.py
    ~~~~~~~

        对进程命名，方便管理
"""
import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    print(name, 'start')
    time.sleep(2)
    print(name, 'stop')


def linux():
    name = multiprocessing.current_process().name
    print(name, 'start')
    time.sleep(3)
    print(name, 'stop')


if __name__ == "__main__":
    worker1 = multiprocessing.Process(name='worker1', target=worker)
    worker2 = multiprocessing.Process(target=worker)
    ubuntu = multiprocessing.Process(name='ubuntu', target=linux)

    worker1.start()
    worker2.start()
    ubuntu.start()
