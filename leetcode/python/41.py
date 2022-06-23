class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set([n for n in nums if n > 0])))
        for i in range(1, len(nums)+1):
            if i != nums[i-1]: return i
        return len(nums) + 1
