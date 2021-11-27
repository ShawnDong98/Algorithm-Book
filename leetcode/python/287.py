from typing import List
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k, v in c.items():
            if v > 1:
                return k
