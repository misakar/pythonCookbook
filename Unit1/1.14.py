# coding: utf-8

"""
    1.14.py
    ~~~~~~~

        对不原生支持比较操作的对象排序

        比如我们想对某个类的实例排序
"""

# 内置的sorted函数可以通过key参数传递可调用对象
# 可调用对象会返回待排序对象中的某些值
# sorted函数则利用这些值来比较对象


class User(object):
    """用户类"""
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User %r' % self.user_id


# 使用
"""
>> users = [User(3), User(2), User(24)]
>> users
[User 3, User 2, User 24]
>> sorted(users, key = lambda u: u.user_id)
[User 1, User 2, User 24]
"""


# key参数可以使用lambda匿名函数，该函数会返回我们希望排序的依据即:user的user_id属性
# 从而对对象进行排序


# 我们还可以使用operator函数的attrgetter方法，用于获取排序依据
# 使用
"""
>> users = [User(3), User(2), User(24)]
>> users
[User 3, User 2, User 24]
>> sorted(users, key = attrgetter('user_id') )
[User 2, User 3, User 24]
"""
