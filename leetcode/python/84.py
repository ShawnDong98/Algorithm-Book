from typing import List
class Solution:
    def largestRectangleArea_v20220415(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [-1] * n
        stk = []

        for i in range(n):
            while len(stk) > 0 and heights[stk[-1]] >= heights[i]: stk.pop()
            if len(stk) == 0: left[i] = -1
            else: left[i] = stk[-1]
            stk.append(i)

        stk = []
        for i in range(n-1, -1, -1):
            while len(stk) and heights[stk[-1]] >= heights[i]: stk.pop()
            if len(stk) == 0: right[i] = n
            else: right[i] = stk[-1]
            stk.append(i)

        res = 0
        for i in range(n):
            res = max(res, heights[i] * (right[i] - left[i] - 1))
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res
