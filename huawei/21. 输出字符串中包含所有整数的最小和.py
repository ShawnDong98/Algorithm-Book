"""
输入字符串s, 输出s中包含所有整数的最小和

说明

1. 字符串s, 只包含 a-z A-Z +-
2. 合法的整数包括
1) 正整数 一个或者多个0-9组成, 如 0 2 3 002 102
2) 负整数 负号 - 开头, 数字部分由一个或者多个0-9组成, 如 -0 -012 -23 -00023

输入描述: 

包含数字的字符串

输出描述: 

所有整数的最小和

示例

1.输入: 
bb1234aa

输出: 
10

2.输入: 
bb12-34aa

输出: 
-31

说明: 
1+2-(34)=-31
"""

inp = input()
res = []
i = 0
while i < len(inp) - 1:
    if inp[i] == "-":
        i += 1
        if i >= len(inp) or not inp[i].isdigit():
            continue
        temp = ["-"]
        while i < len(inp) - 1 and inp[i].isdigit():
            temp.append(inp[i])
            i += 1
        res.append("".join(temp))
    elif inp[i].isdigit():
        res.append(inp[i])
        i += 1
    else:
        i += 1

print(eval("+".join(res)))