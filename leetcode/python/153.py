from typing import List

class Solution:
    def findMin_v20220407(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[r] >= nums[l]: return nums[0]
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] < nums[0]:
                r = mid
            else:
                l = mid + 1
        return nums[r]
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
