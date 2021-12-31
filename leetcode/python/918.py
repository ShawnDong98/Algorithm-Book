from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        a_max, a_min, res_max, res_min = nums[0], nums[0], nums[0], nums[0]
        for i in range(1, n):
            a_max = max(nums[i], nums[i] + a_max)
            res_max = max(res_max, a_max)
            a_min = min(nums[i], nums[i] + a_min)
            res_min = min(res_min, a_min)
        return max(res_max, sum(nums) - res_min) if res_max > 0 else res_max 