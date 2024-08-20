"""
题目: 给定一个数字, 我们按照如下规则把它翻译为字符串: 0翻译成a, 1翻译成b, ……, 11翻译成l, ……, 25翻译成z。一个数字可能有多个翻译。例如, 12258有5种不同的翻译, 分别是bccfi、bwfi、bczi、mcfi和mzi。请编程实现一个函数, 用来计算一个数字有多少种不同的翻译方法。
"""

def func(num):
    s = str(num)
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        one_digit = int(s[i-1:i])
        two_digits = int(s[i-2:i])

        if 10 <= two_digits <= 25:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]

    return dp[n]

# Example usage:
print(func(12258))  # Output: 5
print(func(295))
