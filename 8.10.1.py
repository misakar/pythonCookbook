#!/usr/bin/env python
# encoding: utf-8
"""
    8.10.1.py
    ~~~~~~~~~

        使缓存变量的值不能改变
"""


def lazyproperty(func):
    name = '_lazy_' + func._name_

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)  # self.name = value
            return value
        return lazy
