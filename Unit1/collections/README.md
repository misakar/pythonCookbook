python collections 模块 总结
===
官方文档的介绍:  High-performance container datatypes¶<br/>
collections 模块提供了很多高效的数据类型。<br/>


## 内置数据类型

### namedtuple - 命名元组
nametuple() 函数：用来产生可以利用名字访问元素的元组，通常可以增强代码的可读性<br/>
示例:

    # coding: utf-8
    from collections import namedtuple


    blogs = [
        ('neo1218', 'neo1218@github.io', 19),
        ('z-index', 'z-index@github.io', 20),
    ]

    Blog = namedtuple('Blog', ['name', 'site', 'age'])


    for blog in blogs:
        blog = Blog._make(blog)
        print blog


### deque - 双端队列
deque(maxlen) 函数：用于生成一个双端队列,可以指定长度 maxlen<br/>
deque的基本用法可以参见Unit1的README，这里重点介绍 rotate 函数:<br/>

    deque.rotate(n): 把deque向右翻转n次，如果n为负数,则向左翻转

### Counter - 计数器
计数器的用处是很大的:)<br/>
示例:

    from collections import Counter

    s = '''qwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsa'''

    c = Counter(s)  # 实例化一个Counter对象

    print c.most_common(5)  # 打印出现次数最多的5个字符

### OrderedDict - 有序字典
python的字典默认是无序的<br/>
示例:

    from collections import OrderedDict

    items = (
        ('a', 1),
        ('b', 2),
        ('c', 3)
    )

    dict = OrderedDict(items)

### defaultdict
访问dict[key], 当key不存在时，默认字典就会报错。但是使用defaultdict，只需传入一个工厂函数，当键
不存在时，就可以依靠工厂函数生成默认键值<br/>
示例:

    from collections import defaultdict

    students = [
        # age, name
        [19, 'neo1218']
        [19, 'neo']
        [20, 'jack']
    ]

    dict = defaultdict(list)  # defaultdict(<type 'list'>, {})
    for age, name in students:
        # age 键不存在，但不会报错
        dict[age].append(name)

