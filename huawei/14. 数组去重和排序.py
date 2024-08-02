"""
给定一个乱序的数组，删除所有的重复元素，使得每个元素只出现一次，并且按照出现的次数从高到低进行排序，相同出现次数按照第一次出现顺序进行先后排序。

用例

输入

1,3,3,3,2,4,4,4,5

输出

3,4,1,2,5

备注 数组大小不超过100 数组元素值大小不超过100。
"""

from collections import Counter

inp = list(map(int, input().split(",")))

inp = Counter(inp)

inp = sorted(inp.items(), key=lambda x: -x[1])

print(",".join(map(str, [k for k, v in inp])))