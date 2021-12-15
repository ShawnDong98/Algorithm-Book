from typing import List
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                dfs(j + 1, tmp + [nums[j]])

        dfs(0, [])
        return res

    def subsets_combinations(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) + 1):
            for j in combinations(nums, i):
                res.append(list(j))
        return res

nums = [1, 2, 3]
S = Solution()
print(S.subsets(nums))

