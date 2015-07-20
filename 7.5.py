# -*- coding: utf-8 -*-

"""
    7.5.py
    ~~~~~~

        定义带有默认参数的函数
        变量定义：　_xxx : 不能从 from module import * 导入        私有变量
                　 __xxx__: 系统定义变量，一般是python的内建变量    转换变量
                  __xxx: 类中的私有变量名              __xxx__: Class_xxx
        默认参数：默认参数可以执行检查，防止变量的值被改变！
"""
# 1. 注意使用None作为默认参数的值！！并进行条件判断！
def spam(a, b=None):
    """使用None作为默认参数的值，避免ｂ被改变"""
    if b is None:
        # python似乎总喜欢将异常放在第一位
        # 其实这是一种手段：异常优先处理就像是进行了一次检查
        # 还可以保证代码的精简
        b = []
    print (b)
    return b


# 但是None也是一个用户可以提供的值，如果希望在函数中检测默认参数的任意值
# 采用　object() 创建独特的私有实例(对象)
_no_value = object()
def spam2(a, b=_no_value):
    """注意默认参数的检测！！"""
    if b is _no_value:
        print ("没有给ｂ提供值!")
    else:
        print (b)

# main
x = spam(1)   # x = [] 相当于把ｂ赋给了ｘ
x.append(2)
x.append('neo1218')
print (x)
# 注意默认参数的威力
# 你没有指明参数的时候会采用默认值
spam(2)

spam2(1)
# 这里没有使用默认参数
spam2(1, b=[])
