#!/usr/bin/env python
# encoding: utf-8

"""
    1.3.py
    ~~~~~~
        保存最后N个元素
"""
# 案例1:
"""
查找一系列文本行,如果存在匹配,输出当前文本行以及最后查找的N行文本
"""
"""
python  collections  ------|
                           |
      Learing !!          \ /
                           +
"""
# 1.namedtuple
from collections import namedtuple
websites = [
    ('google', 'http://www.google.com/', u'LarryPage'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]
Website = namedtuple('Website', ['name', 'url', 'founder']) # Website is a namedtuple Class, and website like self
for website in websites:
    website = Website._make(website)
    print website
    print website[0], website.url

# 2.deque
# what is deque: double-ended queue
# An instresting example about deque
import sys
import time
from collections import deque
fancy_loding = deque(">"*20 + "-"*130)
while True:
    print "\r%s" % ''.join(fancy_loding)
    fancy_loding.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)
# so instresting !!!!

# 3.Counter
str = "This is a novel,sorry maybe this is a some thing instresting! ha ha ha , that's so fun ha "
from collections import Counter
c = Counter(str)
print c.most_common(2)

# OrderedDict
# dict is hash but OrderedDict ?
from collections import OrderedDict
items = [
    ('neo1218', '18'),
    ('jack', '19'),
    ('lily', '18')
]
# dict
regular_dict = dict(items)
print regular_dict
# OrderDict
order_dict = OrderedDict(items)
print order_dict

"""
examples
"""
# example1:
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in previous_lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# example1 use on file
if __name__ == "__main__":
    with open("1.3.txt") as f:
        for line, prevlines in search(f, "python", 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')


