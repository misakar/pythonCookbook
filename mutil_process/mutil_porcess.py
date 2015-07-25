#!/usr/bin/env python
# encoding: utf-8
"""
    mutil_process.py
    ~~~~~~~~~~~~~~~~

        python中的多进程
        进程：一个运行的独立程序
        mutilprocess 模块的核心在于，像线程一样管理进程
"""
# 简单的管理进程


import multiprocessing


def worker(num):
    """thread worker function"""
    print("worker: ", num)


if __name__ == "__main__":
    """主进程"""
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(5)
        p.start()
