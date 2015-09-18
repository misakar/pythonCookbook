operator 模块介绍
===
### operator 模块定义了内置的运算操作用于比较序列和字典

## 1. 逻辑操作

    from operator import *

    a = [1, 2, 3, 4]
    b = a

    print a             # [1, 2, 3, 4]
    print b             # [1, 2, 3, 4]
    print not_(a)       # False
    print truth(a)      # True
    print is_(a, b)     # True
    print is_not(a, b)  # False

## 2. 比较操作

    from operator import *

    a = 3;
    b = 5;

    print a, b

    for func in (lt, le, eq, ne, ge, gt):
        print "%s(a, b)" % func , func(a, b)

    # lt: same as a<b
    # le: same as a<=b
    # eq: same as a==b
    # ne: same as a!=b
    # ge: same as a>=b
    # gt: same as a>b

## 3. 运算操作

    正负数转化

    positive: pos(-1)  # -1
    negative: neg(-1)  # 1
    absolute: abs(-1)  # 1

what's more

    add(a, b), div(a, b)
    floordiv(a, b): same as a//b
    mod(a, b), sub(a, b)
    mul(a, b): same as a*b
    pow(a, b): same a的b次方
    truediv(a, b): 无论何时都按a/b计算(哪怕 __future__.division 模块导入)

## 4. 序列操作

## 5. in-place 操作

## 6. 获取属性或元素

## 参考
[python operator模块](http://cangmean.org/2015/07/10/operator/) <br/>
