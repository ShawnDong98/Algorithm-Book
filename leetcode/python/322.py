from typing import List

class Solution:
    """
    假设硬币种类 = {1, 2, 5}, 总金额N = 7。我们从小金额开始逐渐堆积木慢慢逼近目标金额N = 7的解:

    (1) ans(N = 1) = 1
    总金额为1时, 只能用面额为1的硬币

    (2) ans(N = 2) = min[ans(N = 1) + 1, 1] = 1
    在总金额为1的解上多加一枚面额为1的硬币, 或直接用面额为2的硬币, 显然后者更优

    (3) ans(N = 3) = min[ans(N = 1) + 1, ans(N = 2) + 1] = 2
    在总金额为1的解上多加一枚面额为2的硬币，或在总金额为2的解上多加一枚面额为1的硬币

    .........

    (7) ans(N = 7) = min[ans(N = 2) + 1, ans(N = 5) + 1, ans(N = 6) + 1] = 2
    在总金额为2的解上多加一枚面额为5的硬币, 或在总金额为5的解上多加一枚面额为2的硬币, 或在总金额为6的解上多加一枚面额为1的硬币

    该题运用动态规划的思想就是：通过不断求解小面额的解，一点点地逼近目标面额的最终解
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                diff = i - coin
                if diff >= 0:
                    dp[i] = min(dp[diff] + 1, dp[i])

        return dp[-1] if dp[-1] != float("inf") else -1