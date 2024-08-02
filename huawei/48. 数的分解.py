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
for m in range(2, n):
    for a in range(1, n):
        total = sum(a + i for i in range(m))
        if total == n:
            res.append([a+i for i in range(m)])

if len(res) == 0:
    print(n)
else:
    res = sorted(res, key=lambda x: len(x))
    print(f"{n}=" + "+".join(map(str, res[0])))
