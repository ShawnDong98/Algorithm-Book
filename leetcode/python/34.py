import bisect
from typing import List

class Solution:
    def searchRange_v20220404(self, nums: List[int], target: int) -> List[int]:
        lb = bisect.bisect_left(nums, target)
        rb = bisect.bisect_right(nums, target) - 1
        if not nums: return [-1, -1]
        if (lb == len(nums) or nums[lb] != target): return [-1, -1]
        return [lb, rb]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound(nums: List[int], target: int) -> List[int]:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        def right_bound(nums: List[int], target: int) -> List[int]:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left

        lb = left_bound(nums, target)
        rb = right_bound(nums, target) - 1

        # 为空检测
        if not nums: return [-1, -1]
        # target不存在检测， or前表示搜索完未找到目标，
        # or后虽然target在数组范围内， 但不存在该值。例如数组{3, 6, 7},
        # target为5， 则返回[-1, -1]
        if (lb == len(nums) or nums[lb] != target): return [-1, -1]
        return [lb, rb]

