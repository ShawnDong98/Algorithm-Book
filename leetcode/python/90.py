from typing import List
from itertools import combinations
class Solution:
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
