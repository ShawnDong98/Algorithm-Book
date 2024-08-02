"""
给定两个整数数组 array1 array2, 数组元素按升序排列。假设从 array1 array2 中分别取出一个元素可构成一对元素, 现在需要取出 k 对元素, 并对取出的所有元素求和, 计算和的最小值。注意：两对元素如果对应于 array1 array2 中的两个下标均相同, 则视为同一对元素。

输入描述
输入两行数组arr1、arr2
每行首个数字为数组大小size,  0 < size <= 100
arr1, arr2中的每个元素e,  0< e <1000
接下来一行, 正整数k 0 < k <= arr1.size * arr2.size

输出描述
满足要求的最小值

示例一
输入

3 1 1 2
3 1 2 3
2

输出

4

说明：
用例中需要取两个元素, 取第一个数组第0个元素与第二个数组第0个元素组成一个元素[1,1];
取第一个数组第1个元素与第二个数组第0个元素组成一个元素[1,1];
求和为1+1+1+1=4 ,满足要求最小
"""

arr1 = list(map(int, input().split()))[1:]
arr2 = list(map(int, input().split()))[1:]

pt1 = 0
pt2 = 0

k = int(input())
res = []

for i in range(k):
    res.append(arr1[pt1])
    res.append(arr2[pt2])
    if arr1[pt1] <= arr2[pt2]:
        pt1 += 1
    else:
        pt2 += 1
print(sum(res))

