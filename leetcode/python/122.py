from typing import List

class Solution:
    """
    本题在交易股票的过程中，一共会有2种状态：
        - dp0：手里没股票
        - dp1：手里有股票
    初始化2种状态：
        - dp0 = 0
        - dp1 = -prices[0]
    对2种状态进行状态转移：
        - dp0 = max(dp0, dp1 + prices[i])
        前一天也是dp0状态，或者前一天是dp1状态，今天卖出一笔变成dp0状态
        - dp1 = max(dp1, dp0 - prices[i])
        前一天也是dp1状态，或者前一天是dp0状态，今天买入一笔变成dp1状态
    最后一定是手里没有股票赚的钱最多，因此返回的是dp0
    """
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0
        dp1 = -prices[0]
        for i in range(1, len(prices)):
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0 - prices[i])

        return dp0