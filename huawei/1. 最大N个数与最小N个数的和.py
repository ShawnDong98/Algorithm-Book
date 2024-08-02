"""
给定一个数组, 编写一个函数来计算它的最大N个数与最小N个数的和。

你需要对数组进行去重。

说明：

*数组中数字范围[0, 1000]

*最大N个数与最小N个数不能有重叠, 如有重叠, 输入非法返回-1

*输入非法返回-1


输入：
5
95 88 83 64 100
2

输出：
342

说明：
最大2个数[100,95],最小2个数[83,64],输出为342

输入：
5
3 2 3 4 2
2

输出：
-1

说明：
最大2个数[4,3] 最小2个数[3,2], 有重叠输出为-1
"""

def Sum_MaxN_and_MinN(seq, N):
    sorted_seq = sorted(set(seq))
    if N + N > len(sorted_seq):
        return -1
    
    MaxN = sorted_seq[-N:]
    MinN = sorted_seq[:N]
    if set(MaxN) & set(MinN):
        return -1

    return sum(MaxN + MinN)




n = int(input())
seq = list(map(int, input().split()))
N = int(input())
print(Sum_MaxN_and_MinN(seq, N))
