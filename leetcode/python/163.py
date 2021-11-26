from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) + 1
        nums = [float("-inf")] + nums + [float("-inf")]
        for i in range(1, right):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i-1
        return 0

    def isPeak(left, mid, right):
        if left < mid and mid < right:
            return False
        return True


nums = [1,2]
s = Solution()
print(s.findPeakElement(nums))
