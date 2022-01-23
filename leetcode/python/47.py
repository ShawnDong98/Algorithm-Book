from typing import List
from itertools import combinations, permutations



class Solution:
    def permuteUnique_v20220123(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.path = [0] * len(nums)
        self.st = [0] * len(nums)
        nums = sorted(nums)
        self.dfs(nums, 0)
        return self.ans
    def dfs(self, nums, u):
        if u == len(nums):
            self.ans.append(self.path.copy())
            return
        for i in range(len(nums)):
            if not self.st[i]:
                if (i and nums[i-1] == nums[i] and not self.st[i-1]):
                    continue
                self.st[i] = True
                self.path[u] = nums[i]
                self.dfs(nums, u+1)
                self.st[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        1 1 1 2 2 3 3 3

        人为规定顺序
        """
       def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return

            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth+1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0: return []
        nums.sort()
        used = [False] * size
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

nums = [1, 2, 3, 1]
S = Solution()
print(S.permuteUnique(nums))
