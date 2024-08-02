"""
提取字符串中的最长合法简单数学表达式, 字符串长度最长的, 并计算表达式的值。

如果没有, 则返回0。

简单数学表达式只能包含以下内容 

- 0-9数字
- 符号 +-*

说明 

1 所有数字计算结果都不超过long 

2 如果有多个长度一样的请返回第一个表达式的结果 

3 数学表达式必须是最长的合法的 

4 操作符不能连续出现如 +--+1 是不合法的

输入

字符串

输出描述

表达式值

示例

输入

1 - 2abcd

输出

-1
"""

def func(inp):
    i = 0
    res = []
    eq = []
    while i < len(inp):
        num = []
        if inp[i].isdigit():
            while i < len(inp) and inp[i].isdigit():
                eq.append(inp[i])
                i += 1
            eq.append("".join(num))
        elif inp[i] in "+-*":
            if inp[i] in "+-*" and not inp[i+1].isdigit():
                res.append(eq)
                eq = []
            else:
                eq.append(inp[i])
            i += 1
        else:
            res.append(eq)
            eq = []
            i += 1

    return res
                
            
inp = input().replace(" ", "")

res = func(inp)
res = sorted(res, key=lambda x: -len(x))

print(eval("".join(res[0])))