"""
在学校中, N个小朋友站成一队, 第i个小朋友的身高为height[i], 第i个小朋友可以看到的第一个比自己身高更高的小朋友j, 那么j是i的好朋友(要求j > i)。请重新生成一个列表, 对应位置的输出是每个小朋友的好朋友位置, 如果没有看到好朋友, 请在该位置用0代替。小朋友人数范围是 [0, 40000]。

用例1:

输入

2
100 95

输出

0 0

说明

> 第一个小朋友身高100, 站在队尾位置, 向队首看, 没有比他身高高的小朋友, 所以输出第一个值为0。第二个小朋友站在队首, 前面也没有比他身高高的小朋友, 所以输出第二个值为0。

用例2:

输入

8
123 124 125 121 119 122 126 123

输出

1 2 6 5 5 6 0 0

说明

> 123的好朋友是1位置上的124 
124的好朋友是2位置上的125
125的好朋友是6位置上的126
以此类推
"""

n = int(input())
height = list(map(int, input().split()))

res = []

for i in range(len(height)-1):
    flag = 0
    for j in range(i+1, len(height)):
        if height[j] > height[i]:
            flag = 1
            res.append(j)
            break
    if not flag:
        res.append(0)
res.append(0)


print(" ".join(map(str, res)))