"""
给你一个字符串s, 字符串s首尾相连成一个环形, 请你在环中找出'l'、'o'、'x'字符都恰好出现了偶数次最长子字符串的长度。

输入描述
输入是一串小写的字母组成的字符串

输出描述
输出是一个整数

1 ≤ s.length ≤ 5 * 10^5

s只包含小写英文字母

输入
alolobo

输出
6

说明
最长子字符串之一是 "alolob", 它包含 'l'、'o' 各 2 个, 以及 0 个 'x'。

输入
looxdolx

输出
7

说明
最长的子字符串是 "oxdolxl", 由于是首尾连接在一起的, 所以最后一个 'x' 和开头的 'l' 是连接在一起的。此字符串包含 2 个 'l'、2 个 'o'、2 个 'x'。

输入
bcbcbc

输出
6

说明
这个示例中, 字符串 "bcbcbc" 本身就是最长的, 因为 'l'、'o'、'x' 都出现了 0 次。

下面用 Python 解这道题, 并给出解题思路和考察的知识点。
"""

inp = list(input())

double_inp = inp * 2

res = []
for start in range(len(inp)):
    for end in range(start+1, start+len(inp)):
        substr = double_inp[start:end+1]
        cnt_l = substr.count("l")
        cnt_o = substr.count("o")
        cnt_x = substr.count("x")
        if cnt_l % 2 == 0 and cnt_o % 2 == 0 and cnt_x % 2 == 0:
            res.append(len(substr))

print(max(res))