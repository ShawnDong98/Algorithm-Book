from typing import List

class Solution:
    """
        - 子问题 1：以 −2 结尾的连续子数组的最大和是多少
        - 子问题 2：以 1 结尾的连续子数组的最大和是多少；

        定义状态（定义子问题）: dp[i]：表示以 nums[i] 结尾 的 连续 子数组的最大和。

        状态转移方程（描述子问题之间的联系）:
            - 如果 dp[i - 1] > 0，那么可以把 nums[i] 直接接在 dp[i - 1] 表示的那个数组的后面，得到和更大的连续子数组；
            - 如果 dp[i - 1] <= 0，那么 nums[i] 加上前面的数 dp[i - 1] 以后值不会变大。于是 dp[i] 「另起炉灶」，此时单独的一个 nums[i] 的值，就是 dp[i]。

            dp[i] = dp[i−1]+nums[i], if dp[i−1]>0
            dp[i] = nums[i], if dp[i−1]≤0

            或

            dp[i] = max{nums[i],dp[i−1]+nums[i]}

    """
    def maxSubArray_20211225(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        dp = [0 for _ in range(len(nums))]

        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] >= 0: dp[i] = dp[i-1] + nums[i]
            else: dp[i] = nums[i]

        return max(dp)

    def maxSubArray_s1(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)
