from typing import List

class Solution:
    """
        定义状态：
        - dp0：手里没股票，没有处于冷冻期
        - dp1：手里没股票，并且处于冷冻期
        - dp2：手里有股票

        初始化状态：
        - dp0 = 0
        - dp1 = float("-inf")，因为第一天不会出现冷冻期，不过这里赋值为0也没关系其实
        - dp2 = - prices[0]

        状态转移：
        因为本题是有冷冻期的，不能像前面几题那样允许存在当天卖出再买入的情况，因此务必暂存一下更新后的状态，具体看代码
        - new_dp0 = max(dp0, dp1)
          前一天也是dp0状态，或者前一天是dp1状态，今天解冻了变成dp0状态
        - new_dp1 = dp2 + prices[i]
          必然是前一天卖出了才导致今天冷冻，从前一天的dp2状态转移到今天的dp1状态
        - new_dp2 = max(dp2, dp0 - prices[i])
          前一天也是dp2状态，或者前一天是dp0状态，今天买入一笔变成了dp2状态

        最后一定是手里没有股票赚的钱最多，因此最后返回dp0和dp1的最大值
    """
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        # 手里没股票， 没有处于冷冻期
        dp0 = 0
        # 手里没股票，并且处于冷冻期
        dp1 = float("-inf")
        # 手里有股票
        dp2 = -prices[0]

        for i in range(1, len(prices)):
            new_dp0 = max(dp0, dp1)
            new_dp1 = dp2 + prices[i]
            new_dp2 = max(dp2, dp0 - prices[i])
            dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2
        
        return max(dp0, dp1)
