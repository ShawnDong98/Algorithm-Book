from typing import List

class Solution:
    """
    dp[i] 表示前 i 天的最大利润，因为我们始终要使利润最大化，则：

        dp[i] = max(dp[i-1], prices[i]-minprice)

    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minprice)

        return dp[-1]
