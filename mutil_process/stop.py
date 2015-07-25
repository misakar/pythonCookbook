# coding: utf-8

"""
    stop.py
    ~~~~~~~

        关闭进程
"""
import multiprocessing
import time


def worker(:print("start worker!")time.sleep(1)print("finish worker!")if __name__ == "__main__:p = multiprocessing.Process(target=worker)print("Before start: ", p.is_alive)p.start()print("Start: ", p.is_ali) p.terminate() print("Terminate: ", p.is_alive)

    p.join()
    print("Join after terminate: ", p.is_alive)
