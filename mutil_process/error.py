# coding: utf-8

"""
    error.py
    ~~~~~~~~

        关于进程退出的状态码p.exitcode
        == 0:正常退出
        > 0 :进程出现错误，并以该错误码退出
        < 0 :进程由状态码的相反数退出
"""
import multiprocessing
import time
import sys


def exit_error():
    """退出错误  1"""
    sys.exit(1)


def exit_ok():
    """退出成功  0"""
    return


def return_value():
    """返回值    0"""
    return 1


def raises():
    """引发RuntimeError   1"""
    raise RuntimeError('There is an error!')


def terminated():
    """引发阻塞      -15"""
    time.sleep(3)


if __name__ == "__main__":
    jobs = []  # jobs列表存储进程
    for func in [exit_error, exit_ok, return_value, raises, terminated]:
        print("staring: ", func.__name__)
        job = multiprocessing.Process(name=func.__name__, target=func)  # func.func_name　只支持python2
        jobs.append(job)
        job.start()

    jobs[-1].terminate()  # 对terminated进程调用terminate函数

    for job in jobs:
        job.join()  # 阻塞进程
        print("4{}.exitcode = {}".format(job.name, job.exitcode))
