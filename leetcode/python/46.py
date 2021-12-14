from typing import List
from itertools import permutations

class Solution:
    """
    1 2 3

    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()
        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False] * size
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

    def permute_itertools(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


nums = [1,2,3]
S = Solution()
print(S.permute(nums))
