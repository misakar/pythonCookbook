#!/usr/bin/env python
# encoding: utf-8

"""
    1.3.py
    ~~~~~~

        保存最后N个元素

        # 案例1:
        查找一系列文本行, 如果存在匹配, 输出当前文本行以及最后查找的N行文本
"""

# 案例：保存有限个历史纪录，使用 python collections 模块


from collections import deque


def search(lines, pattern, history=5):
    """文本查找函数, 函数返回一个生成器对象"""
    previous_lines = deque(maxlen=history)  # 双端队列, 用于保存历史纪录
    for line in lines:
        if pattern in line:
            # 利用生成器
            yield line, previous_lines  # (line, previous_line)
        previous_lines.append(line)


# 应用
if __name__ == "__main__":
    with open('1.3.txt') as f:
        # 生成器是可迭代的，也是可分解的
        for line, previous in search(f, 'python', 5):
            for pline in previous:
                print(pline)
            print(line)
            print('-'*20)
