"""
    1.12.py
    ~~~~~~~

        找出序列中出现次数最多的元素

        使用collections模块的Counter类
"""

from collections import Counter


words = [
        'neo1218', 'yes', 'No', 'jack',
        'jack', 'No', 'neo1218', 'A',
        'A', 'A', 'O'
]


words_count = Counter(words)
# 打印出现最多的三个元素
print (words_count.most_common(3))
