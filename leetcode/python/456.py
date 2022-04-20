class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        right = float("-inf")
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < right: return True
            while len(stk)!=0 and nums[i] > stk[-1]:
                right = max(right, stk[-1])
                stk.pop()
            stk.append(nums[i])


        return False
