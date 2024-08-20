"""
题目：给你一根长度为 $n$ 的绳子，请把绳子剪成 $m$ 段 ($m$, $n$ 都是整数, $n > 1$ 并且 $m > 1$），每段绳子的长度记为 $k[0], k[1], \cdots, k[m]$。请问 $k[0] \times k[1] \times \cdots \times k[m]$ 可能的最大乘积是多少？例如，当绳子的长度是 8 时，我们把它剪成长 度分别为 2、3、3 的三段，此时得到的最大乘积是 18。
"""
def func(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i-j), j * dp[i-j])


    return dp[n]


n = int(input())
print(func(n))



