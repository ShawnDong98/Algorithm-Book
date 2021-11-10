from typing import List

class Solution:
    """
    到最后交易结束时，一共会有5种状态：
        - dp0：一直不买
        - dp1：到最后也只买入了一笔
        - dp2：到最后买入一笔，卖出一笔
        - dp3：到最后买入两笔，卖出一笔
        - dp4：到最后买入两笔，卖出两笔
    初始化5种状态：
        - dp0 = 0
        - dp1 = -prices[0]
        因为第一天不可能会有dp2，dp3，dp4三种状态，因此将这三者置为负无穷
        - dp2 = float("-inf")
        - dp3 = float("-inf")
        - dp4 = float("-inf")
    对5种状态进行状态转移。
        - dp0 = 0
        # 一直为0
        - dp1 = max(dp1, dp0 - prices[i])
        # 前一天也是dp1状态，或者前一天是dp0状态，今天买入一笔变成dp1状态
        - dp2 = max(dp2, dp1 + prices[i])
        # 前一天也是dp2状态，或者前一天是dp1状态，今天卖出一笔变成dp2状态
        - dp3 = max(dp3, dp2 - prices[i])
        # 前一天也是dp3状态，或者前一天是dp2状态，今天买入一笔变成dp3状态
        - dp4 = max(dp4, dp3 + prices[i])
        # 前一天也是dp4状态，或者前一天是dp3状态，今天卖出一笔变成dp4状态
    最后一定是手里没有股票赚的钱最多，但不一定交易次数越多赚得越多，应该要返回dp0，dp2，dp4的最大值；
    但是代码的写法中其实允许了同一天买入卖出的，只不过因为一天的价格不变而不会对结果有影响，因此最大值是必然会转移到dp4的，所以只要返回dp4就可以了
    """
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        # 一直不买
        dp0 = 0
        # 到最后也只买了一笔
        dp1 = -prices[0]
        # 到最后买入一笔，卖出一笔
        dp2 = float("-inf")
        # 到最后买入两笔，卖出一笔
        dp3 = float("-inf")
        # 到最后买入两笔，卖出两笔
        dp4 = float("-inf")

        for i in range(1, len(prices)):
            dp1 = max(dp1, dp0 - prices[i])
            dp2 = max(dp2, dp1 + prices[i])
            dp3 = max(dp3, dp2 - prices[i])
            dp4 = max(dp4, dp3 + prices[i])

        return dp4


