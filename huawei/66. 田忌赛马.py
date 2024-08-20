"""
给定两个只包含数字的数组a, b, 调整数组a里面数字的顺序, 使得尽可能多的a[i] > b[i]。数组a和b中的数字各不相同。输出所有可以达到最优结果的a数组数量

输入描述
输入的第一行是数组a中的数字, 其中只包含数字, 每两个数字之间相隔一个空格, a数组大小不超过10

输入的第一行是数组b中的数字, 其中只包含数字, 每两个数字之间相隔一个空格, b数组大小不超过10

输出描述
输出所有可以达到最优结果的a数组数量

示例1
输入：
11 8 20
10 13 7

输出：
1

说明：
最优结果只有一个, a=[11,20,8] , 故输出 1 。

示例2
输入：
11 12 20
10 13 7

输出：
2

说明：
有两个 a 数组的排列可以达到最优结果,  [12,20,11] 和 [11,20,12] , 故输出 2 。
"""
from collections import defaultdict
from itertools import permutations

def func(a, b):

    count = defaultdict(int)
    for a_ in permutations(a):
        cnt = sum([1 if a_[i] > b[i] else 0 for i in range(len(a_)) ])
        count[cnt] += 1

    count = sorted(count.items(), key=lambda x: -x[0])

    return count[0][1]


a = list(map(int, input().split()))

b = list(map(int, input().split()))

print(func(a, b))