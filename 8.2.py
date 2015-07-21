# coding: utf-8
"""
    8.2.py
    ~~~~~~

        自定义类的字符串的输出格式
"""
# 定义一个控制字符串输出格式，可以被类使用的私有变量
_formats = {
    # 格式化字符串，用于类的格式化输出
    'ymd': '{0.year}-{0.month}-{0.day}',
    'myd': '{0.month}/{0.year}/{0.day}',
    'dym': '{0.day}/{0.year}/{0.month}'
}


class Date:
    """自定义输出日期类"""
    def __init__(self, day, year, month):
        self.day = day
        self.year = year
        self.month = month

    def __format__(self, form):
        """__format__，类方法，
        解释器会解释为 Date_format，
        调用时 format(args)"""
        if form == '':
            form = 'ymd'
        fmt = _formats[form]
        return fmt.format(self)


# Use this class
date = Date(19, 2015, 7)
print(format(date, ''))
print(format(date, 'myd'))
print(format(date, 'dym'))
