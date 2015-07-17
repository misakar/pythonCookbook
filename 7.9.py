# -*- coding: utf-8 -*-

"""
    7.9.py
    ~~~~~~

        用函数替代只有单个方法的类
"""
# 采用单个方法的类是因为我们希望可以通过类保存环境属性，
# 而这可以通过闭包函数达到同样的效果，而且闭包函数更显
# 得优雅！
from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        """可以通过类的__init__方法保存template"""
        self.template = template
    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


def urltemplate(template):
    """这是一个闭包，利用函数参数保存template"""
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener
# 闭包的核心特性就是它可以记住定义闭包时的环境
