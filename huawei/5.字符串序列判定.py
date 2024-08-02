"""
输入两个字符串S和L, 都只包含英文小写字母。S长度<=100, L长度<=500000。判定S是否是L的有效字串。

判定规则: S中的每个字符在L中都能找到(可以不连续), 且S在L中字符的前后顺序与S中顺序要保持一致。例如, S="ace"是L="abcde"的一个子序列且有效字符是a、c、e, 而"aec"不是有效子序列, 且有效字符只有a、e。

输入描述

输入两个字符串S和L都只包含英文小写字母。S长度<=100L长度<=500,000。

先输入S再输入L每个字符串占一行。

输出描述

输出S串最后一个有效字符在L中的位置。(首位从0开始计算无有效字符返回-1)

用例1

输入

ace
abcde

输出

4

用例2

输入

fgh
abcde

输出

-1

"""

S = list(input())
L = list(input())

res = -1
for s in S:
    try:
        idx = L.index(s)
        L = L[idx+1:]
        res += idx + 1
    except:
        res = -1
        break


print(res)