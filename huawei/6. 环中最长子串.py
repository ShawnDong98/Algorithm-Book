"""
给你一个字符串 s, 字符串 s 首尾相连成一个环形, 请你在环中找出 o 字符出现了偶数次最长子字符串的长度。

示例1

输入
alolobo

输出
6

说明
最长子字符串之一是“alolob”, 它包含'o'2个

示例2

输入
looxdolx

输出
7

说明
最长子字符串是"oxdolxl", 由于是首尾连接在一起的, 所以最后一个'x'和开头的'l'是连接在一起的, 此字符串包含2个o。

示例3

输入
bcbcbc

输出
6
"""

inp = input()

n = len(inp)

s = inp * 2

res = 0

for start in range(n):
    for end in range(start+1, start+n):
        count_o = 0
        for s in inp[start:end]:
            if s == 'o':
                count_o += 1
            
        if count_o != 0 and count_o % 2 == 0:
            res = max(res, end - start)

print(res)





