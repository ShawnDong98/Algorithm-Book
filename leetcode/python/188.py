from typing import List

class Solution:
    """
        先做一下预处理
        - 特判：如果prices长度是0或1，返回0；如果k为0，返回0
        - n天最多交易n/2次，如果k>n/2的话其实交易不了这么多次，所以 k = min(k, n//2)

        定义状态，总共会有2k+1种状态
        - dp0 一直没买
        - dp1 买了1次
        - dp2 买了1次，卖了1次
        - dp3 买了2次，卖了1次
        - dp4 买了2次，卖了2次
        - dp5 买了3次，卖了2次
        - dp6 买了3次，卖了3次
        - ...
        - dp2k 买了k次，卖了k次

        初始化状态
        - dp[0]始终为0
        - dp[1]为初始化为第一天就买入的状态，令其等于 - prices[0]
        - 其余状态都不可能在第一天发生，初始化为足够小的值

        状态转移
        - 外层循环从prices[1]开始往后遍历
        - 内层循环遍历所有状态进行相应的状态转移
        - - dp[0]一直为0所以不用转移，从dp[1]开始转移
        - - 如果当前状态索引j为奇数，也就是手头有股票的情况
             dp[j] = max(dp[j], dp[j - 1] - prices[i])
            前一天也是dp[j]状态；或者前一天是dp[j - 1]状态，今天卖出一笔变成dp2状态
        - - 如果当前状态索引j为偶数，也就是手头没有股票的情况
             dp[j] = max(dp[j], dp[j - 1] + prices[i])
            前一天也是dp[j]状态；或者前一天是dp[j - 1]状态，今天买入一笔变成dp2状态

        最后一定是手里没有股票赚的钱最多，但不一定交易次数越多赚得越多，应该要返回所有偶数状态的最大值；但是代码的写法中其实允许了同一天买入卖出的，只不过因为一天的价格不变而不会对结果有影响，因此最大值是必然会转移到dp[2k]的，所以只要返回dp[2k]就可以了，也就是dp[-1]
    """
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 or k == 0: return 0
        k = min(k, n//2)

        dp = [float("-inf")] * (2 * k + 1)
        dp[0] = 0
        dp[1] = -prices[0]

        for i in range(1, n):
            for j in range(1, 2 * k + 1):
                if j & 1:
                    dp[j] = max(dp[j], dp[j - 1] - prices[i])
                else:
                    dp[j] = max(dp[j], dp[j - 1] + prices[i])
        return dp[-1]


