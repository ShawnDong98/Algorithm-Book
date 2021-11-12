from typing import List

class Solution:
    """
    状态:
    - dp[i]含义：偷窃i号房屋后所获金额

    初始状态:
    - dp[0] = nums[0],dp[1] = nums[1]

    状态转移:
    - max(dp[i - 2], dp[i - 3]) + nums[i]，（注意i == 2的情况额外考虑）

    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        dp = [0] * n
        dp[0], dp[1] = nums[0], nums[1]

        for i in range(2, n):
            dp[i] = max(dp[i - 2], dp[i - 3] if i >= 3 else 0) + nums[i]

        return max(dp[-1], dp[-2])