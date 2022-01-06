from typing import List

class Solution:
    """
    - dp[j] 代表装满容量为j的背包有几种硬币组合
    - 转移方程：dp[j] = dp[j] + dp[j - coin]
    当前填满j容量的方法数 = 之前填满j容量的硬币组合数 + 填满j - coin容量的硬币组合数\\
    也就是当前硬币coin的加入，可以把j -coin容量的组合数加入进来, 和01背包差不多，唯一的不同点在于硬币可以重复使用，一个逆序一个正序的区别
    - 返回dp[-1]，也就是dp[amount]
    """
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]

