# -*- coding: utf-8 -*-

import threading


local = threading.local()
local.name = "main"


def func():
    local.name = "local"
    print local.name
    

t1 = threading.Thread(target=func)
t1.start()
t1.join()


print local.name

# 首先，启动线程会打印线程内部的变量, join阻塞线程后，则会打印全局的name变量
# local 小写字母类 保证了线程设置的属性不会被其他线程设置的属性替换
# 主线程 和 func线程
