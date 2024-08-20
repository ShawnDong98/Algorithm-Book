"""
题目描述：

中秋节, 公司分月饼, m个员工, 买了n个月饼, m<=n, 每个员工至少分1个月饼, 但可以分多个, 单人分到最多月饼的个数是Max1, 单人分到第二多月饼个数是Max2, Max1-Max2<=3, 单人分到第n-1多月饼个数是Max(n-1), 单人分到第n多月饼个数是Max(n), Max(n-1)-Max(n)<=3, 问有多少种分月饼的方法?

输入描述：
每一行输入m n,表示m个员工, n个月饼, m<=n

输出描述：

输出有多少种月饼分法

示例：

输入
2 4

输出
2
"""

# def count_ways(m, n):
#     # 初始化动态规划数组
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
    
#     # 边界条件
#     for i in range(1, n + 1):
#         dp[1][i] = 1
    
#     # 填充动态规划数组
#     for i in range(2, m + 1):
#         for j in range(i, n + 1):
#             for k in range(j - 3, j):
#                 if k >= i - 1:
#                     dp[i][j] += dp[i - 1][k]
    
#     # 返回总的分法数量
#     return dp[m][n]




m, n = map(int, input().split())

print(count_ways(m, n))  # 输出分配方法数


