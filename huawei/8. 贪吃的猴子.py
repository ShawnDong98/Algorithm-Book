"""
一只贪吃的猴子, 来到一个果园, 发现许多串香蕉排成一行, 每串香蕉上有若干根香蕉。每串香蕉的根数由数组 numbers 给出。猴子获取香蕉, 每次都只能从行的开头或者末尾获取, 并且只能获取 N 次, 求猴子最多能获取多少根香蕉。

输入描述

第一行为数组numbers的长度

第二行为数组numbers的值每个数字通过空格分开

第三行输入为N, 表示获取的次数

输出描述

按照题目要求能获取的最大数值

示例1

```
输入
7
1 2 2 7 3 6 1
3

输出
10

```

示例2

```
输入
3
1 2 3
3

输出
6

说明
全部获取所有的香蕉, 因此最终根数为1+2+3 = 6
```

示例3

```
输入
4
4 2 2 3
2

输出
7

说明
第一次获取香蕉为行的开头, 第二次获取为行的末尾, 因此最终根数为4+3 =7
```
"""

n = int(input())
numbers = list(map(int, input().split()))
N = int(input())

left = 0
right = n-1

total = 0
for i in range(N):
    if numbers[left] > numbers[right]:
        total += numbers[left]
        left += 1
    else:
        total += numbers[right]
        right -= 1

print(total)