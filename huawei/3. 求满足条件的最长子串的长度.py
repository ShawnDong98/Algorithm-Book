"""
给定一个字符串, 只包含字母和数字, 按要求找出字符串中的最长（连续）子串的长度, 字符串本身是其最长的子串, 子串要求：

1. 只包含1个字母(a~z, A~Z), 其余必须是数字；
2. 字母可以在子串中的任意位置；

如果找不到满足要求的子串, 如全是字母或全是数字, 则返回-1。

| 输入 | abC124ACb |
| --- | --- |
| 输出 | 4 |
| 说明 | 满足条件的最长子串是C124或者124A, 长度都是4 |

| 输入 | a5 |
| --- | --- |
| 输出 | 2 |
| 说明 | 字符串自身就是满足条件的子串, 长度为2 |

| 输入 | aBB9 |
| --- | --- |
| 输出 | 2 |
| 说明 | 满足条件的子串为B9, 长度为2 |

| 输入 | abcdef |
| --- | --- |
| 输出 | -1 |
| 说明 | 没有满足要求的子串, 返回-1 |
"""

inp = input()

max_length = 0

i = 0

while i < len(inp)-1:
    if inp[i].isalpha():
        i += 1
        length = 0
        while  i < len(inp) and inp[i].isdigit():
            length += 1
            i += 1
        if length > max_length:
            max_length = length

if max_length == 0:
    print(-1)
else:
    print(max_length+1)