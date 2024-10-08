"""
均衡串定义：字符串只包含两种字符，且两种字符的个数相同。
给定一个均衡字符串，请给出可分割成新的均衡子串的最大个数。
约定字符串中只包含大写的'X'和'Y'两种字符。

输入描述
均衡串:XXYYXY

字符串的长度[2,10000]。给定的字符用均为均衡串。

输出描述
可分割为两个子串:

XXYY

XY

示例1
输入
XXYYXY

输出
2

备注
分割后的子串，是原字符串的连续子串。
"""

def func(inp):
    count_X = 0
    count_Y = 0
    count_balance = 0

    for s in inp:
        if s == "X":
            count_X += 1
        elif s == "Y":
            count_Y += 1
        
        if count_X == count_Y:
            count_balance += 1

    return count_balance


inp = input()
print(func(inp))
