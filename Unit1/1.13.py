"""
    1.13.py
    ~~~~~~~

        通过公共键对字典列表进行排序

        字典列表: [{},{},{}]

        我们有一个字典列表，想根据一个或多个字典中的值来对列表排序
"""

# operator模块的itemgetter函数的使用


rows = [
        {'fname': 'neo1218', 'lname':'jack', 'age':19},
        {'fname': 'neo', 'lname':'python', 'age':19},
        {'fname': 'haha', 'lname':'python', 'age':19}
]


from operator import itemgetter


# sorted by fname
rows_sorted_by_fname = sorted(rows, key=itemgetter('fname'))
# this is equal to
rows_sorted_by_fname = sorted(rows, key=lambda r: r['fname'])


# itemgetter 函数可以作为key函数插入到 sorted 以及 max 和 min 函数中
