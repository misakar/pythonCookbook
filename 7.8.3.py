# -*- coding: utf-8 -*-

"""
    7.8.3.py
    ~~~~~~~~

        给一个函数添加日志输出
"""
def output_result(result, log=None):
    """添加debug"""
    if log is not None:
        log.debug('Got %r', result)


def add(x, y):
    return x + y


if __name__ == '__neo1218__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    # apply_async是一个回调函数
    # partial成功解决了参数的兼容性问题
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()


# 关于multiprocessing模块的使用
# multiprocessing模块可以实现并行编程，从而更好的利用多核CPU(python受GIL限制)
# Pool是multiprocessing模块的进程池

""" 简单任务的多进程编程 """
import multiprocessing as mul
import timeit
import os
from math import factorial


pool = mul.Pool() # 实例化一个进程池，参数是进程的个数，默认是cpu_count
mul.cpu_count()


# test
def get_factorial(num, pid=0):
    if pid: # if process setted
        print('pid is', os.getpid()) # getpid: pid return current process id
    return factorial(num)


# 查看当前进程的PID
def list_result(num, pid=0):
    """将阶乘结果返回在列表中，并显示pid值"""
    result = []
    result = [get_factorial(n, pid=pid) for n in range(1, num+1)] # 列表推导
    return result


def list_result_async(num, pid=0, pool=None):
    """多进程模式：开启进程池"""
    pool = mul.Pool() # 在函数中实例化进程池,不能在主进程中实例化
    results_list = []
    results = []
    results_list = [pool.apply_async(get_factorial, (n, pid)) for n in range(1, num+1)]
    # 关闭进程
    pool.close()
    # 阻塞进程
    pool.join()
    for result in results_list:
        results.append(result.get()) # 这里需要通过get()方法获取result, 因为这里的result是AsyncResult
    return results


# 多进程执行
# 使用apply函数，则会在不同的进程中       顺序执行
# 使用apply_async函数，则会在不同进程中　 异步执行
list_result_async(10, pid=1) # 多个pid值执行


# pid=0, 当前进程未开启
# list_result(10, pid=0)
# list_result(10, pid=1) # pid的值全部相同
# 注意,list_result 函数调用　get_factorial　函数是串行计算，但pid相同可见是在一个进程
# 中顺序计算的！


# get_factorial(100, pid=0)
# get_factorial(100, pid=1)


""" 复杂任务的多进程编程 """
