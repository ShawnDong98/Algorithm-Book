class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        res = 0
        for x in nums:
            if x in S and x-1 not in S:
                y = x
                S.remove(x)
                while y+1 in S:
                    y += 1
                    S.remove(y)
                res = max(res, y - x + 1)

        return res
