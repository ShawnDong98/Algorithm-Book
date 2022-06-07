class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 1
        while k > 0 and nums[k - 1] >= nums[k]: k -= 1
        if k <= 0:
            nums[:] = nums[::-1]
        else:
            t = k
            while t < len(nums) and nums[t] > nums[k - 1]: t += 1
            nums[t - 1], nums[k - 1] = nums[k - 1], nums[t - 1]
            nums[k:] = nums[k:][::-1]

