# -*- coding: utf-8 -*-
"""
    ８.4.py
    ~~~~~~~

        类的命名规则
"""
# １，_value: 表示类中的私用变量，不建议外部访问
# ２.__value: 表示类中的特殊变量，会进行名称整合
# class A:
#    def __init__(self):
#          self._inter = 0  # 自动整合为：A_init, A_inter
# 这样在继承时就不会出现名称混乱
# 3. value_: 区别保留字，避免冲突
