"""
服务之间交换的接口成功率作为服务调用关键质量特性, 某个时间段内的接口失败率使用一个数组表示, 数组中每个元素都是单位时间内失败率数值, 数组中的数值为0到100的整数, 给定一个数值minAverageLost表示某个时间段内平均失败率容忍值, 即平均失败率小于等于minAverageLost, 找出数组中最长时间段, 如果未找到则直接返回NULL。

输入描述
有两行内容, 

第一行为 minAverageLost, 

第二行为数组, 数组元素通过空格(" ")分隔,

minAverageLost及数组中元素取值范围为0~100的整数, 数组元素的个数不会超过100个

输出描述
找出平均值小于等于minAverageLost的最长时间段, 输出数组下标对, 格式{beginIndex}-{endIndex} (下标从0开始), 

如果同时存在多个最长时间段, 则输出多个下标对且下标对之间使用空格(” “)拼接, 多个下标对按下标从小到大排序。

示例1

```
输入: 
1
0 1 2 3 4

输出: 
0-2

说明: 
A、输入解释: minAverageLost=1, 数组[0, 1, 2, 3, 4]
B、前3个元素的平均值为1, 因此数组第一个至第三个数组下标, 即0-2
```

示例2

```
输入: 
2
0 0 100 2 2 99 0 2

输出: 
0-1 3-4 6-7

说明: 
A、输入解释: minAverageLost=2, 数组[0, 0, 100, 2, 2, 99, 0, 2]
B、通过计算小于等于2的最长时间段为: 数组下标为0-1即[0, 0], 数组下标为3-4即[2, 2], 数组下标为6-7即[0, 2], 这三个部分都满足平均值小于等2的要求, 因此输出0-1 3-4 6-7
```
"""

minAverageLost = int(input())
arr = list(map(int, input().split()))

res = []
for start in range(len(arr) - 1):
    for end in range(start+1, len(arr)):
        if sum(arr[start:end+1]) / len(arr[start:end+1]) <= minAverageLost:
            res.append((start, end))


res = sorted(res, key=lambda x: -(x[1] - x[0]))

res = [f"{r[0]}-{r[1]}" for r in res if (r[1] - r[0]) == (res[0][1] - res[0][0])]

print(" ".join(res))
