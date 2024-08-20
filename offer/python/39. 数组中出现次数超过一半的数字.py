"""
题目： 数组中有一个数字出现的次数超过数组长度的一半, 请找出这个数字。

例如, 输入一个长度为9的数组 `{1, 2, 3, 2, 2, 2, 5, 4, 2}`。由于数字2在数组中出现了5次, 超过数组长度的一半, 因此输出2。
"""
from collections import Counter
def func(inp):
    cnt = Counter(inp)
    for k, v in cnt.items():
        if v > len(inp) // 2:
            return k

inp = [1, 2, 3, 2, 2, 2, 5, 4, 2]

print(func(inp))