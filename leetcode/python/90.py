from typing import List
from itertools import combinations
class Solution:
    def subsetsWithDup_v20220125(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, u):
            if u == len(nums):
                res.append(path.copy())
                return
            k = u + 1
            while k < len(nums) and nums[k] == nums[u]: k += 1
            for i in range(k-u+1):
                dfs(nums, k)
                path.append(nums[u])
            for i in range(k-u+1): path.pop()

        res = []
        path = []
        nums = sorted(nums)
        dfs(nums, 0)
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, index, res, path):
            res.append(path.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(nums, i + 1, res, path)
                path.pop()

        res = []
        path = []
        nums.sort()
        dfs(nums, 0, res, path)
        return res
