# -*- coding: utf-8 -*-
"""
    8.4.py
    ~~~~~~

        with 与类结合构造上下文管理器
"""
# 在实际编程中，经常需要使用上下文管理器用于处理不同上下文的代码执行。
# 上下文管理器的一个重要思想，就是将实际的代码执行语句与环境准备和环
# 境清理分开，确保上下文无论如何都会被触发
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        # 将列表作为栈，用于存储连接
        self.connections = []

    def __enter__(self):
        """with　语句触发，进行网络连接，并将sock赋给with语句对象"""
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        # 向栈中添加连接
        self.connections.append(sock)
        return sock

    def __exit__(self):
        """清理上下文环境，断开连接"""
        self.connections.pop().close()


# address must be a tuple, not be a str
cnn = LazyConnection(('www.python.org', 80))


# with 触发
with cnn as s1:
    # enter执行，并返回sock给s1
    s1.send(b'GET /psf-landing HTTP/1.0\r\n')
    s1.send(b'Host: www.python.org\r\n')
    s1.send(b'\r\n')
    resp = b''.join(iter(partial(s1.recv, 8192), b''))
    # exit执行，断开连接
    with cnn as s2:
        s1.send(b'GET / HTTP/1.0\r\n')
        s2.send(b'Host: www.python.org\r\n')
        s2.send(b'\r\n')
        resp = b''.join(iter(partial(s2.recv, 2000), b''))
