class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            l_h = height[l]
            r_h = height[r]
            res = max(res, min(l_h, r_h) * (r - l))
            if l_h > r_h: r -= 1
            else: l += 1

        return res
