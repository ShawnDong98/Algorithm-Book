from collections import defaultdict
from typing import List

class Solution:
    def twoSum_v20220317(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)
        res = []
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                res.append(hash_map[target - nums[i]])
                res.append(i)
                return res
            hash_map[nums[i]] = i
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
nums = [3, 2, 4]
target = 6
S = Solution()
print(S.twoSum(nums, target))
