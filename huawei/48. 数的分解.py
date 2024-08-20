"""
给定一个正整数n, 如果能够分解为m(m > 1)个连续正整数之和, 请输出所有分解中, m最小的分解。如果给定整数无法分解为连续正整数, 则输出字符串N。

输入描述
输入数据为一整数, 范围为 (1,2^30]

输出描述
比如输入为:

21

输出:

21=10+11

示例1
输入：
21

输出：
21=10+11

说明：
21可以分解的连续正整数组合的形式有多种:
21=1+2+3+4+5+6
21=6+7+8
21=10+11
因21=10+11, 是最短的分解序列。所以答案是21=10+11
"""

n = int(input())

res = []
for start in range(0, n-1):
    for end in range(start+1, n):
        if sum(range(start, end)) == n:
            res.append(list(range(start, end)))

res = sorted(res, key=lambda x: len(x))


if res:
    print(f"{n}=" + "+".join(map(str, res[0])))
else:
    print(n)
