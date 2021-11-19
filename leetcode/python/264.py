class Solution:
    """
    定义 3 个指针 index2, index3, index5 分别表示丑数集合中还没乘过 2，3，5 的丑数位置

    每次新的丑数 dp[i] = min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5)

    根据 dp[i] 是由 index2, index3, index5 中的哪个相乘得到的，对应的把此 index + 1，表示还没乘过该 index 的最小丑数变大了

    """
    def nthUglyNumber(self, n: int) -> int:
        if n < 0: 
            return 0 
        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2] : index2 += 1
            if dp[i] == 3 * dp[index3] : index3 += 1
            if dp[i] == 5 * dp[index5] : index5 += 1

        return dp[n - 1]

