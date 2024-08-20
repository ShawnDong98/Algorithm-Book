"""
题目： 字符串中第一个只出现一次的字符。在字符串中找出第一个只出现一次的字符。如输入 "abaccdeff"，则输出 b。
"""

from collections import Counter

def func(inp):
    cnt_inp = Counter(inp)

    for k, v in cnt_inp.items():
        if v == 1:
            return k
        
    




inp = "abaccdeff"
print(func(inp))