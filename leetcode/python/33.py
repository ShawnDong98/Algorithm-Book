from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


nums = [4,5,6,7,0,1,2]
target = 0

S = Solution()
print(S.search(nums, target))
