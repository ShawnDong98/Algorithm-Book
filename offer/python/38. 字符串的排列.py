"""
题目：输入一个字符串, 打印出该字符串中字符的所有排列。

例如, 输入字符串 abc, 则打印出由字符 a、b、c 所能排列出来的所有字符串 abc、acb、bac、bca、cab 和 cba。
"""
from itertools import permutations

inp = input()

for inp_ in permutations(inp):
    print("".join(inp_))

