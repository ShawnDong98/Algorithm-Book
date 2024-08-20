"""
幼儿园组织活动, 老师布置了一个任务: 每个小朋友去了解与自己同一个小区的小朋友还有几个。我们将这些数量汇总到数组 garden 中。

请根据这些小朋友给出的信息, 计算小朋友至少有几个？

输入
garden = [2, 2, 3]
1
说明: garden数组长度最大为999。每个小区的小朋友数量最多1000人, 也就是garden的范围为[0,999]

输出
一个数字

示例
输入
2 2 3

输出
7

输入
2 2 2 2 3

输出
10

说明
第一个小朋友反馈有两个小朋友和自己同一小区, 即此小区有3个小朋友

第二个小朋友反馈有两个小朋友和自己同一小区, 即此小区有3个小朋友。

这两个小朋友, 可能是同一小区的, 且此小区的小朋友只有3个人。

第三个小朋友反馈还有3个小朋友与自己同一小区, 则这些小朋友只能是另外一个小区的。这个小区有4个小朋友。

班级里至少有3+4 = 7个小朋友。
"""

from collections import Counter
import math

inp = list(map(int, input().split()))

cnt = Counter(inp)

res = 0
for k, v in cnt.items():
    """
    k 是一个小区除自己外小朋友的数量， 该小区有 k + 1 个小朋友
    v 有这么多小朋友说自己小区还有 k 个 小朋友
    """
    res += math.ceil(v / (k+1)) * (k+1)

print(res)